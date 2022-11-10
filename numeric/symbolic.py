from sympy import *
import numpy as np
from matplotlib import pyplot as plt
import math

x = Symbol('x')
# f = 0.5*x**4 + 0.8*x**3 - 0.2*x**2 + 2*x+2
f = x**4 + 30*x**3 -12*x**2 - 45*x +10
df = f.diff(x)
ddf = df.diff(x)
dddf = ddf.diff(x)
ddddf = dddf.diff(x)
f = lambdify(x, f)
df = lambdify(x, df)
ddf = lambdify(x, ddf)
dddf = lambdify(x, dddf)
ddddf = lambdify(x, ddddf)
func = [f, df, ddf, dddf, ddddf]

def taylor(x, x0, n):
    d=x-x0
    taylor_sum = 0
    for i in range(n+1):
        taylor_sum+=func[i](x0)*d**(i) /math.factorial(i)
    return taylor_sum

def taylor_anim(x):
    plt.style.use('bmh')

    for x_0 in x:
        plt.clf()
        y = f(x)
        y1 = taylor(x, x_0, 1)
        y2 = taylor(x, x_0, 2)
        y3 = taylor(x, x_0, 3)
        y4 = taylor(x, x_0, 4)

        plt.plot(x, y,  label="Original")
        plt.scatter(x_0, f(x_0))

        plt.plot(x, y1, '--', label="Taylor 1")
        plt.plot(x, y2, '--', label="Taylor 2")
        plt.plot(x, y3, '--', label="Taylor 3")
        # plt.plot(x, y4, '--', label="Taylor 4")
        y_max = y.max()
        y_min = y.min()
        diff = y_max-y_min
        plt.ylim([y_min-0.1*diff,y_max+0.1*diff])
        plt.legend()
        plt.pause(0.05)
    plt.show()

x = np.linspace(-5,5,200)
taylor_anim(x)
