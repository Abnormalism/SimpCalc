from PySide6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QWidget, QSizePolicy
from PySide6.QtCore import Qt

class Display(QWidget):
    def __init__(self):
        super().__init__()

        # lineEdit Attributes
        self.lineEdit = QLineEdit()
        self.lineEdit.setFixedHeight(70)
        self.lineEdit.setAlignment(Qt.AlignRight)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        #Layouts
        vLayout = QVBoxLayout()
        self.setLayout(vLayout)
        vLayout.addWidget(self.lineEdit)

    def displayInput(self, input):
        self.lineEdit.setText(input)
