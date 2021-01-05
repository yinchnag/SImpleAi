# file name 'main.py'
from PyQt5.QtWidgets import QApplication

from ui.MainWidget import Mainwidget

import sys


def main():

    #  创建QT
    app = QApplication(sys.argv)
    main_widget = Mainwidget()
    main_widget.show()
    exit(app.exec_())
    pass


if __name__ == '__main__':
    main()

    pass
