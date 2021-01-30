# -*- coding: UTF-8 -*-
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.model_selection import train_test_split


def accuracy_score(y, y_predict):
    assert y.shape[0] == y_predict.shape[0]  # 断言判定
    return sum(y == y_predict) / len(y)


def KNN(x_train, y_train, x_predict, k, p):  # 调用预测函数进行预测
    return np.array([_predict(x_train, y_train, x, k, p) for x in x_predict])


def _predict(x_train, y_train, x, k, p):  # 调用距离计算函数进行距离计算
    distances = [distance(item, x, p=p) for item in x_train]
    return Counter(y_train[np.argsort(distances)[:k]]).most_common(1)[0][0]


def distance(a, b, p):  # 距离的计算
    return np.sum(np.abs(a - b) ** p) ** (1 / p)


if __name__ == "__main__":
    # k=13,p=5
    shuzu, shuzu2 = [], []
    distances, list1 = [], []
    index = 0
    max, best_k, best_p = 0, 0, 0
    count_pos, count_neg, count_zero, base_score, base_k, base_p, jishu = 0, 0, 0, 0, 0, 0, 0
    connect = pd.read_excel('E:/data/KNN_pos.xlsx', header=None).values[:1000, :2]  # 读取文件数据
    table = pd.read_excel('E:/data/KNN_pos.xlsx', header=None).values[:1000, -1]
    x_train, x_test, y_train, y_test = train_test_split(connect, table, test_size=0.2, random_state=1)
    for k in range(1, 21):
        for p in range(1, 11):
            index += 1
            print(index)
            y_predict = KNN(x_train, y_train, x_test, k=k, p=p)
            count = accuracy_score(y_test, y_predict)
            shuzu.append(count)
            if count > max:
                max = count
                best_k = k
                best_p = p
    print(best_k, best_p)  # 选出最好的k和p值
    list4 = [i for i in range(0, 200, 1)]
    plt.plot(list4, shuzu, '-..', color='gray', linewidth=1, label='SVM-Positive')
    plt.plot(list4, shuzu2, '--.', color='green', linewidth=1, label='SVM-Negative')
    plt.legend()
    plt.show()
