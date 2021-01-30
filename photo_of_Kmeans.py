# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def Kmeans(data, k, center):  # 选取距离最近的样本点
    label = []
    for i in range(data.shape[0]):
        temp = []
        for j in range(k):
            temp.append(np.sum(np.abs(data[i, :] - center[j, :]) ** 2))
        label.append(np.argsort(temp)[0])
    return np.array(label)


if __name__ == "__main__":
    data = np.loadtxt('E:/data/8000_clean_two.txt')
    k = 2
    center = np.zeros((k, data.shape[1]))
    center[0][0], center[0][1], center[1][0], center[1][1] = 6.5, 1.2, 2.3, 4.4
    label = Kmeans(data, k, center)
    font1 = {'family': 'Times New Roman',
             'size': 10}
    plt.xlabel('Positive', font1)  # 绘制图形
    plt.ylabel('Negative', font1)
    plt.scatter(data[label == 0, 0], data[label == 0, 1], color='gray', marker='.')
    plt.scatter(data[label == 1, 0], data[label == 1, 1], color='#A9A9A9', marker='.')
    plt.plot([1, 7, 18.948, 73.555], [0 - 1.6, 5.96, 21.02448, 89.8193], color='#708090')
    plt.show()
