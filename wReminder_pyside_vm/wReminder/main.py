import sys
from PySide6 import QtWidgets
from core.reminder_view_model import MainWindow


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
