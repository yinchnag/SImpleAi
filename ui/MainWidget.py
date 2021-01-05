
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ui.PaintBoard import PaintBoard
#  主窗口


class Mainwidget(QWidget):

    def __init__(self):
        super().__init__()

        #  数据初始化
        self.__init_data__()

        # 面板初始化
        self.__init_view__()

        pass

    def __init_view__(self):
        # 界面大小
        self.setFixedHeight(480)
        self.setFixedWidth(640)
        self.setWindowTitle('SimpleAI')
        self.label_name = QLabel('SIKI学院', self)
        self.label_name.setGeometry(500, 10, 120, 35)

        self.label_name = QLabel('Python人工智障', self)
        self.label_name.setGeometry(500, 40, 120, 35)

        self.label_name = QLabel('yinc', self)
        self.label_name.setGeometry(500, 100, 120, 35)

        self.setWindowIcon(QIcon('./Data/ui/.icon.png'))

        # 新建一个水平布局
        main_layout = QHBoxLayout(self)
        #  设置内边距为10像素
        main_layout.setSpacing(10)
        main_layout.addWidget(self.__paintBoard__)

        # 创建子布局
        sub_layout = QVBoxLayout(self)

        # 设置子布局分割方式
        splitter = QSplitter(self)
        sub_layout.addWidget(splitter)
        sub_layout.setContentsMargins(5, 5, 5, 5)
        # 子布局中添加按钮
        self.btn_start = QPushButton('识别')
        self.btn_start.setParent(self)
        #  添加点击事件
        self.btn_start.clicked.connect(self.on_btn_start_click)
        #  添加按钮到子垂直布局中
        self.btn_clear = QPushButton('清空')
        self.btn_clear.setParent(self)
        self.btn_clear.clicked.connect(self.on_btn_clear_click)

        self.btn_save = QPushButton('保存图形')
        self.btn_save.setParent(self)
        #  添加点击事件
        self.btn_save.clicked.connect(self.on_btn_save_clickk)
        sub_layout.addWidget(self.btn_save)
        sub_layout.addWidget(self.btn_clear)
        sub_layout.addWidget(self.btn_start)
        #  子布局加入到主布局中
        main_layout.addLayout(sub_layout)
        pass

    def __init_data__(self):
        self.__paintBoard__ = PaintBoard()
        pass

    def on_btn_start_click(self):
        print('start')
        pass

    def on_btn_clear_click(self):
        # print('clear')
        self.__paintBoard__.clear()
        pass

    def on_btn_save_clickk(self):
        # print('save')
        self.__paintBoard__.save_img()
        pass

    pass
