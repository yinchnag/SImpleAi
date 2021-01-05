from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

class PaintBoard(QWidget):

    def __init__(self):
        super().__init__()

        #  初始化画板
        self.__init_view__()
        #  初始化数据
        self.__init_data__()
        pass

    def __init_view__(self):
        self.setFixedSize(480, 460)

        # #  设置背景色
        # self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        # self.setStyleSheet('background-color:blue')

        pass

    def __init_data__(self):
        #  创建画图工具
        self.__painter__ = QPainter()
        #  调整画笔的粗细
        self.__thickness__ = 10
        # 画笔的颜色
        self.__pen_color__ = QColor('black')
        #  创建画板
        self.__board__ = QPixmap(QSize(480, 406))
        #  改变画板的填充色
        self.__board__.fill(Qt.white)

        self.__current_pos__ = QPoint(0, 0)
        self.__last_pos__ = QPoint(0, 0)
        # #  画一条线
        # self.__painter__.begin(self.__board__)
        #
        # #  设置笔的颜色以及粗细
        # self.__painter__.setPen(QPen(self.__pen_color__, self.__thickness__))
        #
        # #  划线
        # self.__painter__.drawLine(QPoint(0, 0), QPoint(100, 100))
        #
        # self.__painter__.end()
        self.__eraser__ = False
        pass

    def paintEvent(self, PaintEvent):
        #  绘图事件
        self.__painter__.begin(self)

        self.__painter__.drawPixmap(0, 0, self.__board__)

        self.__painter__.end()
        pass

    # 鼠标点击事件
    def mousePressEvent(self, MouseEvent):
        # print('mouse click', MouseEvent.pos())
        self.__current_pos__ = MouseEvent.pos()
        self.__last_pos__ = self.__current_pos__
        pass

    #  鼠标移动事件
    def mouseMoveEvent(self, MouseEvent):
        # print('mouse move', MouseEvent.pos())
        self.__current_pos__ = MouseEvent.pos()

        #  划线
        self.__painter__.begin(self.__board__)

        if  self.__eraser__ == True:
            self.__pen_color__ = QColor('white')
            pass

        self.__painter__.setPen(QPen(self.__pen_color__, self.__thickness__))
        self.__painter__.drawLine(self.__last_pos__, self.__current_pos__)
        self.__painter__.end()
        self.__last_pos__ = self.__current_pos__

        self.update()
        pass

    #  清空画板
    def clear(self):
        #  填充白色
        self.__board__.fill(Qt.white)

        #  更新画板
        self.update()

        pass
    #  保存图片
    def save_img(self):
        # 获得当前突变
        image = self.__board__.toImage()
        #  生成唯一ID
        uuid = QUuid()
        image.save('./Data/img/'+uuid.createUuid().toString()+'.png')
        pass

    pass
