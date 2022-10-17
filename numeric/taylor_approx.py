import numpy as np
from matplotlib import pyplot as plt

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

x = -5
y0 = f(x)
y1 = f(x)
y2 = f(x)
y3 = f(x)
y4 = f(x)
x_max = 3
dx = 1

y_list0 = [y0]
y_list1 = [y1]
y_list2 = [y1]
y_list3 = [y1]
y_list4 = [y1]
x_list = [x]

while x<=x_max:
    y1 = f(x) + dx*f_dx(x)+((dx**2)/np.math.factorial(2))*f_ddx(x)+((dx**3)/np.math.factorial(3))*f_dddx(x)+((dx**4)/np.math.factorial(4))*f_ddddx(x)
    y2 = f(x) + dx*f_dx(x)+((dx**2)/np.math.factorial(2))*f_ddx(x)+((dx**3)/np.math.factorial(3))*f_dddx(x)
    y3 = f(x) + dx*f_dx(x)+((dx**2)/np.math.factorial(2))*f_ddx(x)
    y4 = f(x) + dx*f_dx(x)

    x += dx
    y_list1.append(y1)
    y_list2.append(y2)
    y_list3.append(y3)
    y_list4.append(y4)
    x_list.append(x)
    y_list0.append(f(x))

# plt.plot(x_list, y_list0, '--g')
plt.plot(x_list, y_list1)
plt.plot(x_list, y_list2)
plt.plot(x_list, y_list3)
plt.plot(x_list, y_list4)
plt.show()