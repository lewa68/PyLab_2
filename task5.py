import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStatusBar
from PyQt6.QtGui import QColor
from PyQt6.uic import loadUi

class PlagiarismChecker(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('task5.ui', self)
        self.setWindowTitle("Антиплагиат")
        self.pushButton.clicked.connect(self.check_plagiarism)

    def check_plagiarism(self):
        text1 = self.plainTextEdit.toPlainText().splitlines()
        text2 = self.plainTextEdit_2.toPlainText().splitlines()

        if not text1 and not text2:
            self.show_status("Оба текста пусты", QColor("blue"))
            return
        if not text1 or not text2:
            self.show_status("Один из текстов пуст", QColor("red"))
            return

        total_lines = max(len(text1), len(text2))
        matching_lines = 0

        for line1, line2 in zip(text1, text2):
            if line1.strip().lower() == line2.strip().lower():
                matching_lines += 1


        similarity = matching_lines / total_lines if total_lines > 0 else 0
        threshold = self.doubleSpinBox.value()

        if similarity >= threshold:
            msg = f"⚠️ Плагиат обнаружен! Сходство: {similarity:.2%} (порог: {threshold:.0%})"
            color = QColor("red")
        else:
            msg = f"✅ Плагиат не обнаружен. Сходство: {similarity:.2%}"
            color = QColor("green")

        self.show_status(msg, color)

    def show_status(self, message, color):
        self.statusBar.setStyleSheet(f"color: {color.name()}; font-weight: bold;")
        self.statusBar.showMessage(message, 5000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PlagiarismChecker()
    window.show()
    sys.exit(app.exec())