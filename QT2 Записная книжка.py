from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QListWidget, QLabel
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Phone Numbers')
        self.setGeometry(400, 100, 450, 325)
        self.setFixedSize(450, 325)

        self.text_1 = QLabel(self)
        self.text_1.move(25, 25)
        self.text_1.resize(50, 25)
        self.text_1.setText('Name')

        self.name = QLineEdit(self)
        self.name.move(75, 25)
        self.name.resize(225, 25)

        self.text_2 = QLabel(self)
        self.text_2.move(25, 75)
        self.text_2.resize(50, 25)
        self.text_2.setText('Number')

        self.number = QLineEdit(self)
        self.number.move(75, 75)
        self.number.resize(225, 25)

        self.button = QPushButton(self)
        self.button.move(325, 25)
        self.button.resize(100, 75)
        self.button.setText('Draw')
        self.button.clicked.connect(self.convert)

        self.result = QListWidget(self)
        self.result.move(25, 125)
        self.result.resize(400, 175)

    def convert(self):
        self.result.addItem(f'{self.name.text()} - {self.number.text()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    app.exec()
    sys.exit(app.exec())
