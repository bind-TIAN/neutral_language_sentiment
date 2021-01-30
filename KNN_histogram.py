# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

x = np.arange(4)
y = [0.812, 0.778, 0.846, 0.814]
y1 = [0.896, 0.884, 0.886, 0.892]
font1 = {'family': 'Times New Roman',
         'size': 10}  # 调整字体和字号
bar_width = 0.2
tick_label = ["1", "2", "3", "4"]
plt.xlim(-1, 4)
plt.ylim(0, 1)  # 设置坐标区域
plt.bar(x, y, bar_width, align="center", color="#FF00FF", label="Positive", alpha=0.5)  # 绘制柱状图
plt.bar(x + bar_width, y1, bar_width, align="center", color="#7CFC00", label="Negative", alpha=0.5)
plt.xlabel("P-value", font1)
plt.ylabel("Ratio(%)", font1)
plt.title("11,000 balanced corpora", font1)  # 打印标签
plt.xticks(x + bar_width, tick_label)
plt.legend()
plt.show()