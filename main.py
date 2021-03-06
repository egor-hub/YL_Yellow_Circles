import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

import UI


class MainWidget(QMainWindow, UI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Git и случайные окружности')

        self.pushButton.clicked.connect(self.run)

        self.do_paint = False

    def draw_circle(self, qp):
        x = randint(50, 400)
        y = randint(100, 300)
        diameter = randint(50, 200)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        qp.setBrush(color)
        qp.drawEllipse(x - diameter // 2, y - diameter // 2, diameter, diameter)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            for _ in range(randint(2, 5)):
                self.draw_circle(qp)
            qp.end()

    def run(self):
        self.do_paint = True
        self.repaint()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


app = QApplication(sys.argv)
ex = MainWidget()
ex.show()
sys.excepthook = except_hook
sys.exit(app.exec_())
