# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def Kmeans(data, center, k=2):  # 选取距离最近的样本点
    label = []
    for i in range(data.shape[0]):
        temp = []
        for j in range(k):
            temp.append(np.sum(np.abs(data[i, :] - center[j, :]) ** 2))
        label.append(np.argsort(temp)[0])
    return np.array(label)


def new_center(data, label, k=2):  # 优化新的聚类中心
    center = np.zeros((k, data.shape[1]))
    for col in range(data.shape[1]):
        for i in range(k):
            center[i, col] = data[label == i, col].mean()
    return center


if __name__ == "__main__":
    j = 0
    np.random.seed(1)
    data = np.loadtxt('E:/data/4000_clean.txt')
    center = np.zeros((2, data.shape[1]))  # 初始化聚类中心
    for i in range(center.shape[1]):
        center[:, i] = np.random.rand(2) * (data[:, i].max() - data[:, i].min())
    label = Kmeans(data, center)
    c = new_center(data, label)  # 更新聚类中心
    label = Kmeans(data, c)
    if (c == center).all():
        pass
    else:
        center = c  # 不断更新聚类中心
    plt.xlim(0, 80)
    plt.ylim(0, 80)
    y_train = data[:, -1]  # 绘制散点图
    plt.scatter(data[y_train == 0, 0], data[y_train == 0, 1], color='yellow')
    plt.scatter(data[y_train == 1, 0], data[y_train == 1, 1], color='#d725de')
    plt.scatter(data[y_train == 2, 0], data[y_train == 2, 1], color='#2F4F4F')
    plt.scatter(center[:, 0], center[:, 1], color='r')
    plt.show()
