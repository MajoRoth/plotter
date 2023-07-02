import pandas
import numpy as np
from plotter import plot_data, plot_comparison
import matplotlib.pyplot as plt
import matplotlib as mpl

# Data Settings



# preprocess data


FIGURE_WIDTH = 12
FIGURE_HEIGHT = 12
DOUBLE_FIGURE_HEIGHT = 18
FONT = "Arial"
FONT_WEIGHT = "bold"
FONT_SIZE = 22
LINE_WIDTH = 3

# matplotlib settings
mpl.rcParams['font.family'] = FONT
mpl.rcParams['font.weight'] = FONT_WEIGHT
plt.rcParams['font.size'] = FONT_SIZE
plt.rcParams['axes.linewidth'] = LINE_WIDTH


COLORS = ["red", "blue", "orange", "pink", "green", "purple"]

plt.rcParams["figure.figsize"] = (FIGURE_WIDTH, FIGURE_HEIGHT)
fig, graph_ax = plt.subplots(1)




# x = np.array(list(range(0, 35, 5)))
# print(x)
# y = [0.06, 0.06, 0.04, 0.04, 0.01, 0.14, 2.06]# 22.2, 46]
# y = np.array(y)
# std = [0.04, 0.04, 0.05, 0.05, 0.03, 0.16, 1.11]# 11.2, 3.35]
# std = np.array(std)


x = np.array([128, 256, 512, 1024, 2048]) / 100
y = [0.39, 0.31, 0.04, 0.06, 5.4]
y = np.array(y)
std = [0.41, 0.16, 0.08, 0.04, 1.6]
std = np.array(std)


graph_ax.yaxis.grid(True)

graph_ax.set_xlabel(f'$Bit~Rate~[kbps]$', fontsize=26)
graph_ax.set_ylabel(f'$BER [\%]$', fontsize=26)






graph_ax.set_xticks(x)


graph_ax.bar([1, 2, 3, 4, 5], y, yerr=std, align='center',
       alpha=0.9,
       ecolor='red',
       capsize=0, error_kw={'elinewidth': 6})

graph_ax.set_xticks([1, 2, 3, 4, 5])
graph_ax.set_xticklabels(["1", "2", "4", "8", "16"])
graph_ax.set_title(f"$BER~Measured~as~Function~of~Bit~Rate$", fontname="Arial", size=32, fontweight="bold")
graph_ax.legend(loc='best')


plt.tight_layout()


graph_dir_path="./../graphs"
# plt.show()
plt.savefig(f"{graph_dir_path}/BER-bit.eps"
                    .replace(" ", "_").replace("{", "").replace("}", ""), format="eps")
