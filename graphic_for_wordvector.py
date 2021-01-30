# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt

plt.subplot(1, 2, 1)
list4 = [i for i in range(100, 600, 100)]
list1 = [0.852, 0.854, 0.854, 0.87, 0.866]
list2 = [0.74, 0.722, 0.708, 0.712, 0.708]
font1 = {'family': 'Times New Roman',
         'size': 10}
plt.xlabel('Word2vec size number', font1)
plt.ylabel('Ratio(%)', font1)
plt.title('11000 balance corpus', font1)
plt.ylim(0.7, 0.9)
plt.plot(list4, list1, '-..', color='gray', linewidth=1, label='SVM-positive')
plt.plot(list4, list2, '-.*', color='blue', linewidth=1, label='SVM-negative')  # 绘制图形
plt.legend()
plt.subplot(1, 2, 2)
list5 = [i for i in range(100, 600, 100)]
list3 = [183.95, 217.03, 297, 357.4, 426.2]
font2 = {'family': 'Times New Roman',
         'size': 10}  # 设置主题区域
plt.xlabel('Word2vec size number', font2)
plt.ylabel('Time(s)', font2)
plt.title('11000 balance corpus', font2)
plt.ylim(150, 450)  # 设置阈值
plt.plot(list5, list3, '-..', color='gray', linewidth=1, label='time')
plt.legend()
plt.show()