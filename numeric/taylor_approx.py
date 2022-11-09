from cProfile import label
import numpy as np
from matplotlib import pyplot as plt
import math

def f(x):
    return 0.5*x**4 + 0.8*x**3 - 0.2*x**2 + 2*x+2

def f_dx(x):
    return  2*x**3 + (12/5)*x**2 - (2/5)*x+2

def f_ddx(x):
    return 6*x**2 + (24/5)*x-(2/5)

def f_dddx(x):
    return 12*x+24/5

def f_ddddx(x):
    return 12

def taylor1(x, x0):
    d=x-x0
    taylur_sum = f(x0)+f_dx(x0)*d
    return taylur_sum
def taylor2(x, x0):
    d=x-x0
    taylur_sum = f(x0)+f_dx(x0)*d+f_ddx(x0)*d**2 /math.factorial(2)
    return taylur_sum
def taylor3(x, x0):
    d=x-x0
    taylur_sum = f(x0)+f_dx(x0)*d+f_ddx(x0)*d**2 /math.factorial(2)+f_dddx(x0)*d**3 /math.factorial(3)
    return taylur_sum
def taylor4(x, x0):
    d=x-x0
    taylur_sum = f(x0)+f_dx(x0)*d+f_ddx(x0)*d**2 /math.factorial(2)+f_dddx(x0)*d**3 /math.factorial(3)+f_ddddx(x0)*d**4 /math.factorial(4)
    return taylur_sum

x_0=-2
x = np.linspace(-3,1.5,100)

plt.style.use('bmh')

for x_0 in x:
    plt.clf()
    y = f(x)
    y1 = taylor1(x, x_0)
    y2 = taylor2(x, x_0)
    y3 = taylor3(x, x_0)
    y4 = taylor4(x, x_0)

    # plt.plot(x, y,  label="Original")
    plt.scatter(x_0, f(x_0))

    plt.plot(x, y1, '--', label="Taylor 1")
    plt.plot(x, y2, '--', label="Taylor 2")
    plt.plot(x, y3, '--', label="Taylor 3")
    plt.plot(x, y4, '--', label="Taylor 4")
    plt.ylim([-2.5,15])
    plt.legend()
    plt.pause(0.08)
plt.show()
