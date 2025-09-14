import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6.uic import loadUi

class NimGame(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('task4.ui', self)
        self.setWindowTitle("Игра 'Псевдоним'")
        self.pushButton_start.clicked.connect(self.start_game)
        self.pushButton_take.clicked.connect(self.player_move)
        self.pushButton_take.setEnabled(False)
        self.spinBox.setMaximum(3)
        self.spinBox.setMinimum(1)
        self.stones = 0

    def start_game(self):
        try:
            n = int(self.lineEdit.text())
            if n <= 0:
                raise ValueError
            self.stones = n
            self.label_stones.setText(f"Осталось: {n}")
            self.label_status.setText("Ваш ход!")
            self.pushButton_take.setEnabled(True)
            self.lineEdit.setEnabled(False)
            self.pushButton_start.setEnabled(False)
            self.spinBox.setValue(1)
        except:
            self.label_status.setText("Введите корректное число камней!")

    def player_move(self):
        take = self.spinBox.value()
        if take > self.stones:
            self.label_status.setText("Нельзя взять больше, чем есть!")
            return
        self.stones -= take
        self.label_stones.setText(f"Осталось: {self.stones}")
        if self.stones == 0:
            self.label_status.setText("🎉 Вы выиграли!")
            self.end_game()
            return
        self.pushButton_take.setEnabled(False)
        self.label_status.setText("Ход компьютера...")
        QTimer.singleShot(1000, self.computer_move)

    def computer_move(self):
        if self.stones <= 3:
            take = self.stones
        else:
            take = (self.stones - 1) % 4
            if take == 0:
                take = 1
        self.stones -= take
        self.label_stones.setText(f"Осталось: {self.stones}")
        if self.stones == 0:
            self.label_status.setText("💀 Компьютер выиграл!")
            self.end_game()
            return
        self.pushButton_take.setEnabled(True)
        self.label_status.setText("Ваш ход!")

    def end_game(self):
        self.pushButton_take.setEnabled(False)
        self.lineEdit.setEnabled(True)
        self.pushButton_start.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NimGame()
    window.show()
    sys.exit(app.exec())