from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QComboBox,\
    QPushButton, QLCDNumber, QCheckBox, QLabel, QPlainTextEdit

import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Макдональдс 1')
        self.setGeometry(500, 300, 165, 360)

        self.check_box_1 = QCheckBox(self)
        self.check_box_1.move(15, 15)
        self.check_box_1.clicked.connect(self.convert)

        self.check_box_2 = QCheckBox(self)
        self.check_box_2.move(15, 45)
        self.check_box_2.clicked.connect(self.convert)

        self.check_box_3 = QCheckBox(self)
        self.check_box_3.move(15, 75)
        self.check_box_3.clicked.connect(self.convert)

        self.check_box_4 = QCheckBox(self)
        self.check_box_4.move(15, 105)
        self.check_box_4.clicked.connect(self.convert)

        self.text_1 = QLabel(self)
        self.text_1.move(45, 15)
        self.text_1.resize(75, 15)
        self.text_1.setText('Чизбургер')

        self.text_2 = QLabel(self)
        self.text_2.move(45, 45)
        self.text_2.resize(75, 15)
        self.text_2.setText('Гамбургер')

        self.text_3 = QLabel(self)
        self.text_3.move(45, 75)
        self.text_3.resize(75, 15)
        self.text_3.setText('Кола')

        self.text_4 = QLabel(self)
        self.text_4.move(45, 105)
        self.text_4.resize(75, 15)
        self.text_4.setText('Нагетсы')

        self.button = QPushButton(self)
        self.button.move(15, 135)
        self.button.resize(135, 30)
        self.button.setText('Заказать')
        self.button.clicked.connect(self.convert)

        self.result = QPlainTextEdit(self)
        self.result.move(15, 180)
        self.result.resize(135, 165)

        self.res = []

    def convert(self):
        sender = self.sender()
        if sender == self.check_box_1:
            if self.text_1.text() in self.res:
                del self.res[self.res.index(self.text_1.text())]
            else:
                self.res.append(self.text_1.text())
        elif sender == self.check_box_2:
            if self.text_2.text() in self.res:
                del self.res[self.res.index(self.text_2.text())]
            else:
                self.res.append(self.text_2.text())
        elif sender == self.check_box_3:
            if self.text_3.text() in self.res:
                del self.res[self.res.index(self.text_3.text())]
            else:
                self.res.append(self.text_3.text())
        elif sender == self.check_box_4:
            if self.text_4.text() in self.res:
                del self.res[self.res.index(self.text_4.text())]
            else:
                self.res.append(self.text_4.text())
        elif sender == self.button:
            self.result.setPlainText('')
            self.result.insertPlainText('Ваш заказ:\n')
            self.result.insertPlainText('\n')
            for e in self.res:
                self.result.insertPlainText(f'{e}\n')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    app.exec()
    sys.exit(app.exec())
