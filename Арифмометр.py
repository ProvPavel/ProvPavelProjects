from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QComboBox,\
    QPushButton, QLCDNumber, QCheckBox, QLabel

import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Прятки для виджетов')
        self.setGeometry(300, 400, 625, 75)

        self.input_value_1 = QLineEdit(self)
        self.input_value_1.move(25, 25)
        self.input_value_1.resize(75, 25)

        self.plus = QPushButton(self)
        self.plus.move(125, 25)
        self.plus.resize(75, 25)
        self.plus.setText('+')
        self.plus.clicked.connect(self.p)

        self.minus = QPushButton(self)
        self.minus.move(225, 25)
        self.minus.resize(75, 25)
        self.minus.setText('-')
        self.minus.clicked.connect(self.m)

        self.star = QPushButton(self)
        self.star.move(325, 25)
        self.star.resize(75, 25)
        self.star.setText('*')
        self.star.clicked.connect(self.s)

        self.input_value_2 = QLineEdit(self)
        self.input_value_2.move(425, 25)
        self.input_value_2.resize(75, 25)

        self.output_value = QLineEdit(self)
        self.output_value.move(525, 25)
        self.output_value.resize(75, 25)

    def p(self):
        self.output_value.setText(str(float(self.input_value_1.text()) +
                                  float(self.input_value_2.text())))

    def m(self):
        self.output_value.setText(str(float(self.input_value_1.text()) -
                                  float(self.input_value_2.text())))

    def s(self):
        self.output_value.setText(str(float(self.input_value_1.text()) *
                                  float(self.input_value_2.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    app.exec()
    sys.exit(app.exec())
