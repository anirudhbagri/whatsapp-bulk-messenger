import sys
import os
import time
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QTextEdit, QFileDialog, QListWidget, 
                             QSpinBox, QProgressBar, QTabWidget, QMessageBox, QLineEdit,
                             QGroupBox, QFormLayout, QListWidgetItem, QSplitter)
from PySide6.QtCore import Qt, QThread, Signal, QDir, QSize
from PySide6.QtGui import QIcon, QFont, QPixmap
from urllib.parse import quote
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import time
from PySide6.QtWidgets import QInputDialog
from deneme.GUI import Ui_MainWindow  # Dönüştürülen UI dosyası

class WhatsAppSenderThread(QThread):
    progress_update = Signal(int, str)  # İlerleme durumu için sinyal
    status_update = Signal(str)         # Durum mesajları için sinyal
    finished_signal = Signal()          # İşlem bitişi için sinyal

    def __init__(self, numbers, message, media_files, wait, delay):
        super().__init__()
        self.numbers = numbers
        self.message = message
        self.media_files = media_files
        self.delay = delay * 10
        self.wait = wait 
        self.is_running = True

    def log_status(self, message):
        current_time = time.strftime("%H:%M:%S")
        log_entry = f"[{current_time}] {message}"
        self.status_update.emit(log_entry)  

    def run(self):
        try:
            options = Options()
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            options.add_argument("--profile-directory=Default")
            options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")
            options.add_argument('--start-maximized')
            options.add_argument("--disable-background-timer-throttling")
            options.add_argument("--disable-renderer-backgrounding")

            self.status_update.emit("Tarayıcı başlatılıyor...")

            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            self.driver.get('https://web.whatsapp.com')
            
            self.status_update.emit("WhatsApp Web'e giriş yapın ve QR kodu okutun...")
            # QR kod okutma için bekle
            
            try:
                WebDriverWait(self.driver, 100000).until(
                        EC.presence_of_element_located((By.XPATH, "//h1[text()='Sohbetler']"))
                    )
            except:
                self.status_update.emit("Giriş yapılamadı. QR kodu okutulamadı.")
                self.driver.quit()
                self.finished_signal.emit()
                return
            
            total_number = len(self.numbers)
            for idx, number in enumerate(self.numbers):
                if not self.is_running:
                    self.status_update.emit("İşlem durduruldu.")
                    break
                    
                number = number.strip()
                if number == "":
                    continue
                    
                self.progress_update.emit(idx + 1, number)
                self.status_update.emit(f"Mesaj gönderiliyor: {number}")
                
                try:
                    url = f'https://web.whatsapp.com/send?phone={number}&text={quote(self.message)}'
                    self.driver.get(url)
                    
                    try:
                        WebDriverWait(self.driver, self.delay).until(
                        EC.presence_of_element_located((By.XPATH, "//div[text()='URL yoluyla paylaşılan telefon numarası geçersiz.']"))
                        )
                        self.log_status(f"Geçersiz numara: {number}")
                        continue
                    except:
                        pass

                    # Medya dosyalarını gönder
                    if self.media_files:
                        self.status_update.emit("Medya dosyaları yükleniyor...")
                        for i, media_file in enumerate(self.media_files):
                            attach_button = WebDriverWait(self.driver, self.delay).until(
                                EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='plus']"))
                            )
                            attach_button.click()
                            
                            image_box = WebDriverWait(self.driver, self.delay).until(
                                EC.presence_of_element_located((By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']"))
                            )
                            image_box.send_keys(media_file)
                            time.sleep(self.wait)
                    
                    # Mesajı gönder
                    send_button = WebDriverWait(self.driver, self.delay).until(
                        EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']"))
                    )
                    send_button.click()
                    time.sleep(self.wait)
                    # Yükleme tamamlanana kadar bekle
                    target_div = self.driver.find_element(By.CSS_SELECTOR, "div[data-tab='8'].x3psx0u")
                    WebDriverWait(target_div, 300).until_not(
                        EC.presence_of_element_located((By.TAG_NAME, "circle"))
                    )
                    if self.is_running:
                        self.log_status(f"Mesaj gönderildi: {number}")
                
                except Exception as e:
                    self.status_update.emit(f"Hata: {str(e)}")
                
                time.sleep(self.wait)
            
            self.driver.quit()
            self.finished_signal.emit()
            
        
        except Exception as e:
            self.status_update.emit(f"Kritik hata: {str(e)}")
            self.finished_signal.emit()
    
    def stop(self):  # Yeni stop metodu ekle
        self.is_running = False
        if self.driver:
            self.driver.quit()
        

class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.sender_thread = None
        self.media_files = []
        self.numbers = []
        self.ui.addNumberBtn.clicked.connect(self.add_number)
        # Butonları bağla
        self.ui.startBtn.clicked.connect(self.start_sending)
        self.ui.stopBtn.clicked.connect(self.stop_sending)
        self.ui.removeNumberBtn.clicked.connect(self.remove_number)
        self.ui.importNumbersBtn.clicked.connect(self.import_numbers)
        self.ui.addMediaBtn.clicked.connect(self.add_media)
        self.ui.removeMediaBtn.clicked.connect(self.remove_media)
        self.ui.clearMediaBtn.clicked.connect(self.clear_media)


    def start_sending(self):
        if self.sender_thread and self.sender_thread.isRunning():
            return
        
        self.ui.progressBar.setValue(0)
        message = self.ui.messageEdit.toPlainText()
        delay = self.ui.delaySpin.value()
        wait = self.ui.waitSpin.value()

        if not self.numbers:
            QMessageBox.critical(self, "Hata", "Lütfen en az bir numara ekleyin!")
            return
        
        self.sender_thread = WhatsAppSenderThread(self.numbers, message, self.media_files, wait, delay)
        self.sender_thread.progress_update.connect(self.update_progress)
        self.sender_thread.status_update.connect(self.update_status)
        self.sender_thread.finished_signal.connect(self.sending_finished)
        
        self.ui.startBtn.setEnabled(False)
        self.ui.stopBtn.setEnabled(True)
        self.sender_thread.start()
        
    def stop_sending(self):
        if self.sender_thread:
            self.sender_thread.stop()
            self.ui.startBtn.setEnabled(True)
            self.ui.stopBtn.setEnabled(False)
            self.sender_thread.is_running = False
            self.ui.statusText.append("İşlemler durduruluyor...")
        
            
    def update_progress(self, current, number):
        self.ui.progressBar.setValue(int((current / len(self.numbers)) * 100))
        self.ui.statusText.append(f"İşleniyor: {number} ({current}/{len(self.numbers)})")
        
    def update_status(self, message):
        self.ui.statusText.append(message)
        
    def sending_finished(self):
        self.ui.startBtn.setEnabled(True)
        self.ui.stopBtn.setEnabled(False)
        self.ui.statusText.append("İşlem tamamlandı!")

    def add_number(self):
        number, ok = QInputDialog.getText(self, "Numara Ekle", 
                                      "Telefon numarasını ülke koduyla birlikte girin (örn: 905551234567):")
        if ok and number:
            self.ui.numbersList.addItem(number)
            self.numbers.append(number)
            self.log_status(f"Numara eklendi: {number}")

    def remove_number(self):
        selected_items = self.ui.numbersList.selectedItems()
        if not selected_items:
            return
            
        for item in selected_items:
            self.numbers.remove(item.text())
            self.ui.numbersList.takeItem(self.ui.numbersList.row(item))
            self.log_status(f"Numara silindi: {item.text()}")
    
    def import_numbers(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Numara Listesi İçe Aktar", "", "Metin Dosyaları (*.txt)")
        if not file_path:
            return
            
        try:
            with open(file_path, "r") as f:
                new_numbers = [line.strip() for line in f.readlines() if line.strip()]
                
                self.numbers.extend(new_numbers)
                self.ui.numbersList.clear()
                self.ui.numbersList.addItems(new_numbers)
                
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
            self.ui.mediaList.addItem(os.path.basename(path))
            
        self.log_status(f"{len(file_paths)} medya dosyası eklendi.")
    
    def remove_media(self):
        selected_items = self.ui.mediaList.selectedItems()
        if not selected_items:
            return
            
        for item in selected_items:
            file_name = item.text()
            for i, path in enumerate(self.media_files):
                if os.path.basename(path) == file_name:
                    self.media_files.pop(i)
                    break
                    
            self.ui.mediaList.takeItem(self.ui.mediaList.row(item))
            self.log_status(f"Medya dosyası kaldırıldı: {file_name}")
    
    def clear_media(self):
        self.media_files.clear()
        self.ui.mediaList.clear()
        self.log_status("Tüm medya dosyaları temizlendi.")

    def log_status(self, message):
        current_time = time.strftime("%H:%M:%S")
        log_entry = f"[{current_time}] {message}"
        self.ui.statusText.append(log_entry)
        # Otomatik olarak en alta kaydır
        self.ui.statusText.verticalScrollBar().setValue(self.ui.statusText.verticalScrollBar().maximum())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("windows")
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec())