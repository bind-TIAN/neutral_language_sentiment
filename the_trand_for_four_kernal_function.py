# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
if __name__ == "__main__":
    list4 = [i for i in range(0, 4)]
    list_pos = [1.57, 2.20, 2.06, 1.46]
    tick_label = ["Rbf", "Linear", "Poly", "Sigmoid"]#绘制图形
    plt.plot(list4, list_pos, '-..', color='gray', linewidth=1, label='Test dataset')
    font1 = {'family': 'Times New Roman',
             'size': 10}
    plt.ylim(0, 3)
    plt.xlabel('Types of kernel functions', font1)#设置主题
    plt.ylabel('Time(%)', font1)
    plt.xticks(list4, tick_label)
    plt.legend()
    plt.show()