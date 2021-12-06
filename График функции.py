import sys
from math import log, cos, sin, tan, sqrt, pi, e
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPainter, QMouseEvent
from PyQt6.QtGui import QColor


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('График функции')
        self.setGeometry(0, 0, 1081, 921)
        self.setFixedSize(1081, 921)

        self.new_zoom = QLineEdit(self)
        self.new_zoom.move(981, 70)
        self.new_zoom.resize(90, 20)
        self.new_zoom.setText('-450;450')

        self.coords = QLabel(self)
        self.coords.setText('Координаты: None, None')
        self.coords.move(10, 10)
        self.coords.resize(150, 20)
        self.setMouseTracking(True)

        self.start = int(self.new_zoom.text().split(';')[0])
        self.stop = int(self.new_zoom.text().split(';')[1])

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

        self.button_draw = QPushButton(self)
        self.button_draw.move(931, 100)
        self.button_draw.resize(140, 50)
        self.button_draw.setText('DRAW')
        self.button_draw.clicked.connect(self.help)

    def paintEvent(self, event):
        if self.flag:
            self.start = int(self.new_zoom.text().split(';')[0])
            self.stop = int(self.new_zoom.text().split(';')[1])
            qp = QPainter(self)
            qp.begin(self)
            qp.setPen(QColor(0, 0, 0))
            qp.drawLine(10, 461, 911, 461)
            qp.drawLine(461, 10, 461, 911)
            self.drawing(qp, self.function_1.text())
            self.drawing(qp, self.function_2.text())
            qp.end()
            self.flag = False

    def help(self):
        self.flag = True
        self.update()

    def mouseMoveEvent(self, event: QMouseEvent):
        cx = int(str(event.pos())[:-1:].split("(")[1].split(",")[0])
        cy = int(str(event.pos())[:-1:].split("(")[1].split(",")[1])
        self.coords.setText(f'Координаты: '
                            f'{round((cx - 461) * ((self.stop - self.start) / 900), 3)};'
                            f'{round((461 - cy) * ((self.stop - self.start) / 900), 3)}')

    def drawing(self, qp, name_of_function):
        try:
            qp.setPen(QColor(255, 0, 0))
            x = self.start
            while x <= self.stop:
                try:
                    y = self.f(x, name_of_function)
                    a = round(x * float(900 / (self.stop - self.start)))
                    b = round(y * float(900 / (self.stop - self.start)))
                    if self.points:
                        qp.drawLine(self.points[-1][0] + 461,  # (self.stop - self.start) // 2 + 10
                                    461 - self.points[-1][1],
                                    a + 461,
                                    461 - b)
                        self.points.append([a, b])
                    else:
                        self.points.append([a, b])
                except Exception:
                    self.points = []
                finally:
                    x += (self.stop - self.start) / 900
            self.points = []
        except Exception:
            pass

    def f(self, x, name_of_function):
        return eval(name_of_function.replace('x', f'({str(x)})'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    app.exec()
    sys.exit(app.exec())
