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
data_path = './../data/coupled_result.csv'

# unpack data
data_frame = read_csv(data_path)
frequency = data_frame["Frequency (kHz)"]
amplitude = data_frame["Amplitude (V)"]
phase = data_frame["Phase (rad)"]

# process data


def show_amplitude_to_freq():
    fig, ax = plt.subplots()
    ax.plot(frequency, amplitude, 'o', markersize=10, markeredgewidth=1, color='blue',
            markerfacecolor='lightskyblue', label='Measurement')
    ax.set_xlabel('$Frequency (kHz)$', fontsize=26)
    ax.set_ylabel('$Amplitude (V)$', fontsize=26)
    ax.set_title("Voltage Measured as function of Frequency", fontname="Arial", size=32, fontweight="bold")

    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    plt.grid()
    # plt.show()

    # THIS IS HOW YOU SHOULD SAVE - YES IN PDF FORMAT
    plt.savefig("./../graphs/coupled_rlc_amplitude_to_frequency.png", dpi=300)


def show_phase_to_freq():
    fig, ax = plt.subplots()
    ax.plot(frequency, phase, 'o', markersize=10, markeredgewidth=1, color='blue',
            markerfacecolor='lightskyblue', label='Measurement')
    ax.set_xlabel('$Frequency (kHz)$', fontsize=26)
    ax.set_ylabel('$Phase (rad)$', fontsize=26)
    ax.set_title("Phase Measured as function of Frequency", fontname="Arial", size=32, fontweight="bold")

    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    plt.grid()
    # plt.show()

    # THIS IS HOW YOU SHOULD SAVE - YES IN PDF FORMAT
    plt.savefig("./../graphs/coupled_rlc_phase_to_frequency.png", dpi=300)


show_amplitude_to_freq()
