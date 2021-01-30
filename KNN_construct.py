# -*- coding: UTF-8 -*-
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def KNN(x_train, y_train, x_predict):  # 调用预测函数对样本点进行预测
    return [_predict(x_train, y_train, x) for x in x_predict]


def _predict(x_train, y_train, x, k=7):
    distances = [distance(item, x) for item in x_train]  # 得出距离关系
    return Counter(y_train[np.argsort(distances)[:k]]).most_common(1)[0][0]  # 对距离进行从小到大排序，选出最近的距离点


def distance(a, b, p=2):  # 距离计算公式
    return np.sum(np.abs(a - b) ** p) ** (1 / p)


if __name__ == "__main__":
    distances, list1 = [], []
    count_pos, count_neg, count_zero = 0, 0, 0
    x_train = pd.read_excel('./2000_pos_neg.xlsx', header=None).values[:, :2]  # 读取2列
    y_train = pd.read_excel('./2000_pos_neg.xlsx', header=None).values[:, -1]  # 读取情感标记列
    x = pd.read_excel('./test_pos.xlsx', header=None).values[:, :2]
    list1 = KNN(x_train, y_train, x)
    for i in range(len(list1)):  # 统计情感标记值
        if list1[i] == 2:
            count_pos += 1
        elif list1[i] == 1:
            count_neg += 1
        elif list1[i] == 0:
            count_zero += 1
    print(KNN(x_train, y_train, x))
    print(count_pos, count_neg, count_zero)
