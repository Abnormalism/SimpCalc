from PySide6.QtWidgets import QApplication
from Classes.MainWindow import MainWindow

import sys

app = QApplication(sys.argv)
window = MainWindow(app)

window.show()
app.exec()

#TODO:
"""
1.) Modulo Feature
2.) Power Feature
3.) Styles
4.) Proper formatting on huge Numbers
5.) User Settings e.g decimal places, round down/up
"""