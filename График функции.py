import sys
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPainter
from PyQt6.QtGui import QColor


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('График функции')
        self.setGeometry(100, 50, 1081, 921)
        self.setFixedSize(1081, 921)

        self.start = -450
        self.stop = 450
        self.flag = False
        self.points = []
        self.colors = [[255, 0, 255], [128, 0, 128], [255, 0, 0], [128, 0, 0],
                       [128, 128, 128], [128, 128, 0], [0, 255, 0], [0, 128, 0],
                       [0, 255, 255], [0, 128, 128], [0, 0, 255], [0, 0, 128]]

        self.text_1 = QLabel(self)
        self.text_1.move(931, 10)
        self.text_1.resize(40, 20)
        self.text_1.setText('f1(x) =')

        self.function_1 = QLineEdit(self)
        self.function_1.move(971, 10)
        self.function_1.resize(100, 20)

        self.text_2 = QLabel(self)
        self.text_2.move(931, 40)
        self.text_2.resize(40, 20)
        self.text_2.setText('f2(x) =')

        self.function_2 = QLineEdit(self)
        self.function_2.move(971, 40)
        self.function_2.resize(100, 20)

        self.text_zoom = QLabel(self)
        self.text_zoom.move(931, 70)
        self.text_zoom.resize(50, 20)
        self.text_zoom.setText('ZOOM =')

        self.zoom = QLineEdit(self)
        self.zoom.move(981, 70)
        self.zoom.resize(90, 20)
        self.zoom.setText('100')

        self.button = QPushButton(self)
        self.button.move(931, 100)
        self.button.resize(140, 50)
        self.button.setText('DRAW')
        self.button.clicked.connect(self.help)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter(self)
            qp.begin(self)
            qp.setPen(QColor(0, 0, 0))
            qp.drawLine(10, 461, 911, 461)
            qp.drawLine(461, 10, 461, 911)
            self.drawing(qp, self.function_1)
            self.drawing(qp, self.function_2)
            qp.end()
            self.flag = False

    def help(self):
        self.flag = True
        self.update()

    def drawing(self, qp, name_of_function):
        try:
            qp.setPen(QColor(255, 0, 0))
            x = self.start / float(self.zoom.text())
            while x <= self.stop / float(self.zoom.text()):
                try:
                    y = self.f(str(x), name_of_function)
                    a = self.ball(x * float(self.zoom.text()))
                    b = self.ball(y * float(self.zoom.text()))
                    if self.points:
                        qp.drawLine(self.points[-1][0] + 461, 461 - self.points[-1][1],
                                    a + 461, 461 - b)
                        self.points.append([a, b])
                    else:
                        self.points.append([a, b])
                except Exception:
                    self.points = []
                finally:
                    x += 1 / float(self.zoom.text())
            self.points = []
        except Exception:
            pass

    def f(self, x, name_of_function):
        return eval(name_of_function.text().replace('x', f'({x})'))

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
