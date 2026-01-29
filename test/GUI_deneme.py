import sys
import os
import glob
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QTextEdit, QFileDialog, QListWidget, 
                             QSpinBox, QProgressBar, QTabWidget, QMessageBox, QLineEdit,
                             QGroupBox, QFormLayout, QListWidgetItem)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QDir
from PyQt5.QtGui import QIcon, QFont
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import time

class WhatsAppSenderThread(QThread):
    progress_update = pyqtSignal(int, str)
    status_update = pyqtSignal(str)
    finished_signal = pyqtSignal()
    
    def __init__(self, numbers, message, media_files, delay_between_messages):
        super().__init__()
        self.numbers = numbers
        self.message = message
        self.media_files = media_files
        self.delay_between_messages = delay_between_messages
        self.stop_requested = False
        
    def run(self):
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--profile-directory=Default")
        options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")
        options.add_argument('--start-maximized')
        options.add_argument("--disable-background-timer-throttling")
        options.add_argument("--disable-renderer-backgrounding")
        
        try:
            self.status_update.emit("Tarayıcı başlatılıyor...")
            
            # ChromeDriver lokasyonunu kontrol et
            chromedriver_path = "chromedriver.exe"
            if not os.path.exists(chromedriver_path):
                self.status_update.emit("Hata: chromedriver.exe bulunamadı!")
                return
                
            svc = webdriver.ChromeService(executable_path=chromedriver_path)
            driver = webdriver.Chrome(service=svc, options=options)
            
            self.status_update.emit("WhatsApp Web açılıyor...")
            driver.get('https://web.whatsapp.com')
            
            # QR kodu taramasını bekleyin
            self.status_update.emit("Lütfen QR kodu tarayın ve ENTER tuşuna basın...")
            delay = 30
            
            # WhatsApp Web'in yüklenmesini bekle
            try:
                WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@data-testid='chat-list']"))
                )
                self.status_update.emit("WhatsApp Web'e giriş yapıldı!")
            except Exception as e:
                self.status_update.emit(f"WhatsApp Web yüklenemedi: {str(e)}")
                driver.quit()
                return
            
            # Mesajları göndermeye başla
            total_number = len(self.numbers)
            for idx, number in enumerate(self.numbers):
                if self.stop_requested:
                    self.status_update.emit("İşlem kullanıcı tarafından durduruldu.")
                    break
                    
                number = number.strip()
                if number == "":
                    continue
                    
                self.progress_update.emit(idx, number)
                self.status_update.emit(f"Mesaj gönderiliyor: {number} ({idx+1}/{total_number})")
                
                try:
                    # URL oluştur ve sayfaya git
                    url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + quote(self.message)
                    driver.get(url)
                    
                    # Olası uyarıları kontrol et
                    try:
                        alert = driver.switch_to.alert
                        alert.accept()
                    except:
                        pass
                    
                    # Sohbetin yüklenmesini bekle
                    message_box = WebDriverWait(driver, delay).until(
                        EC.presence_of_element_located((By.XPATH, "//div[@title='Yazın ya da sesin gelmesi için buraya dokunun']"))
                    )
                    
                    # Eğer medya dosyaları varsa, onları ekle
                    if self.media_files:
                        for img_idx, img_path in enumerate(self.media_files):
                            try:
                                # Ekleme butonuna tıkla
                                attach_button = WebDriverWait(driver, delay).until(
                                    EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='attach-menu-plus']"))
                                )
                                attach_button.click()
                                sleep(1)
                                
                                # Dosya giriş elementini bul
                                image_box = WebDriverWait(driver, delay).until(
                                    EC.presence_of_element_located((By.XPATH, "//input[@accept='*']"))
                                )
                                
                                # Dosyayı gönder
                                image_box.send_keys(os.path.abspath(img_path))
                                sleep(2)
                                
                                self.status_update.emit(f"Dosya eklendi: {os.path.basename(img_path)}")
                            except Exception as e:
                                self.status_update.emit(f"Dosya eklenemedi: {str(e)}")
                    
                    # Gönder butonunu bul ve tıkla
                    send_button = WebDriverWait(driver, delay).until(
                        EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']"))
                    )
                    send_button.click()
                    
                    # Mesajın gönderilmesini bekle
                    sleep(2)
                    
                    # Mesajların arasında belirtilen süre kadar bekle
                    sleep(self.delay_between_messages)
                    
                    self.status_update.emit(f"Mesaj başarıyla gönderildi: {number}")
                    
                except Exception as e:
                    self.status_update.emit(f"Hata: {number} numarasına mesaj gönderilemedi: {str(e)}")
            
            self.status_update.emit("Tüm mesajlar gönderildi!")
            driver.quit()
            self.finished_signal.emit()
            
        except Exception as e:
            self.status_update.emit(f"Kritik hata: {str(e)}")
            self.finished_signal.emit()
    
    def stop(self):
        self.stop_requested = True
        self.status_update.emit("İşlem durdurma istendi, lütfen bekleyin...")


class WhatsAppMessengerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.sender_thread = None
        self.numbers = []
        self.media_files = []
        
    def initUI(self):
        self.setWindowTitle("WhatsApp Toplu Mesaj Gönderme")
        self.setGeometry(100, 100, 800, 600)
        
        # Ana widget ve layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Sekme widget'ı oluştur
        tab_widget = QTabWidget()
        main_layout.addWidget(tab_widget)
        
        # Mesaj sekmesi
        message_tab = QWidget()
        tab_widget.addTab(message_tab, "Mesaj Ayarları")
        
        # Alıcılar sekmesi
        recipients_tab = QWidget()
        tab_widget.addTab(recipients_tab, "Alıcılar")
        
        # Medya sekmesi
        media_tab = QWidget()
        tab_widget.addTab(media_tab, "Medya Dosyaları")
        
        # Durum sekmesi
        status_tab = QWidget()
        tab_widget.addTab(status_tab, "Durum")
        
        # Mesaj sekmesi düzeni
        message_layout = QVBoxLayout(message_tab)
        
        message_group = QGroupBox("Mesaj İçeriği")
        message_form = QVBoxLayout()
        message_group.setLayout(message_form)
        
        # Mesaj içeriği
        message_form.addWidget(QLabel("Gönderilecek Mesaj:"))
        self.message_edit = QTextEdit()
        self.message_edit.setPlaceholderText("Buraya gönderilecek mesajı yazın...")
        message_form.addWidget(self.message_edit)
        
        # Mesaj seçenekleri
        options_group = QGroupBox("Gönderim Seçenekleri")
        options_form = QFormLayout()
        options_group.setLayout(options_form)
        
        self.delay_spin = QSpinBox()
        self.delay_spin.setRange(1, 60)
        self.delay_spin.setValue(10)
        self.delay_spin.setSuffix(" saniye")
        options_form.addRow("Mesajlar Arası Bekleme Süresi:", self.delay_spin)
        
        message_layout.addWidget(message_group)
        message_layout.addWidget(options_group)
        
        # Alıcılar sekmesi düzeni
        recipients_layout = QVBoxLayout(recipients_tab)
        
        # Numara listesi için grup kutusu
        numbers_group = QGroupBox("Telefon Numaraları")
        numbers_layout = QVBoxLayout()
        numbers_group.setLayout(numbers_layout)
        
        self.numbers_list = QListWidget()
        numbers_layout.addWidget(self.numbers_list)
        
        buttons_layout = QHBoxLayout()
        
        self.add_number_btn = QPushButton("Numara Ekle")
        self.add_number_btn.clicked.connect(self.add_number)
        
        self.remove_number_btn = QPushButton("Seçili Numarayı Sil")
        self.remove_number_btn.clicked.connect(self.remove_number)
        
        self.import_numbers_btn = QPushButton("Numaraları İçe Aktar")
        self.import_numbers_btn.clicked.connect(self.import_numbers)
        
        buttons_layout.addWidget(self.add_number_btn)
        buttons_layout.addWidget(self.remove_number_btn)
        buttons_layout.addWidget(self.import_numbers_btn)
        
        numbers_layout.addLayout(buttons_layout)
        recipients_layout.addWidget(numbers_group)
        
        # Medya sekmesi düzeni
        media_layout = QVBoxLayout(media_tab)
        
        media_group = QGroupBox("Eklenecek Medya Dosyaları")
        media_box_layout = QVBoxLayout()
        media_group.setLayout(media_box_layout)
        
        self.media_list = QListWidget()
        media_box_layout.addWidget(self.media_list)
        
        media_buttons = QHBoxLayout()
        
        self.add_media_btn = QPushButton("Dosya Ekle")
        self.add_media_btn.clicked.connect(self.add_media)
        
        self.remove_media_btn = QPushButton("Seçili Dosyayı Kaldır")
        self.remove_media_btn.clicked.connect(self.remove_media)
        
        self.clear_media_btn = QPushButton("Tüm Dosyaları Temizle")
        self.clear_media_btn.clicked.connect(self.clear_media)
        
        media_buttons.addWidget(self.add_media_btn)
        media_buttons.addWidget(self.remove_media_btn)
        media_buttons.addWidget(self.clear_media_btn)
        
        media_box_layout.addLayout(media_buttons)
        media_layout.addWidget(media_group)
        
        # Durum sekmesi düzeni
        status_layout = QVBoxLayout(status_tab)
        
        status_group = QGroupBox("İşlem Durumu")
        status_form = QVBoxLayout()
        status_group.setLayout(status_form)
        
        self.status_text = QTextEdit()
        self.status_text.setReadOnly(True)
        status_form.addWidget(self.status_text)
        
        self.progress_bar = QProgressBar()
        status_form.addWidget(self.progress_bar)
        
        status_buttons = QHBoxLayout()
        
        self.start_btn = QPushButton("Gönderimi Başlat")
        self.start_btn.clicked.connect(self.start_sending)
        
        self.stop_btn = QPushButton("Gönderimi Durdur")
        self.stop_btn.clicked.connect(self.stop_sending)
        self.stop_btn.setEnabled(False)
        
        status_buttons.addWidget(self.start_btn)
        status_buttons.addWidget(self.stop_btn)
        
        status_form.addLayout(status_buttons)
        status_layout.addWidget(status_group)
        
        # Uygulama bilgisi
        info_label = QLabel("WhatsApp Toplu Mesaj Gönderme Uygulaması © 2025")
        info_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(info_label)
        
        # İlk durum mesajı
        self.log_status("Uygulama başlatıldı. WhatsApp Web'e giriş yapmak için 'Gönderimi Başlat' butonuna tıklayın.")
    
    def add_number(self):
        number, ok = QLineEdit.getText(self, "Numara Ekle", 
                                      "Telefon numarasını ülke koduyla birlikte girin (örn: 905551234567):")
        if ok and number:
            self.numbers_list.addItem(number)
            self.numbers.append(number)
            self.log_status(f"Numara eklendi: {number}")
    
    def remove_number(self):
        selected_items = self.numbers_list.selectedItems()
        if not selected_items:
            return
            
        for item in selected_items:
            self.numbers.remove(item.text())
            self.numbers_list.takeItem(self.numbers_list.row(item))
            self.log_status(f"Numara silindi: {item.text()}")
    
    def import_numbers(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Numara Listesi İçe Aktar", "", "Metin Dosyaları (*.txt)")
        if not file_path:
            return
            
        try:
            with open(file_path, "r") as f:
                new_numbers = [line.strip() for line in f.readlines() if line.strip()]
                
                self.numbers.extend(new_numbers)
                self.numbers_list.clear()
                self.numbers_list.addItems(new_numbers)
                
                self.log_status(f"{len(new_numbers)} numara içe aktarıldı.")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Dosya içe aktarılırken hata oluştu: {str(e)}")
    
    def add_media(self):
        file_paths, _ = QFileDialog.getOpenFileNames(self, "Medya Dosyaları Ekle", "", 
                                                  "Medya Dosyaları (*.jpg *.jpeg *.png *.pdf *.mp4)")
        if not file_paths:
            return
            
        for path in file_paths:
            self.media_files.append(path)
            self.media_list.addItem(os.path.basename(path))
            
        self.log_status(f"{len(file_paths)} medya dosyası eklendi.")
    
    def remove_media(self):
        selected_items = self.media_list.selectedItems()
        if not selected_items:
            return
            
        for item in selected_items:
            file_name = item.text()
            for i, path in enumerate(self.media_files):
                if os.path.basename(path) == file_name:
                    self.media_files.pop(i)
                    break
                    
            self.media_list.takeItem(self.media_list.row(item))
            self.log_status(f"Medya dosyası kaldırıldı: {file_name}")
    
    def clear_media(self):
        self.media_files.clear()
        self.media_list.clear()
        self.log_status("Tüm medya dosyaları temizlendi.")
    
    def start_sending(self):
        # Gerekli kontrolleri yap
        if not self.numbers:
            QMessageBox.warning(self, "Uyarı", "Lütfen en az bir telefon numarası ekleyin.")
            return
            
        message = self.message_edit.toPlainText()
        if not message and not self.media_files:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir mesaj yazın veya medya dosyası ekleyin.")
            return
        
        # Butonları güncelle
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        
        # İlerleme çubuğunu hazırla
        self.progress_bar.setRange(0, len(self.numbers))
        self.progress_bar.setValue(0)
        
        # Thread'i başlat
        self.sender_thread = WhatsAppSenderThread(
            self.numbers, 
            message, 
            self.media_files, 
            self.delay_spin.value()
        )
        
        # Sinyalleri bağla
        self.sender_thread.progress_update.connect(self.update_progress)
        self.sender_thread.status_update.connect(self.log_status)
        self.sender_thread.finished_signal.connect(self.sending_finished)
        
        # Thread'i başlat
        self.sender_thread.start()
        self.log_status("Gönderim işlemi başlatıldı...")
    
    def stop_sending(self):
        if self.sender_thread and self.sender_thread.isRunning():
            self.sender_thread.stop()
            self.log_status("Gönderim işlemi durdurma komutu verildi. Lütfen bekleyin...")
    
    def update_progress(self, index, number):
        self.progress_bar.setValue(index + 1)
    
    def sending_finished(self):
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.log_status("Gönderim işlemi tamamlandı.")
    
    def log_status(self, message):
        current_time = time.strftime("%H:%M:%S")
        log_entry = f"[{current_time}] {message}"
        self.status_text.append(log_entry)
        # Otomatik olarak en alta kaydır
        self.status_text.verticalScrollBar().setValue(self.status_text.verticalScrollBar().maximum())

def main():
    app = QApplication(sys.argv)
    window = WhatsAppMessengerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()