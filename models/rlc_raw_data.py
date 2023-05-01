import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from pandas import read_csv

# Matlab Settings
figure_width = 12
figure_height = 12

plt.rcParams["figure.figsize"] = (figure_width, figure_height)
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 22
plt.rcParams['axes.linewidth'] = 3


# Data Settings
data_path = './../data/rlc_raw.csv'

# preprocess data
data_frame = read_csv(data_path)
data_frame = data_frame.drop(index=0)

print(data_frame)




time_ms = data_frame["Time"]
amplitude = data_frame["Channel A"]

print(time_ms)
print(amplitude)
# process data
time_ms_normal = time_ms.astype(float) + 100
amplitude = amplitude.astype(float)

# Create figure and add axes object
fig, ax = plt.subplots()
ax.plot(time_ms_normal, amplitude, 'o', markersize=10, markeredgewidth=1, color='blue', markerfacecolor='lightskyblue', label='Measurement')
ax.set_xlabel('$Time (ms)$', fontsize=26)
ax.set_ylabel('$v_{out} (V)$', fontsize=26)
ax.set_title("Voltage Measured as function of Time", fontname="Arial", size=28, fontweight="bold")

plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.grid()
#plt.show()

# THIS IS HOW YOU SHOULD SAVE - YES IN PDF FORMAT
plt.savefig("./../graphs/rlc_voltage_to_time.png", dpi=300)

