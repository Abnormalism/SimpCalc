from PySide6.QtWidgets import QApplication
from Classes.MainWindow import MainWindow

import sys

app = QApplication(sys.argv)
window = MainWindow(app)

window.show()
app.exec()

#TODO:
"""
4.) Proper formatting on huge Numbers
5.) User Settings e.g decimal places, round down/up
"""