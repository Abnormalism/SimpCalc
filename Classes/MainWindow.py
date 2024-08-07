from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from .Display import Display
from .UserAction import UserAction

class MainWindow(QMainWindow):
    def __init__(self, app=None):
        super().__init__()

        self.setWindowTitle("SimpCalc")
        self.WIDTH, self.HEIGHT = 400, 450
        self.setFixedSize(self.WIDTH, self.HEIGHT)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        vLayout = QVBoxLayout()
        central_widget.setLayout(vLayout)

        self.userAction = UserAction()
        vLayout.addWidget(self.userAction)