from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QComboBox, \
    QPushButton, QLCDNumber, QCheckBox, QLabel

import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Калькулятор')
        self.setGeometry(400, 100, 100, 100)
        self.setFixedSize(425, 625)

        self.result = QLineEdit(self)
        self.result.move(25, 25)
        self.result.resize(375, 75)

        self.button_7 = QPushButton(self)
        self.button_7.move(25, 125)
        self.button_7.resize(75, 75)
        self.button_7.setText('7')
        self.button_7.clicked.connect(self.count)

        self.button_8 = QPushButton(self)
        self.button_8.move(125, 125)
        self.button_8.resize(75, 75)
        self.button_8.setText('8')
        self.button_8.clicked.connect(self.count)

        self.button_9 = QPushButton(self)
        self.button_9.move(225, 125)
        self.button_9.resize(75, 75)
        self.button_9.setText('9')
        self.button_9.clicked.connect(self.count)

        self.res_1 = QPushButton(self)
        self.res_1.move(325, 125)
        self.res_1.resize(75, 75)
        self.res_1.setText('+')
        self.res_1.clicked.connect(self.count)

        self.button_4 = QPushButton(self)
        self.button_4.move(25, 225)
        self.button_4.resize(75, 75)
        self.button_4.setText('4')
        self.button_4.clicked.connect(self.count)

        self.button_5 = QPushButton(self)
        self.button_5.move(125, 225)
        self.button_5.resize(75, 75)
        self.button_5.setText('5')
        self.button_5.clicked.connect(self.count)

        self.button_6 = QPushButton(self)
        self.button_6.move(225, 225)
        self.button_6.resize(75, 75)
        self.button_6.setText('6')
        self.button_6.clicked.connect(self.count)

        self.res_2 = QPushButton(self)
        self.res_2.move(325, 225)
        self.res_2.resize(75, 75)
        self.res_2.setText('-')
        self.res_2.clicked.connect(self.count)

        self.button_1 = QPushButton(self)
        self.button_1.move(25, 325)
        self.button_1.resize(75, 75)
        self.button_1.setText('1')
        self.button_1.clicked.connect(self.count)

        self.button_2 = QPushButton(self)
        self.button_2.move(125, 325)
        self.button_2.resize(75, 75)
        self.button_2.setText('2')
        self.button_2.clicked.connect(self.count)

        self.button_3 = QPushButton(self)
        self.button_3.move(225, 325)
        self.button_3.resize(75, 75)
        self.button_3.setText('3')
        self.button_3.clicked.connect(self.count)

        self.res_3 = QPushButton(self)
        self.res_3.move(325, 325)
        self.res_3.resize(75, 75)
        self.res_3.setText('*')
        self.res_3.clicked.connect(self.count)

        self.button_C = QPushButton(self)
        self.button_C.move(25, 425)
        self.button_C.resize(75, 75)
        self.button_C.setText('C')
        self.button_C.clicked.connect(self.count)

        self.button_0 = QPushButton(self)
        self.button_0.move(125, 425)
        self.button_0.resize(75, 75)
        self.button_0.setText('0')
        self.button_0.clicked.connect(self.count)

        self.button_point = QPushButton(self)
        self.button_point.move(225, 425)
        self.button_point.resize(75, 75)
        self.button_point.setText('.')
        self.button_point.clicked.connect(self.count)

        self.res_4 = QPushButton(self)
        self.res_4.move(325, 425)
        self.res_4.resize(75, 75)
        self.res_4.setText('/')
        self.res_4.clicked.connect(self.count)

        self.button_res = QPushButton(self)
        self.button_res.move(25, 525)
        self.button_res.resize(375, 75)
        self.button_res.setText('=')
        self.button_res.clicked.connect(self.count)

    def count(self):
        try:
            a = self.sender()
            if a == self.button_7:
                self.result.setText(self.result.text() + '7')

            elif a == self.button_8:
                self.result.setText(self.result.text() + '8')

            elif a == self.button_9:
                self.result.setText(self.result.text() + '9')

            elif a == self.res_1:
                self.result.setText(self.result.text() + '+')

            elif a == self.button_4:
                self.result.setText(self.result.text() + '4')

            elif a == self.button_5:
                self.result.setText(self.result.text() + '5')

            elif a == self.button_6:
                self.result.setText(self.result.text() + '6')

            elif a == self.res_2:
                self.result.setText(self.result.text() + '-')

            elif a == self.button_1:
                self.result.setText(self.result.text() + '1')

            elif a == self.button_2:
                self.result.setText(self.result.text() + '2')

            elif a == self.button_3:
                self.result.setText(self.result.text() + '3')

            elif a == self.res_3:
                self.result.setText(self.result.text() + '*')

            elif a == self.button_C:
                self.result.setText('')

            elif a == self.button_0:
                self.result.setText(self.result.text() + '0')

            elif a == self.button_point:
                self.result.setText(self.result.text() + '.')

            elif a == self.res_4:
                self.result.setText(self.result.text() + '/')

            elif a == self.button_res:
                self.result.setText(str(eval(self.result.text())))

        except Exception:
            self.result.setText('Error')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    app.exec()
    sys.exit(app.exec())
