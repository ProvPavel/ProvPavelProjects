from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('График функции')
        self.setGeometry(0, 0, 1301, 1001)
        self.setFixedSize(1301, 1001)

        self.start = -500
        self.stop = 500

        self.text_1 = QLabel(self)
        self.text_1.move(1021, 10)
        self.text_1.resize(20, 20)
        self.text_1.setText('y=')

        self.FUNCTION = QLineEdit(self)
        self.FUNCTION.move(1041, 10)
        self.FUNCTION.resize(260, 20)

        self.text_2 = QLabel(self)
        self.text_2.move(1021, 40)
        self.text_2.resize(20, 20)
        self.text_2.setText('ZOOM=')

        self.ZOOM = QLineEdit(self)
        self.ZOOM.move(1041, 40)
        self.ZOOM.resize(260, 20)
        self.ZOOM.setText('1')

        self.button = QPushButton(self)
        self.button.move(1021, 70)
        self.button.resize(270, 20)
        self.button.setText('DRAW')
        self.button.clicked.connect(self.paintEvent)

    def paintEvent(self):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(Qt.black)
        qp.drawLine(10, 511, 1011, 511)
        qp.drawLine(511, 10, 511, 1011)
        qp.setPen(Qt.red)
        x = self.start / float(self.ZOOM.text())
        while x <= self.stop / float(self.ZOOM.text()):
            try:
                y = self.f(str(x))
                qp.drawPoint(x + 510, y + 510)
            except Exception:
                pass
            finally:
                x += 1 / float(self.ZOOM.text())
        qp.end()

    def f(self, x):
        r = self.FUNCTION.text()
        t = eval(r.replace('x', f'({x})'))
        if t >= 0:
            return int(t + 0.5)
        return int(t - 0.5)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    app.exec()
    sys.exit(app.exec())
