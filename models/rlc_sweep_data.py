from pandas import read_csv
from plotter import plot_data
import numpy as np

# Matlab Settings
figure_width = 12
figure_height = 20

# Data Settings
data_path = './../data/rlc_analyzed.csv'
# unpack data
data_frame = read_csv(data_path)

phase = -data_frame["Phase [rad]"]
amplitude = data_frame["Amplitude [V]"]
frequency = data_frame["Frequency [KHz]"]


def phase_to_freq_fit(x, a, b, c):
    return -np.arctan((a * x - 1 / (b * x)) / (1.618)) + c

phase_starting_point = [0.2769, 0.0003, 0]
phase_starting_bounds = ((-100, -np.inf, -np.inf), (np.inf, np.inf, np.inf))


def amp_to_freq_fit(x, a, b, c):
    return 2 / (np.sqrt(
        c ** 2 + (a * x - 1 / (b * x)) ** 2
    ))

amp_starting_point = [0.008, 0.001, 0.8]

plot_data(frequency, phase, phase_to_freq_fit, starting_points=phase_starting_point, bounds=phase_starting_bounds, residuals=True, save=False)
plot_data(frequency, amplitude, amp_to_freq_fit, starting_points=amp_starting_point, residuals=True, save=False)



# def show_phase_by_frequency():
#     # Fit
#     def objective_phase_to_freq(x, a, b, c):
#         return -np.arctan((a * x - 1 / (b * x)) / (1.618)) + c
#
#     popt, pcov = curve_fit(objective_phase_to_freq, frequency, phase, p0=[0.2769, 0.0003, 0], bounds=((-100, -np.inf, -np.inf), (np.inf, np.inf, np.inf)))
#     fit = objective_phase_to_freq(frequency, popt[0], popt[1], popt[2])
#     print_fit_data(objective_phase_to_freq, popt, pcov)
#
#     residuals = phase - fit
#
#     """
#         Show Graphs
#     """
#     fig, ax = plt.subplots(2)
#     fig.tight_layout(pad=4.0)
#     ax[0].plot(frequency, phase, 'o', markersize=7, markeredgewidth=1, color='blue', markerfacecolor='lightskyblue', label='Measurement')
#     ax[0].plot(frequency, fit, '-', color='red', label="Fit", linewidth=3)
#     ax[0].set_xlabel('$Frequency (KHz)$', fontsize=26)
#     ax[0].set_ylabel('$Phase (rad)$', fontsize=26)
#     ax[0].set_title("Phase Measured as function of Frequency", fontname="Arial", size=32, fontweight="bold")
#     ax[0].legend(loc='best')
#
#     ax[1].stem(frequency, residuals, label='Residuals', linefmt='black')
#     ax[1].set_title("Residuals Graph", fontname="Arial", size=32, fontweight="bold")
#     ax[1].set_xlabel('$Frequency (Khz)$', fontsize=26)
#     ax[1].set_ylabel('$Phase (rad)$', fontsize=26)
#
#     plt.yticks(fontsize=20)
#     plt.xticks(fontsize=20)
#     ax[0].grid()
#     ax[1].grid()
#
#     plt.show()
#     # THIS IS HOW YOU SHOULD SAVE - YES IN PDF FORMAT
#     plt.savefig("./../graphs/rlc_phase_to_freq.png", dpi=300)
#
#
# def show_amplitude_by_frequency():
#
#     def old_objective_amplitude_to_freq(x, a, b, c):
#         return 2 / (np.sqrt(
#             c ** 2 + (a * x - 1 / (b * x)) ** 2
#         ))
#
#     def objective_amplitude_to_freq(x, R, L, C):
#         Rs=618.6
#         Cs=32*10 ** (-12)
#
#         expression_1 =  Rs + (R) / (1 + (Cs * R * 2 * np.pi * x) ** 2)
#         expression_2 = (1) / (2 * np.pi * x * C) - 2 * np.pi * x * L + (Cs * 2 * np.pi * x * R ** 2) / (1 + (Cs * R * 2 * np.pi * x)**2)
#         return np.sqrt(expression_1 ** 2 + expression_2 ** 2)
#
#     # popt, pcov = curve_fit(objective_amplitude_to_freq, frequency, amplitude, p0=[0.008, 0.001, 0.8])
#     popt, pcov = curve_fit(objective_amplitude_to_freq, frequency, amplitude, p0=[1, 1, 1])
#     fit = objective_amplitude_to_freq(frequency, popt[0], popt[1], popt[2])
#     print_fit_data(objective_amplitude_to_freq, popt, pcov)
#
#     residuals = amplitude - fit
#
#     """
#         Show Graphs
#     """
#     fig, ax = plt.subplots(2)
#     fig.tight_layout(pad=4.0)
#
#     ax[0].plot(frequency, amplitude, 'o', markersize=7, markeredgewidth=1, color='blue', markerfacecolor='lightskyblue', label='Measurement')
#     ax[0].plot(frequency, fit, '-', color='red', label="Fit", linewidth=3)
#     ax[0].set_xlabel('$Frequency (Khz)$', fontsize=26)
#     ax[0].set_ylabel('$Amplitude (V)$', fontsize=26)
#     ax[0].set_title("Amplitude Measured as function of Frequency", fontname="Arial", size=32, fontweight="bold")
#     ax[0].legend(loc='best')
#
#     ax[1].stem(frequency, residuals, label='Residuals', linefmt='black')
#     ax[1].set_title("Residuals Graph", fontname="Arial", size=32, fontweight="bold")
#     ax[1].set_xlabel('$Frequency (Khz)$', fontsize=26)
#     ax[1].set_ylabel('$Amplitude (V)$', fontsize=26)
#
#     plt.yticks(fontsize=20)
#     plt.xticks(fontsize=20)
#     ax[0].grid()
#     ax[1].grid()
#
#     plt.show()
#
#     plt.savefig("./../graphs/rlc_amplitude_to_freq_new.png", dpi=300)


