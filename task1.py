import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QRadioButton
from PyQt6.uic import loadUi

class FlagApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('task1.ui', self)  # Загружаем интерфейс из task1.ui
        self.setWindowTitle("Текстовый флаг")
        self.setFixedSize(400, 600)  # Нельзя изменять размер окна

        self.pushButton.clicked.connect(self.draw_flag)

    def draw_flag(self):
        colors = []
        # Получаем выбранные цвета для каждой полосы
        for i, group in enumerate([self.groupBox, self.groupBox_2, self.groupBox_3]):
            for rb in group.findChildren(QRadioButton):
                if rb.isChecked():
                    colors.append(rb.text())
                    break
            else:
                colors.append("Не выбрано")

        result = ", ".join(colors)
        self.label.setText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FlagApp()
    window.show()
    sys.exit(app.exec())