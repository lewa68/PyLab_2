import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QDateTime
from PyQt6.uic import loadUi

class DiaryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('task2.ui', self)
        self.setWindowTitle("Ежедневник")
        self.pushButton.clicked.connect(self.add_event)

    def add_event(self):
        event_name = self.lineEdit.text().strip()
        if not event_name:
            return
        date = self.calendarWidget.selectedDate()  # ← ТУТ ОНО БУДЕТ РАБОТАТЬ!
        time = self.timeEdit.time()
        datetime_obj = QDateTime(date, time)
        formatted = f"{datetime_obj.toString('dd.MM.yyyy HH:mm')} — {event_name}"
        self.listWidget.addItem(formatted)
        self.listWidget.sortItems()
        self.lineEdit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DiaryApp()
    window.show()
    sys.exit(app.exec())