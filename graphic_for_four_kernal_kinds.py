# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt

if __name__ == "__main__":
    list4 = [i for i in range(0, 4)]
    list_pos = [0.88, 0.882, 0.42, 0.716]
    list_neg = [0.892, 0.89, 0.964, 0.782]
    font1 = {'family': 'Times New Roman',
             'size': 10}  # 设置标签区域
    tick_label = ["Rbf", "Linear", "Poly", "Sigmoid"]  # 四种核函数类型
    plt.plot(list4, list_pos, '-..', color='gray', linewidth=1, label='Positive')
    plt.plot(list4, list_neg, '-.*', color='#778899', linewidth=1, label='Negative')  # 绘制图形
    plt.ylim(0, 1)
    plt.xlabel('Types of kernel functions', font1)
    plt.ylabel('Ratio(%)', font1)  # 设置主题
    plt.xticks(list4, tick_label)
    plt.legend()
    plt.show()