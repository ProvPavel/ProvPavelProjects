from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QComboBox,\
    QPushButton, QLCDNumber, QCheckBox, QLabel

import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Прятки для виджетов')
        self.setGeometry(500, 400, 225, 135)

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
        self.text_1.setText('Павел')

        self.text_2 = QLabel(self)
        self.text_2.move(45, 45)
        self.text_2.resize(75, 15)
        self.text_2.setText('Андрей')

        self.text_3 = QLabel(self)
        self.text_3.move(45, 75)
        self.text_3.resize(75, 15)
        self.text_3.setText('Илья')

        self.text_4 = QLabel(self)
        self.text_4.move(45, 105)
        self.text_4.resize(75, 15)
        self.text_4.setText('Арсений')

        self.output_value_1 = QLineEdit(self)
        self.output_value_1.move(135, 15)
        self.output_value_1.resize(75, 15)
        self.output_value_1.setText('Пришёл')
        self.output_value_1.hide()

        self.output_value_2 = QLineEdit(self)
        self.output_value_2.move(135, 45)
        self.output_value_2.resize(75, 15)
        self.output_value_2.setText('Пришёл')
        self.output_value_2.hide()

        self.output_value_3 = QLineEdit(self)
        self.output_value_3.move(135, 75)
        self.output_value_3.resize(75, 15)
        self.output_value_3.setText('Пришёл')
        self.output_value_3.hide()

        self.output_value_4 = QLineEdit(self)
        self.output_value_4.move(135, 105)
        self.output_value_4.resize(75, 15)
        self.output_value_4.setText('Пришёл')
        self.output_value_4.hide()

    def convert(self):
        a = self.sender()
        if a == self.check_box_1:
            if self.output_value_1.isHidden():
                self.output_value_1.show()
            else:
                self.output_value_1.hide()

        if a == self.check_box_2:
            if self.output_value_2.isHidden():
                self.output_value_2.show()
            else:
                self.output_value_2.hide()

        if a == self.check_box_3:
            if self.output_value_3.isHidden():
                self.output_value_3.show()
            else:
                self.output_value_3.hide()

        if a == self.check_box_4:
            if self.output_value_4.isHidden():
                self.output_value_4.show()
            else:
                self.output_value_4.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    app.exec()
    sys.exit(app.exec())
