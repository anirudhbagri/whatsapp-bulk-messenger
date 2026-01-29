# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'whatsapp-messenger-ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QListWidget, QListWidgetItem,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 669)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #181C14;\n"
"}\n"
"QTabWidget::pane {\n"
"    border: 1px solid #D1D1D1;\n"
"    background-color: #3C3D37;\n"
"    border-radius: 8px;\n"
"}\n"
"QTabBar::tab {\n"
"    background-color: #DCDCDC;\n"
"    color: #666666;\n"
"    padding: 8px 16px;\n"
"    margin-right: 4px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    background-color: white;\n"
"    color: #075E54;\n"
"    font-weight: bold;\n"
"}\n"
"QTabBar::tab:hover:!selected {\n"
"    background-color: #ECECEC;\n"
"}\n"
"QGroupBox {\n"
"    background-color: #697565;\n"
"    border-radius: 6px;\n"
"    margin-top: 12px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #E0E0E0;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 5px 0 5px;\n"
"    color: #ECDFCC;\n"
"}\n"
"QTextEdit, QListWidget {\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 4px;\n"
"    background-color: white;\n"
""
                        "    padding: 4px;\n"
"}\n"
"QProgressBar {\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 4px;\n"
"    background-color: white;\n"
"    text-align: center;\n"
"    color: black;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #25D366;\n"
"    border-radius: 4px;\n"
"}\n"
"QLabel {\n"
"    color: #333333;\n"
"	\n"
"}\n"
"QSpinBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"\n"
"#recipientsTab QPushButton, #mediaTab QPushButton{\n"
"border:none;\n"
"padding: 6px;\n"
"border-radius:5px;\n"
"color:rgb(232, 232, 232);\n"
"\n"
"}\n"
"#addNumberBtn, #addMediaBtn{\n"
"	background-color: rgb(0, 170, 0); \n"
"}\n"
"#addNumberBtn:hover, #addMediaBtn:hover{\n"
"background-color: rgb(0, 120, 0); \n"
"}\n"
"\n"
"#removeNumberBtn, #removeMediaBtn {\n"
"	background-color:rgb(200, 0, 0) \n"
"}\n"
"#removeNumberBtn:hover,  #removeMediaBtn:hover{\n"
"background-color: rgb(170, 0, 0); \n"
"}\n"
"\n"
"#importNumbersBtn, #clearMediaBtn{\n"
"	background-c"
                        "olor: rgb(152, 152, 152); \n"
