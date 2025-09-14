import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression

class AddressBookApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('task3.ui', self)
        self.setWindowTitle("Записная книжка")
        
        # Ограничиваем ввод в lineEdit_2 только цифрами
        phone_regex = QRegularExpression(r"^[0-9]*$")  # Только цифры (включая пустое)
        phone_validator = QRegularExpressionValidator(phone_regex, self)
        self.lineEdit_2.setValidator(phone_validator)

        self.pushButton.clicked.connect(self.add_contact)

    def add_contact(self):
        name = self.lineEdit.text().strip()
        phone = self.lineEdit_2.text().strip()
        if not name or not phone:
            return

        contact = f"{name}: {phone}"
        self.listWidget.addItem(contact)
        self.lineEdit.clear()
        self.lineEdit_2.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AddressBookApp()
    window.show()
    sys.exit(app.exec())