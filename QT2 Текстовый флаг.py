from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, \
    QButtonGroup, QRadioButton, QPushButton
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Text Flag')
        self.setGeometry(400, 100, 100, 100)
        self.setFixedSize(425, 325)

        self.result = QLineEdit(self)
        self.result.move(25, 25)
        self.result.resize(375, 75)
        self.result.setDisabled(True)
        self.result.setText('Flag:')

        self.button = QPushButton(self)
        self.button.move(25, 225)
        self.button.resize(375, 75)
        self.button.setText('Draw')
        self.button.clicked.connect(self.convert)

        self.color_11 = QRadioButton(self)
        self.color_11.move(25, 125)
        self.color_11.setText('Red')

        self.color_12 = QRadioButton(self)
        self.color_12.move(25, 150)
        self.color_12.setText('Green')

        self.color_13 = QRadioButton(self)
        self.color_13.move(25, 175)
        self.color_13.setText('Blue')

        self.color_21 = QRadioButton(self)
        self.color_21.move(125, 125)
        self.color_21.setText('Red')

        self.color_22 = QRadioButton(self)
        self.color_22.move(125, 150)
        self.color_22.setText('Green')

        self.color_23 = QRadioButton(self)
        self.color_23.move(125, 175)
        self.color_23.setText('Blue')

        self.color_31 = QRadioButton(self)
        self.color_31.move(225, 125)
        self.color_31.setText('Red')

        self.color_32 = QRadioButton(self)
        self.color_32.move(225, 150)
        self.color_32.setText('Green')

        self.color_33 = QRadioButton(self)
        self.color_33.move(225, 175)
        self.color_33.setText('Blue')

        self.group_1 = QButtonGroup(self)
        self.group_1.addButton(self.color_11)
        self.group_1.addButton(self.color_12)
        self.group_1.addButton(self.color_13)

        self.group_2 = QButtonGroup(self)
        self.group_2.addButton(self.color_21)
        self.group_2.addButton(self.color_22)
        self.group_2.addButton(self.color_23)

        self.group_3 = QButtonGroup(self)
        self.group_3.addButton(self.color_31)
        self.group_3.addButton(self.color_32)
        self.group_3.addButton(self.color_33)

    def convert(self):
        if self.color_11.isChecked():
            a = self.color_11.text()
        elif self.color_12.isChecked():
            a = self.color_12.text()
        elif self.color_13.isChecked():
            a = self.color_13.text()
        else:
            a = 'None'
        if self.color_21.isChecked():
            b = self.color_21.text()
        elif self.color_22.isChecked():
            b = self.color_22.text()
        elif self.color_23.isChecked():
            b = self.color_23.text()
        else:
            b = 'None'
        if self.color_31.isChecked():
            c = self.color_31.text()
        elif self.color_32.isChecked():
            c = self.color_32.text()
        elif self.color_33.isChecked():
            c = self.color_33.text()
        else:
            c = 'None'
        self.result.setText(f'Flag: {a}, {b} and {c}.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    app.exec()
    sys.exit(app.exec())
