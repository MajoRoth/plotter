import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from pandas import read_csv

# Matlab Settings
figure_width = 12
figure_height = 20

plt.rcParams["figure.figsize"] = (figure_width, figure_height)
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 22
plt.rcParams['axes.linewidth'] = 3


# Data Settings
data_path = './../data/rlc_analyzed.csv'
# unpack data
data_frame = read_csv(data_path)

phase = -data_frame["phase [rad]"]
amplitude = data_frame["amplitude [V]"]
frequency = data_frame["frequency [KHz]"]



def show_phase_by_frequency():
    # Fit
    def objective_phase_to_freq(x, a, b):
        return -np.arctan((a * x - 1 / (b * x)) / (1.618))

    popt, pcov = curve_fit(objective_phase_to_freq, frequency, phase, p0=[0.2769, 0.0003])
    fit = objective_phase_to_freq(frequency, popt[0], popt[1])
    print_fit_data(objective_phase_to_freq, popt, pcov)

    residuals = phase - fit

    """
        Show Graphs
    """
    fig, ax = plt.subplots(2)
    fig.tight_layout(pad=4.0)
    ax[0].plot(frequency, phase, 'o', markersize=7, markeredgewidth=1, color='blue', markerfacecolor='lightskyblue', label='Measurement')
    ax[0].plot(frequency, fit, '-', color='red', label="Fit", linewidth=3)
    ax[0].plot(frequency, fit, '-', color='red', label="Fit", linewidth=3)
    ax[0].set_xlabel('$Frequency (KHz)$', fontsize=26)
    ax[0].set_ylabel('$Phase (rad)$', fontsize=26)
    ax[0].set_title("Phase Measured as function of Frequency", fontname="Arial", size=32, fontweight="bold")
    ax[0].legend(loc='best')

    ax[1].stem(frequency, residuals, label='Residuals', linefmt='black')
    ax[1].set_title("Residuals Graph", fontname="Arial", size=32, fontweight="bold")
    ax[1].set_xlabel('$Frequency (Khz)$', fontsize=26)
    ax[1].set_ylabel('$Phase (rad)$', fontsize=26)

    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    ax[0].grid()
    ax[1].grid()

    # plt.show()
    # THIS IS HOW YOU SHOULD SAVE - YES IN PDF FORMAT
    plt.savefig("./../graphs/rlc_phase_to_freq.png", dpi=300)


def show_amplitude_by_frequency():

    def objective_amplitude_to_freq(x, a, b, c):
        return 2 / (np.sqrt(
            c ** 2 + (a * x - 1 / (b * x)) ** 2
        ))

    popt, pcov = curve_fit(objective_amplitude_to_freq, frequency, amplitude, p0=[0.008, 0.001, 0.8])
    fit = objective_amplitude_to_freq(frequency, popt[0], popt[1], popt[2])
    print_fit_data(objective_amplitude_to_freq, popt, pcov)

    residuals = amplitude - fit

    """
        Show Graphs
    """
    fig, ax = plt.subplots(2)
    fig.tight_layout(pad=4.0)

    ax[0].plot(frequency, amplitude, 'o', markersize=7, markeredgewidth=1, color='blue', markerfacecolor='lightskyblue', label='Measurement')
    ax[0].plot(frequency, fit, '-', color='red', label="Fit", linewidth=3)
    ax[0].set_xlabel('$Frequency (Khz)$', fontsize=26)
    ax[0].set_ylabel('$Amplitude (V)$', fontsize=26)
    ax[0].set_title("Amplitude Measured as function of Frequency", fontname="Arial", size=32, fontweight="bold")
    ax[0].legend(loc='best')

    ax[1].stem(frequency, residuals, label='Residuals', linefmt='black')
    ax[1].set_title("Residuals Graph", fontname="Arial", size=32, fontweight="bold")
    ax[1].set_xlabel('$Frequency (Khz)$', fontsize=26)
    ax[1].set_ylabel('$Amplitude (V)$', fontsize=26)

    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    ax[0].grid()
    ax[1].grid()

    # plt.show()

    plt.savefig("./../graphs/rlc_amplitude_to_freq.png", dpi=300)


def print_fit_data(objective, popt, pcov):
    perr = np.sqrt(np.diag(pcov))
    print(f"printing [{objective.__name__}] fitting values")
    for i, var in enumerate(objective.__code__.co_varnames[1:]):
        print(f"parameter {var} = {popt[i]}, with std={perr[i]}")

show_phase_by_frequency()