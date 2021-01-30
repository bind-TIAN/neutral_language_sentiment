# -*- coding: UTF-8 -*-
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.model_selection import train_test_split


def accuracy_score(y, y_predict):
    count1, count2 = 0, 0
    assert y.shape[0] == y_predict.shape[0]  # y与y_predict的长度需相等
    for i in range(2000):
        if y[i] == y_predict[i] and y[i] == 1:
            count1 += 1
        elif y[i] == y_predict[i] and y[i] == 2:
            count2 += 1
    return count1, count2


# return sum(y == y_predict) / len(y)


def KNN(x_train, y_train, x_predict, k, p):
    return np.array([_predict(x_train, y_train, x, k, p) for x in x_predict])


def _predict(x_train, y_train, x, k, p):
    distances = [distance(item, x, p=p) for item in x_train]
    return Counter(y_train[np.argsort(distances)[:k]]).most_common(1)[0][0]


def distance(a, b, p):
    return np.sum(np.abs(a - b) ** p) ** (1 / p)


if __name__ == "__main__":
    # k=13,p=5
    shuzu, shuzu2 = [], []
    distances, list1 = [], []
    index = 0
    max, best_k, best_p = 0, 0, 0
    count_pos, count_neg, count_zero, base_score, base_k, base_p, jishu = 0, 0, 0, 0, 0, 0, 0
    connect = pd.read_excel('E:/data/KNN_10000.xlsx', header=None).values[:10000, :2]
    table = pd.read_excel('E:/data/KNN_10000.xlsx', header=None).values[:10000, -1]
    x_train, x_test, y_train, y_test = train_test_split(connect, table, test_size=0.2, random_state=1)
    y_predict = KNN(x_train, y_train, x_test, k=13, p=5)
    count1, count2 = accuracy_score(y_test, y_predict)
    print(count1, count2)
