from sympy import *
import numpy as np
from matplotlib import pyplot as plt

x = Symbol('x')
f = 2*x**2+3
df = f.diff(x)
ddf = df.diff(x)
dddf = ddf.diff(x)
ddddf = dddf.diff(x)
print(f)
print(df)

f = lambdify(x, f)
df = lambdify(x, df)

t = np.linspace(-5, 5, 100)
y = f(t)
dy=df(t)

plt.plot(t, y)
plt.plot(t, dy)
plt.show()