"""
    create a graph vor v_in by v_out
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from pandas import read_csv

# Matlab Settings
figure_width = 12
figure_height = 10

plt.rcParams["figure.figsize"] = (figure_width, figure_height)
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 20
plt.rcParams['axes.linewidth'] = 3


# Data Settings
data_path = './../data/picoscope_internal_resistance_measurement_1KOhm.csv'


# unpack data
data_frame = read_csv(data_path)
data = data_frame.values

v_in = data_frame["V_in [V]"]
v_out_milivolt = data_frame["V_out [mV]"]

# Process The Data
v_out = v_out_milivolt/1000

# fit the line
def objective(x, m, b):
    return m*x + b

popt, pcov = curve_fit(objective, v_in, v_out, p0=[0.1678, 0.0017])
perr = np.sqrt(np.diag(pcov))

fit = objective(v_in, popt[0], popt[1])

print(f"parameters={popt}, popt={perr}")

# Create figure and add axes object
fig, ax = plt.subplots()
ax.plot(v_in, v_out, 'o', markersize=10, markeredgewidth=1, color='blue', markerfacecolor='lightskyblue', label='Measurement')
ax.plot(v_in, fit, '-', color='red', label="Fit", linewidth=3)
ax.set_xlabel('$v_{in} (V)$', fontsize=26)
ax.set_ylabel('$v_{out} (V)$', fontsize=26)
ax.set_title("Voltage Measured As A Function of Voltage Generated", fontname="Arial", size=28, fontweight="bold")
plt.legend(loc='best')

plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.grid()
# plt.show()

# THIS IS HOW YOU SHOULD SAVE - YES IN PDF FORMAT
plt.savefig("./../graphs/internal_resistance.png", dpi=300)