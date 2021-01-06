from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

# 0 一
# 1 丁
# 2 七
# 3 万
# 4 丈
# 5 三
# 6 上
# 7 下
# 8 不
# 9 与

def get_chinese_data():

    x = []
    y = []
    # 便利文件夹种所有文件
    for file_paths, dir_names, file_names in os.walk('../data/chinese_char'):
        # 拿到文件相对路径
        for  file_name in file_names:
            # print(file_paths+'/'+file_name)
            # 获得每张文件的数据
            image_data = get_image_data(file_paths+'/'+file_name)
            x.append(image_data.reshape(-1))
            if file_paths.find('00000') != 1:
                y.append(0)
            elif file_paths.find('00001') != 1:
                y.append(1)
            elif file_paths.find('00002') != 1:
                y.append(2)
            elif file_paths.find('00003') != 1:
                y.append(3)
            elif file_paths.find('00004') != 1:
                y.append(4)
            elif file_paths.find('00005') != 1:
                y.append(5)
            elif file_paths.find('00006') != 1:
                y.append(6)
            elif file_paths.find('00007') != 1:
                y.append(7)
            elif file_paths.find('00008') != 1:
                y.append(8)
            elif file_paths.find('00009') != 1:
                y.append(9)
            pass
        print(x)
        print(y)
        pass

    pass


def get_image_data(path):
    img = Image.open(path).convert('L')
    # 重新设置图形大小
    img = img.resize((400, 400), Image.ANTIALIAS)
    # 二维数组化
    img_data = np.zeros((400, 400), dtype=np.int)
    for i in range(400):
        for j in range(400):
            img_data[i][j] = 255 - img.getpixel((j, i))
            pass
        pass
    # print(img_data)
    # plt.imshow(img_data, cmap=plt.cm.gray_r)
    # plt.show()
    # print(img_data.reshape(-1)) # 数据一维化
    return img_data
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