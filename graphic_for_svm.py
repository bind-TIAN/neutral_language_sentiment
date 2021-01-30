# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt

if __name__ == "__main__":
    list4 = [i for i in range(500, 5500, 500)]
    list1 = [0.804, 0.836, 0.795, 0.842, 0.861, 0.813, 0.852, 0.845, 0.848, 0.848]
    list2 = [0.826, 0.859, 0.847, 0.866, 0.848, 0.875, 0.871, 0.868, 0.879, 0.882]
    list3 = [0.832, 0.832, 0.848, 0.8, 0.802, 0.88, 0.877, 0.936, 0.892, 0.878]
    list5 = [0.76, 0.876, 0.805, 0.876, 0.850, 0.843, 0.818, 0.839, 0.828, 0.849]  # 数据
    font1 = {'family': 'Times New Roman',
             'size': 10}  # 设置字的型号
    plt.ylim(0.7, 1)
    plt.title("SVM balanced corpora", font1)
    plt.xlabel('Train_dataset_size', font1)  # 设置主题
    plt.ylabel('Ratio(%)', font1)
    plt.plot(list4, list1, '-..', color='gray', linewidth=1, label='Cross-validation positive')
    plt.plot(list4, list2, '-.*', color='#708090', linewidth=1, label='Cross-validation negative')
    plt.plot(list4, list3, '--.', color='blue', linewidth=1, label='Not-cross-validation positive')
    plt.plot(list4, list5, '--*', color='#FF00FF', linewidth=1, label='Not-cross-validation negative')  # 绘制图形
    plt.legend()
    plt.show()