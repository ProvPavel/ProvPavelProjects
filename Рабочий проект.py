from random import choice
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QApplication
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Случайная строка')
        self.setGeometry(300, 300, 270, 50)

        self.input_value = QLineEdit(self)
        self.input_value.move(10, 10)
        self.input_value.resize(100, 30)

        self.button = QPushButton(self)
        self.button.setText('->')
        self.button.move(120, 10)
        self.button.resize(30, 30)
        self.button.clicked.connect(self.convert)

        self.output_value = QLineEdit(self)
        self.output_value.move(160, 10)
        self.output_value.resize(100, 30)

    def convert(self):
        if self.button.text() == '->':
            self.button.setText('<-')
            self.output_value.setText(self.input_value.text())
            self.input_value.setText('')
        else:
            self.button.setText('->')
            self.input_value.setText(self.output_value.text())
            self.output_value.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    app.exec()
    sys.exit(app.exec())

f = open('lines.txt')
data = f.readlines()
if data:
    print(choice(data))
f.close()

