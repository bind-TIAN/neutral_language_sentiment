# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
from collections import Counter


def predict(paraone, paratwo):
    boss, temp, count_no = 0, 0, 0
    if paraone <= len(feture_dict[1][0]) and paratwo <= len(feture_dict[1][0]):
        b = label_dict[1] * feture_dict[1][0][paraone] * feture_dict[1][1][paratwo]  # 采用概率统计相关公式进行预测
        c = label_dict[2] * feture_dict[2][0][paraone] * feture_dict[2][1][paratwo]
        boss = max(b, c)
        exp2 = lambda y: y if boss == b else 0
        exp3 = lambda z: z if boss == c else 0  # lambda函数判定
        print(exp2(-1), exp3(1))
    else:
        count_no += 1
        print(count_no)


def calc(X):
    res, features = {}, {}
    for i in range(x_train.shape[1]):
        features[i] = np.unique(x_train[:, i])  # x_train
    for i in range(X.shape[1]):
        feature_counter = Counter(X[:, i])
        temp = {}
        for item in features[i]:
            count = feature_counter[item] if item in feature_counter else 0
            temp[item] = count / len(X)  # 统计比例
        res[i] = temp
    return res


if __name__ == "__main__":
    list1 = []
    x_train = pd.read_excel('E:/data/train_8000_clean.xls', header=None).values[:, :2]
    y_train = pd.read_excel('E:/data/train_8000_clean.xls', header=None).values[:, -1]  # 读取一系列文件
    # x_train = pd.read_excel('E:/data/train_6000_clean.xlsx', header=None).values[:, :2]
    # y_train = pd.read_excel('E:/data/train_6000_clean.xlsx', header=None).values[:, -1]
    # x_train = pd.read_excel('E:/data/train_4000_clean.xlsx', header=None).values[:, :2]
    # y_train = pd.read_excel('E:/data/train_4000_clean.xlsx', header=None).values[:, -1]
    # x_train = pd.read_excel('E:/data/train_2000_clean.xlsx', header=None).values[:, :2]
    # y_train = pd.read_excel('E:/data/train_2000_clean.xlsx', header=None).values[:, -1]
    label_dict, feture_dict = {}, {}  # 初始化字典
    for k in Counter(y_train).keys():  # k=0,1,2
        label_dict[k] = Counter(y_train)[k] / len(y_train)  # 统计个数
        feture_dict[k] = calc(x_train[y_train == k])
        # x_test = pd.read_csv('E:/data/test_1000_clean_neg.csv', header=None).values[:1000, :2]
    x_test = pd.read_csv('E:/data/test_1000_clean_pos.csv', header=None).values[:1000, :2]
    for i in range(x_train.shape[0]):
        predict(x_test[i][0], x_test[i][1])  # predict(2, 2, 0, 1, 2)