"}\n"
"#importNumbersBtn:hover, #clearMediaBtn:hover{\n"
"background-color:rgb(142, 165, 144); \n"
"}\n"
"#startBtn {\n"
"	background-color: rgb(0, 170, 0); \n"
"	color:white;\n"
"	border: none;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"\n"
"}\n"
"#startBtn:hover {\n"
"	background-color: rgb(0, 120, 0); \n"
"\n"
"}\n"
"\n"
"#stopBtn {\n"
"	background-color:rgba(195, 14, 4, 100); \n"
"	color:white;\n"
"	border: none;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}\n"
"#stopBtn:enabled{\n"
"background-color:rgba(200, 0, 0, 150);\n"
"}\n"
"#stopBtn:!enabled{\n"
"	\n"
"}\n"
"#stopBtn:hover {\n"
"	background-color: rgb(180, 0, 0);\n"
"	 \n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName(u"headerLayout")
        self.logoLabel = QLabel(self.centralwidget)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMinimumSize(QSize(40, 40))
        self.logoLabel.setMaximumSize(QSize(40, 40))

        self.headerLayout.addWidget(self.logoLabel)

        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setStyleSheet(u"font-size: 18px; font-weight: bold; color: #075E54;")

        self.headerLayout.addWidget(self.titleLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.headerLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget::tab-bar { alignment: center; }")
        self.messageTab = QWidget()
        self.messageTab.setObjectName(u"messageTab")
        self.messageLayout = QVBoxLayout(self.messageTab)
        self.messageLayout.setSpacing(15)
        self.messageLayout.setObjectName(u"messageLayout")
        self.messageLayout.setContentsMargins(20, 20, 20, 20)
        self.messageGroup = QGroupBox(self.messageTab)
        self.messageGroup.setObjectName(u"messageGroup")
        self.messageGroup.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.messageGroup.setFlat(False)
        self.messageGroup.setCheckable(False)
        self.messageFormLayout = QVBoxLayout(self.messageGroup)
        self.messageFormLayout.setSpacing(10)
        self.messageFormLayout.setObjectName(u"messageFormLayout")
        self.messageFormLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.messageFormLayout.setContentsMargins(15, 20, 15, 15)
        self.messageLabel = QLabel(self.messageGroup)
        self.messageLabel.setObjectName(u"messageLabel")
        self.messageLabel.setStyleSheet(u"font-weight: bold; color:#333333;")

        self.messageFormLayout.addWidget(self.messageLabel)

        self.messageEdit = QTextEdit(self.messageGroup)
        self.messageEdit.setObjectName(u"messageEdit")
        self.messageEdit.setMinimumSize(QSize(0, 120))
        self.messageEdit.setStyleSheet(u"color: black;")

        self.messageFormLayout.addWidget(self.messageEdit)


        self.messageLayout.addWidget(self.messageGroup)

        self.optionsGroup = QGroupBox(self.messageTab)
        self.optionsGroup.setObjectName(u"optionsGroup")
        self.optionsFormLayout = QFormLayout(self.optionsGroup)
        self.optionsFormLayout.setObjectName(u"optionsFormLayout")
        self.optionsFormLayout.setHorizontalSpacing(10)
        self.optionsFormLayout.setVerticalSpacing(10)
        self.optionsFormLayout.setContentsMargins(15, 20, 15, 15)
        self.delayLabel = QLabel(self.optionsGroup)
        self.delayLabel.setObjectName(u"delayLabel")

        self.optionsFormLayout.setWidget(0, QFormLayout.LabelRole, self.delayLabel)

        self.delayLayout = QHBoxLayout()
        self.delayLayout.setObjectName(u"delayLayout")
        self.delaySpin = QSpinBox(self.optionsGroup)
        self.delaySpin.setObjectName(u"delaySpin")
        self.delaySpin.setMinimumSize(QSize(100, 0))
        self.delaySpin.setMinimum(1)
        self.delaySpin.setMaximum(60)
        self.delaySpin.setValue(2)
        self.delaySpin.setDisplayIntegerBase(10)

        self.delayLayout.addWidget(self.delaySpin)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.delayLayout.addItem(self.horizontalSpacer_2)

        self.waitLabel = QLabel(self.optionsGroup)
        self.waitLabel.setObjectName(u"waitLabel")

        self.delayLayout.addWidget(self.waitLabel)

        self.waitSpin = QSpinBox(self.optionsGroup)
        self.waitSpin.setObjectName(u"waitSpin")
        self.waitSpin.setMinimum(1)
        self.waitSpin.setValue(2)

        self.delayLayout.addWidget(self.waitSpin)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.delayLayout.addItem(self.horizontalSpacer_5)


        self.optionsFormLayout.setLayout(0, QFormLayout.FieldRole, self.delayLayout)


        self.messageLayout.addWidget(self.optionsGroup)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.messageLayout.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.messageTab, "")
        self.recipientsTab = QWidget()
        self.recipientsTab.setObjectName(u"recipientsTab")
        self.recipientsLayout = QVBoxLayout(self.recipientsTab)
        self.recipientsLayout.setSpacing(15)
        self.recipientsLayout.setObjectName(u"recipientsLayout")
        self.recipientsLayout.setContentsMargins(20, 20, 20, 20)
        self.numbersGroup = QGroupBox(self.recipientsTab)
        self.numbersGroup.setObjectName(u"numbersGroup")
        self.numbersLayout = QVBoxLayout(self.numbersGroup)
        self.numbersLayout.setSpacing(10)
        self.numbersLayout.setObjectName(u"numbersLayout")
        self.numbersLayout.setContentsMargins(15, 20, 15, 15)
        self.infoLabel = QLabel(self.numbersGroup)
        self.infoLabel.setObjectName(u"infoLabel")
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.infoLabel.setFont(font)
        self.infoLabel.setStyleSheet(u"font-weight: bold; color:#333333;")

        self.numbersLayout.addWidget(self.infoLabel)

        self.numbersList = QListWidget(self.numbersGroup)
        self.numbersList.setObjectName(u"numbersList")
        self.numbersList.setStyleSheet(u"QListWidget::item { padding: 6px; }\n"
"QListWidget::item:alternate { background-color: #F7F7F7; }\n"
"QListWidget{color: black;}")
        self.numbersList.setAlternatingRowColors(True)

        self.numbersLayout.addWidget(self.numbersList)

        self.numbersButtonsLayout = QHBoxLayout()
        self.numbersButtonsLayout.setSpacing(10)
        self.numbersButtonsLayout.setObjectName(u"numbersButtonsLayout")
        self.addNumberBtn = QPushButton(self.numbersGroup)
        self.addNumberBtn.setObjectName(u"addNumberBtn")
        self.addNumberBtn.setStyleSheet(u"")

        self.numbersButtonsLayout.addWidget(self.addNumberBtn)

        self.removeNumberBtn = QPushButton(self.numbersGroup)
        self.removeNumberBtn.setObjectName(u"removeNumberBtn")

        self.numbersButtonsLayout.addWidget(self.removeNumberBtn)

        self.importNumbersBtn = QPushButton(self.numbersGroup)
        self.importNumbersBtn.setObjectName(u"importNumbersBtn")

        self.numbersButtonsLayout.addWidget(self.importNumbersBtn)


        self.numbersLayout.addLayout(self.numbersButtonsLayout)


        self.recipientsLayout.addWidget(self.numbersGroup)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.recipientsLayout.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.recipientsTab, "")
        self.mediaTab = QWidget()
        self.mediaTab.setObjectName(u"mediaTab")
        self.mediaLayout = QVBoxLayout(self.mediaTab)
        self.mediaLayout.setSpacing(15)
        self.mediaLayout.setObjectName(u"mediaLayout")
        self.mediaLayout.setContentsMargins(20, 20, 20, 20)
        self.mediaGroup = QGroupBox(self.mediaTab)
        self.mediaGroup.setObjectName(u"mediaGroup")
        self.mediaBoxLayout = QVBoxLayout(self.mediaGroup)
        self.mediaBoxLayout.setSpacing(10)
        self.mediaBoxLayout.setObjectName(u"mediaBoxLayout")
        self.mediaBoxLayout.setContentsMargins(15, 20, 15, 15)
        self.mediaInfoLabel = QLabel(self.mediaGroup)
        self.mediaInfoLabel.setObjectName(u"mediaInfoLabel")
        self.mediaInfoLabel.setStyleSheet(u"font-weight: bold; color:#333333;")

        self.mediaBoxLayout.addWidget(self.mediaInfoLabel)

        self.mediaList = QListWidget(self.mediaGroup)
        self.mediaList.setObjectName(u"mediaList")
        self.mediaList.setStyleSheet(u"QListWidget::item { padding: 6px; }\n"
"QListWidget::item:alternate { background-color: #F7F7F7; }\n"
"QListWidget{color:black;}")
        self.mediaList.setAlternatingRowColors(True)

        self.mediaBoxLayout.addWidget(self.mediaList)

        self.mediaButtonsLayout = QHBoxLayout()
        self.mediaButtonsLayout.setSpacing(10)
        self.mediaButtonsLayout.setObjectName(u"mediaButtonsLayout")
        self.addMediaBtn = QPushButton(self.mediaGroup)
        self.addMediaBtn.setObjectName(u"addMediaBtn")

        self.mediaButtonsLayout.addWidget(self.addMediaBtn)

        self.removeMediaBtn = QPushButton(self.mediaGroup)
        self.removeMediaBtn.setObjectName(u"removeMediaBtn")

        self.mediaButtonsLayout.addWidget(self.removeMediaBtn)

        self.clearMediaBtn = QPushButton(self.mediaGroup)
        self.clearMediaBtn.setObjectName(u"clearMediaBtn")

        self.mediaButtonsLayout.addWidget(self.clearMediaBtn)


        self.mediaBoxLayout.addLayout(self.mediaButtonsLayout)


        self.mediaLayout.addWidget(self.mediaGroup)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mediaLayout.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.mediaTab, "")
        self.statusTab = QWidget()
        self.statusTab.setObjectName(u"statusTab")
        self.statusLayout = QVBoxLayout(self.statusTab)
        self.statusLayout.setSpacing(15)
        self.statusLayout.setObjectName(u"statusLayout")
        self.statusLayout.setContentsMargins(20, 20, 20, 20)
        self.statusGroup = QGroupBox(self.statusTab)
        self.statusGroup.setObjectName(u"statusGroup")
        self.statusFormLayout = QVBoxLayout(self.statusGroup)
        self.statusFormLayout.setSpacing(10)
        self.statusFormLayout.setObjectName(u"statusFormLayout")
        self.statusFormLayout.setContentsMargins(15, 20, 15, 15)
        self.statusText = QTextEdit(self.statusGroup)
        self.statusText.setObjectName(u"statusText")
        self.statusText.setStyleSheet(u"QTextEdit {\n"
"    background-color: #F7F7F7;\n"
"    font-family: 'Consolas', 'Courier New', monospace;\n"
"    line-height: 1.4;\n"
"	color:black;\n"
"}")
        self.statusText.setReadOnly(True)

        self.statusFormLayout.addWidget(self.statusText)

        self.progressLabel = QLabel(self.statusGroup)
        self.progressLabel.setObjectName(u"progressLabel")
        self.progressLabel.setStyleSheet(u"font-weight: bold;")

        self.statusFormLayout.addWidget(self.progressLabel)

        self.progressBar = QProgressBar(self.statusGroup)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 30))
        self.progressBar.setValue(0)

        self.statusFormLayout.addWidget(self.progressBar)

        self.statusButtonsLayout = QHBoxLayout()
        self.statusButtonsLayout.setSpacing(10)
        self.statusButtonsLayout.setObjectName(u"statusButtonsLayout")
        self.startBtn = QPushButton(self.statusGroup)
        self.startBtn.setObjectName(u"startBtn")
        self.startBtn.setMinimumSize(QSize(0, 40))

        self.statusButtonsLayout.addWidget(self.startBtn)

        self.stopBtn = QPushButton(self.statusGroup)
        self.stopBtn.setObjectName(u"stopBtn")
        self.stopBtn.setEnabled(False)
        self.stopBtn.setMinimumSize(QSize(0, 40))

        self.statusButtonsLayout.addWidget(self.stopBtn)


        self.statusFormLayout.addLayout(self.statusButtonsLayout)


        self.statusLayout.addWidget(self.statusGroup)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.statusLayout.addItem(self.verticalSpacer_4)

        self.tabWidget.addTab(self.statusTab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.footerLayout = QHBoxLayout()
        self.footerLayout.setObjectName(u"footerLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.footerLayout.addItem(self.horizontalSpacer_3)

        self.footerLabel = QLabel(self.centralwidget)
        self.footerLabel.setObjectName(u"footerLabel")
        self.footerLabel.setStyleSheet(u"color: #666666; font-size: 10px;")
        self.footerLabel.setAlignment(Qt.AlignCenter)

        self.footerLayout.addWidget(self.footerLabel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.footerLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.footerLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WhatsApp Toplu Mesaj", None))
        self.logoLabel.setText("")
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"WhatsApp Toplu Mesaj G\u00f6nderme", None))
        self.messageGroup.setTitle(QCoreApplication.translate("MainWindow", u"Mesaj \u0130\u00e7eri\u011fi", None))
        self.messageLabel.setText(QCoreApplication.translate("MainWindow", u"G\u00f6nderilecek Mesaj:", None))
        self.messageEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.messageEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buraya g\u00f6nderilecek mesaj\u0131 yaz\u0131n...", None))
        self.optionsGroup.setTitle(QCoreApplication.translate("MainWindow", u"G\u00f6nderim Se\u00e7enekleri", None))
        self.delayLabel.setText(QCoreApplication.translate("MainWindow", u"Mesajlar Aras\u0131 Bekleme S\u00fcresi:", None))
        self.delaySpin.setSuffix(QCoreApplication.translate("MainWindow", u" saniye", None))
        self.waitLabel.setText(QCoreApplication.translate("MainWindow", u"Elemenlar\u0131n Bulunmas\u0131 \u0130\u00e7in Gereken Maks. S\u00fcre:", None))
        self.waitSpin.setSuffix(QCoreApplication.translate("MainWindow", u" saniye", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.messageTab), QCoreApplication.translate("MainWindow", u"Mesaj Ayarlar\u0131", None))
        self.numbersGroup.setTitle(QCoreApplication.translate("MainWindow", u"Telefon Numaralar\u0131", None))
        self.infoLabel.setText(QCoreApplication.translate("MainWindow", u"Telefon numaralar\u0131n\u0131 \u00fclke koduyla birlikte ekleyin (\u00f6rn: 905551234567)", None))
        self.addNumberBtn.setText(QCoreApplication.translate("MainWindow", u"Numara Ekle", None))
        self.removeNumberBtn.setText(QCoreApplication.translate("MainWindow", u"Se\u00e7ili Numaray\u0131 Sil", None))
        self.importNumbersBtn.setText(QCoreApplication.translate("MainWindow", u"Numaralar\u0131 \u0130\u00e7e Aktar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.recipientsTab), QCoreApplication.translate("MainWindow", u"Al\u0131c\u0131lar", None))
        self.mediaGroup.setTitle(QCoreApplication.translate("MainWindow", u"Eklenecek Medya Dosyalar\u0131", None))
        self.mediaInfoLabel.setText(QCoreApplication.translate("MainWindow", u"G\u00f6ndermek istedi\u011finiz resim, video veya di\u011fer dosyalar\u0131 ekleyin", None))
        self.addMediaBtn.setText(QCoreApplication.translate("MainWindow", u"Dosya Ekle", None))
        self.removeMediaBtn.setText(QCoreApplication.translate("MainWindow", u"Se\u00e7ili Dosyay\u0131 Kald\u0131r", None))
        self.clearMediaBtn.setText(QCoreApplication.translate("MainWindow", u"T\u00fcm Dosyalar\u0131 Temizle", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mediaTab), QCoreApplication.translate("MainWindow", u"Medya Dosyalar\u0131", None))
        self.statusGroup.setTitle(QCoreApplication.translate("MainWindow", u"\u0130\u015flem Durumu", None))
        self.progressLabel.setText(QCoreApplication.translate("MainWindow", u"\u0130lerleme:", None))
        self.startBtn.setText(QCoreApplication.translate("MainWindow", u"G\u00f6nderimi Ba\u015flat", None))
        self.stopBtn.setText(QCoreApplication.translate("MainWindow", u"G\u00f6nderimi Durdur", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.statusTab), QCoreApplication.translate("MainWindow", u"Durum", None))
        self.footerLabel.setText(QCoreApplication.translate("MainWindow", u"WhatsApp Toplu Mesaj G\u00f6nderme Uygulamas\u0131 \u00a9 2025", None))
    # retranslateUi

