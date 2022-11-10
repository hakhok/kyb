import numpy as np
from matplotlib import pyplot as plt
import control as co

# plt.rcParams['figure.figsize'] = [12, 5]
# plt.rcParams['font.size'] = 12

G1 = co.tf([2, 5], [1, 2, 3])
G1_ss = co.tf2ss(G1)
G1_tf = co.ss2tf(G1_ss)
# print(G1)
# print(G1_ss)
# print(G1_tf)

# zeroes and poles
G2 = 5 * co.tf(np.poly([-2, -5]), np.poly([-4, -5, -9]))
# print(G2)

A = [
    [0, 1, 0],
    [0, 0, 1],
    [-1, -2, -3]
]
B = [[1],[0],[1]]
C = [1, 0, 0]
D = 0
sys = co.ss(A, B, C, D)
sys_tf = co.ss2tf(sys)
# print(sys)
# print(sys_tf)

t = np.linspace(0, 25, 1000)
t1, y1 = co.impulse_response(sys, t)
t2, y2 = co.step_response(sys, t)
t3, y3 = co.step_response(sys, t, [-1, 1, 3])

# fig, axs = plt.subplots(3)

# axs[0].plot(t1, y1)
# axs[0].grid()
# axs[0].set_title("impulse response")

# axs[1].plot(t2, y2)
# axs[1].grid()
# axs[1].set_title("step response")

# axs[2].plot(t3, y3)
# axs[2].grid()
# axs[2].set_title("step response with initial condotions")

# plt.xlabel('time (s)')
# plt.ylabel('amplitude')

# 

# co.bode_plot(sys, dB=True)
# co.nyquist_plot(sys)
# plt.show()

G3 = co.tf([10], np.poly([-1, -2, -3]))

gm, pm, _, pcf, gcf, _ = co.stability_margins(G3)
# print(G3)
# print(f"PCF = {pcf}, GM (abs) = {gm}, GCF = {gcf}, PM (deg) = {pm}")

G4 = co.tf([1], [1, 4, 5, 0])
print(G4)
co.root_locus(G4)
plt.show()
