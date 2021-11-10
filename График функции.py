from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel
from PyQt6.QtGui import QPainter, QColor, QPen
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('График функции')
        self.setGeometry(0, 0, 1301, 1001)
        self.setFixedSize(1241, 921)

        self.start = -450
        self.stop = 450
        self.flag = False
        self.points = []

        self.text_1 = QLabel(self)
        self.text_1.move(931, 10)
        self.text_1.resize(20, 20)
        self.text_1.setText('y =')

        self.FUNCTION = QLineEdit(self)
        self.FUNCTION.move(951, 10)
        self.FUNCTION.resize(120, 20)
        self.FUNCTION.setText('x')

        self.text_2 = QLabel(self)
        self.text_2.move(931, 40)
        self.text_2.resize(50, 20)
        self.text_2.setText('ZOOM =')

        self.ZOOM = QLineEdit(self)
        self.ZOOM.move(981, 40)
        self.ZOOM.resize(90, 20)
        self.ZOOM.setText('1')

        self.button = QPushButton(self)
        self.button.move(931, 70)
        self.button.resize(140, 20)
        self.button.setText('DRAW')
        self.button.clicked.connect(self.help)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter(self)
            qp.begin(self)
            self.drawing(qp)
            qp.end()
            self.flag = False
            self.points = []

    def help(self):
        self.flag = True
        self.update()

    def drawing(self, qp):
        qp.setPen(QColor(0, 0, 0))
        qp.drawLine(10, 461, 911, 461)
        qp.drawLine(461, 10, 461, 911)
        qp.setPen(QColor(255, 0, 0))
        x = self.start / float(self.ZOOM.text())
        while x <= self.stop / float(self.ZOOM.text()):
            try:
                y = self.f(str(x))
                a = self.ball(x * float(self.ZOOM.text()))
                b = self.ball(y * float(self.ZOOM.text()))
                if self.points:
                    qp.drawLine(self.points[-1][0] * int(self.ZOOM.text()) + 461,
                                461 - self.points[-1][1] * int(self.ZOOM.text()),
                                a + 461, 461 - b)
                    self.points.append([a, b])
                else:
                    self.points.append([a, b])
            except Exception:
                pass
            finally:
                x += 1 / float(self.ZOOM.text())

    def f(self, x):
        return eval(self.FUNCTION.text().replace('x', f'({x})'))

    def ball(self, a):
        if a >= 0:
            return int(a + 0.5)
        return int(a - 0.5)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    app.exec()
    sys.exit(app.exec())
