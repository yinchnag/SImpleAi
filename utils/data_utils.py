from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

def get_chinese_data():

    for file_paths, dir_names, file_names in os.walk('../data/chinese_char'):
        print(file_names)
        pass

    pass


def get_image_data():
    img = Image.open('../data/chinese_char/train/00000/702.png').convert('L')
    # 重新设置图形大小
    img = img.resize((400, 400), Image.ANTIALIAS)
    # 二维数组化
    img_data = np.zeros((400, 400), dtype=np.int)
    for i in range(400):
        for j in range(400):
            img_data[i][j] = 255 - img.getpixel((i, j))
            pass
        pass
    print(img_data)
    # plt.imshow(img_data, cmap=plt.cm.gray_r)
    # plt.show()
    # print(img_data.reshape(-1)) # 数据一维化
    pass

def get_data_x_y_one():
    img = Image.open('../data/chinese_char/train/00000/702.png').convert('L')
    # 重新设置图形大小
    img = img.resize((400, 80), Image.ANTIALIAS)
    # 二维数组化
    img_data = np.zeros((400, 400), dtype=np.int)
    for i in range(400):
        if i < 160:
            for j in range(400):
                img_data[i][j] = 0
        elif i >= 160 and i < 240:
            for j in range(400):
                img_data[i][j] = 255 - img.getpixel((j, i - 160))
                pass
            pass
        else:
            for j in range(400):
                img_data[i][j] = 0
                pass
            pass
        pass

    print(img_data)
    plt.imshow(img_data, cmap=plt.cm.gray_r)
    plt.show()
    # print(img_data.reshape(-1)) # 数据一维化
    pass

get_chinese_data()