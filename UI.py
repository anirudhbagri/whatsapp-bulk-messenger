import sys
import subprocess  # To execute external scripts
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QFileDialog,
    QTabWidget,
)
from PyQt5.QtGui import QIcon

class FileWriteApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("File Writer")
        self.setGeometry(100, 100, 400, 300)

        # Create a central widget to center-align the tab bar
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a horizontal layout for center-aligning the tab bar
        central_layout = QHBoxLayout(central_widget)

        # Create a tabbed interface
        self.tab_widget = QTabWidget(self)
        central_layout.addWidget(self.tab_widget)

        # Create the "Numbers" tab
        self.numbers_tab = QWidget()
        self.tab_widget.addTab(self.numbers_tab, "Numbers")
        self.createNumbersTab(self.numbers_tab, "numbers.txt")

        # Create the "Messages" tab
        self.messages_tab = QWidget()
        self.tab_widget.addTab(self.messages_tab, "Messages")
        self.createMessageTab(self.messages_tab, "message.txt")

        # Load the initial content
        self.loadInitialContent()

    def createNumbersTab(self, tab, file_name):
        # Create a QVBoxLayout for the tab
        layout = QVBoxLayout(tab)

        # Create a QTextEdit widget to display/edit text
        text_edit = QTextEdit()
        layout.addWidget(text_edit)

        # Create a QPushButton to go to the next tab
        next_button = QPushButton("Next", tab)
        next_button.setIcon(QIcon("next_icon.png"))  # Provide an icon
        next_button.clicked.connect(lambda: self.nextTab(text_edit, file_name))
        layout.addWidget(next_button)

    def createMessageTab(self, tab, file_name):
        # Create a QVBoxLayout for the tab
        layout = QVBoxLayout(tab)

        # Create a QTextEdit widget to display/edit text
        text_edit = QTextEdit()
        layout.addWidget(text_edit)

        # Create a QPushButton to send messages
        send_button = QPushButton("Send Message", tab)
        send_button.setIcon(QIcon("send_icon.png"))  # Provide an icon
        send_button.clicked.connect(lambda: self.sendMessages())
        layout.addWidget(send_button)

    def loadInitialContent(self):
        # Load the initial content of "numbers.txt" and "message.txt" when the UI opens
        self.loadFile(self.numbers_tab, "numbers.txt")
        self.loadFile(self.messages_tab, "message.txt")

    def loadFile(self, tab, file_name):
        # Load the content of the specified file into the QTextEdit widget
        file_path = file_name
        try:
            with open(file_path, "r") as file:
                file_content = file.read()
                text_edit = tab.findChild(QTextEdit)
                if text_edit:
                    text_edit.setPlainText(file_content)
        except FileNotFoundError:
            pass

    def nextTab(self, text_edit, file_name):
        # Save the edited content to the current file
        self.saveToFile(text_edit, file_name)

        # Switch to the next tab (if available)
        current_index = self.tab_widget.currentIndex()
        next_index = current_index + 1
        if next_index < self.tab_widget.count():
            self.tab_widget.setCurrentIndex(next_index)

    def saveToFile(self, text_edit, file_name):
        # Save the edited content to the specified file
        file_path = file_name
        text_to_save = text_edit.toPlainText()
        try:
            with open(file_path, "w") as file:
                file.write(text_to_save)
            print(f"Content saved to {file_path}")
        except Exception as e:
            print(f"Error saving to {file_path}: {str(e)}")

    def sendMessages(self):
        # Execute the batch file (Send Messages.bat) for sending messages
        try:
            subprocess.run(["python", "automator.py"])
            print("Messages sent successfully.")
        except Exception as e:
            print(f"Error sending messages: {str(e)}")

def main():
    app = QApplication(sys.argv)
    window = FileWriteApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
