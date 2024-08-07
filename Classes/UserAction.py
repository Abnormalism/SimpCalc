from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QVBoxLayout
from .Display import Display

class UserAction(QWidget):
    def __init__(self):
        super().__init__()

        #Attributes
        self.inputs = []

        vLayout = QVBoxLayout()
        self.setLayout(vLayout)

        # Display Class
        self.display = Display()
        vLayout.addWidget(self.display)

        #Layouts
        gridLayout = QGridLayout()
        vLayout.addLayout(gridLayout)

        gridLayout.setSpacing(10)
        userAction = [
            ('(', 0, 1),(')', 0, 2), ('del', 0, 3), ('c', 0, 4),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('%', 1, 3), ('x²', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('/', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3), ('-', 3, 4),
            ('0', 4, 0, 1, 2), ('.', 4, 2), ('=', 4, 3, 1, 2)
        ]

        for text, row, col, *span in userAction:
            pushButton = QPushButton(text)
            pushButton.setFixedHeight(50)
            pushButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            pushButton.pressed.connect(lambda t=text: self.userInput(t))

            if span:
                gridLayout.addWidget(pushButton, row, col, *span)
            else:
                gridLayout.addWidget(pushButton, row, col)

    def userInput(self, text):
        if text not in ['c', '=', 'del']:
            self.inputs.append(text)
            display = ''.join(self.inputs)
            self.display.displayInput(display)

        elif text == 'c':
            self.display.lineEdit.clear()
            self.inputs = []

        elif text == 'del':
            if len(self.inputs) > 0:
                self.inputs.pop()

            display = ''.join(self.inputs)
            self.display.displayInput(display)

        elif text == '=':
            display = ''.join(self.inputs)

            try:
                result = str(eval(display))
                self.inputs = [result]
                self.display.displayInput(result)
            except Exception as e:
                print(f"Error evaluating expression: {e}")
                self.display.displayInput("Error")

