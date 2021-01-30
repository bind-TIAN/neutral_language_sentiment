# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd
import jieba
import jieba.posseg
from sklearn.svm import SVC
from gensim.models import word2vec
from sklearn.model_selection import train_test_split
import warnings


def svm_tran(train_vec, y_train, test_vec, y_test, list_one, list_two, train_model):
    jishu_pos, jishu_neg, jishu_pos_pos, jishu_pos_neg = 0, 0, 0, 0
    clf = SVC(C=1)  # 设置参数
    clf.fit(train_vec, y_train)
    print(clf.score(train_vec, y_train), clf.score(test_vec, y_test))  # 打印权值分数
    if clf.score(test_vec, y_test) >= 0.55:  # 设置阈值
        for line in list_one:
            result = clf.predict(get_sent_vec(300, jieba.lcut(line), train_model))  # 对句子进行预测
            if int(result[0] == 1):
                jishu_pos += 1
            else:
                jishu_neg += 1
        for line in list_two:
            result = clf.predict(get_sent_vec(300, jieba.lcut(line), train_model))
            if int(result[0] == 1):
                jishu_pos_pos += 1
            else:
                jishu_pos_neg += 1
    return jishu_pos, jishu_neg, jishu_pos_pos, jishu_pos_neg


def get_sent_vec(size, sentence, model):  # 计算句子的均值得分
    vec = np.zeros(size).reshape(1, size)
    count = 0
    for word in sentence:
        try:
            vec += model[word].reshape(1, size)
            count += 1
        except:
            continue
    if count != 0:
        vec /= count
    return vec


def practice(list1, list2, list_pos, list_neg):
    jishu_pos, jishu_neg, jishu_pos_pos, jishu_pos_neg, cishu = 0, 0, 0, 0, 0
    table = np.append((np.ones(len(list1))), (np.zeros(len(list2))), axis=0)
    pos_and_neg = np.concatenate([[jieba.lcut(line) for line in list1], [jieba.lcut(line) for line in list2]])  # 合并
    while True:
        cishu += 1
        print(cishu)
        x_train, x_test, y_train, y_test = train_test_split(pos_and_neg, table, test_size=0.2)  # 二八分割
        train_model = word2vec.Word2Vec(x_train, hs=1, min_count=1, window=5, size=300, iter=100)  # 词向量工具
        test_model = word2vec.Word2Vec(x_test, hs=1, min_count=1, window=5, size=300, iter=100)
        train_vec = np.concatenate([get_sent_vec(300, line, train_model) for line in x_train])
        test_vec = np.concatenate([get_sent_vec(300, line, test_model) for line in x_test])
        jishu_pos, jishu_neg, jishu_pos_pos, jishu_pos_neg = svm_tran(train_vec, y_train, test_vec, y_test,
                                                                      list_pos, list_neg, train_model)  # 训练模型
        if jishu_pos != 0 and jishu_neg != 0 and jishu_pos_pos != 0 and jishu_pos_neg != 0:
            break
    return jishu_pos, jishu_neg, jishu_pos_pos, jishu_pos_neg


if __name__ == "__main__":
    warnings.filterwarnings('ignore')
    jishu_pos, jishu_neg, jishu_pos_pos, jishu_pos_neg = 0, 0, 0, 0
    ep1, ep2, ep3, en1, en2, en3, tp, tn = [], [], [], [], [], [], [], []

    neg = pd.read_excel('E:/data/SVM_5550_neg.xlsx', header=None).values[:3000, :]
    pos = pd.read_excel('E:/data/SVM_5550_pos.xlsx', header=None).values[:3000, :]  # 读文件数据
    print(pos.shape)
    for i in range(3000, 4000):
        test_neg = pd.read_excel('E:/data/SVM_5550_neg.xlsx', header=None).values[:i, :]
        test_pos = pd.read_excel('E:/data/SVM_5550_pos.xlsx', header=None).values[:i, :]
    for i in range(0, 1000):
        tp.append(test_pos[i][0])
        tn.append(test_neg[i][0])
    element_pos1, element_pos2, element_pos3 = np.split(pos, 3)
    print(element_pos1)
    element_neg1, element_neg2, element_neg3 = np.split(neg, 3)  # 分割数据
    for i in range(0, 1000):
        ep1.append(element_pos1[i][0])
        en1.append(element_neg1[i][0])
    for i in range(1000, 2000):
        ep2.append(element_pos2[i][0])
        en2.append(element_neg2[i][0])
    for i in range(2000, 3000):
        ep3.append(element_pos3[i][0])
        en3.append(element_neg3[i][0])

    boss_pos1 = np.concatenate([ep1, ep2, ep3])
    boss_neg1 = np.concatenate([en1, en2, en3])  # 第一种情况

    boss_pos2 = np.concatenate([ep1, ep2, tp])
    boss_neg2 = np.concatenate([en1, en2, tn])  # 第二种情况

    boss_pos3 = np.concatenate([ep1, ep3, tp])
    boss_neg3 = np.concatenate([en1, en3, tn])  # 第三种情况

    boss_pos4 = np.concatenate([ep2, ep3, tp])
    boss_neg4 = np.concatenate([en2, en3, tn])  # 第四种情况

    jishu_pos, jishu_neg, jishu_pos_pos, jishu_pos_neg = practice(boss_pos1, boss_neg1, tp, tn)  # 第一种情况实验

    print("#######第一种情况########")
    print(jishu_pos, jishu_neg, jishu_pos_pos, jishu_pos_neg)

    jishu_pos, jishu_neg, jishu_pos_pos, jishu_pos_neg = practice(boss_pos2, boss_neg2, ep3, en3)  # 第二种情况实验
    print("#######第二种情况########")
    print(jishu_pos, jishu_neg, jishu_pos_pos, jishu_pos_neg)

    jishu_pos, jishu_neg, jishu_pos_pos, jishu_pos_neg = practice(boss_pos3, boss_neg3, ep2, en2)  # 第三种情况
    print("#######第三种情况########")
    print(jishu_pos, jishu_neg, jishu_pos_pos, jishu_pos_neg)

    jishu_pos, jishu_neg, jishu_pos_pos, jishu_pos_neg = practice(boss_pos4, boss_neg4, ep1, en1)  # 第四种情况
    print("#######第四种情况########")
    print(jishu_pos, jishu_neg, jishu_pos_pos, jishu_pos_neg)
