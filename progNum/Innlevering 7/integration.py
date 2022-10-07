import numpy as np

def integrate_midpoint(f, a, b):
    return (b-a)*f((a+b)/2)

def integrate_trapezoidal(f, a, b):
    return (b-a)*(f(a)+f(b))/2



for n in range(5):
    def f(x): return x**n
    a = 0
    b = 1

    I_mid = integrate_midpoint(f, a, b)
    I_trap = integrate_trapezoidal(f, a, b)
    I_exact = (1/(n+1))*b**(n+1) - (1/(n+1))*a**(n+1)
    print(f"n: {n}. Error mid: {I_mid-I_exact}. Error trap: {I_trap-I_exact}.")

# The error is 0 for both functions when n = 0 and 1
# This is because the numerical methods gives the right answears for
# these numbers

def integrate_composite_trapezoidal(f,a,b,n):
    d_x = (b-a)/n
    integral = 0
    for k in range(n):
        x = a+k*d_x
        integral += (f(x) + f(x + d_x))/2
    return integral*d_x

def integrate_composite_simpson(f,a,b,n):
    d_x = (b-a)/n
    integral = f(a)+f(b)
    for k in range(n-1):
        k+=1
        x = a+k*d_x
        if k%2==0:
            integral+= 2*f(x)
        else:
            integral+= 4*f(x)
    integral = integral*d_x/3
    return integral

a = 0
b = 1
n = 10

def y(x):   return x**5 - x**3 + np.exp(x)
def y2(x):  return -(3/4)*x**3+x**2+17*x
def f(x):   return 5*x**4 - 3*x**2 + np.exp(x)
def f2(x):  return -4*x**2 +2*x +17

I_exact = y(b)-y(a)
I_exact2 = y2(b)-y2(a)
I_trap = integrate_composite_trapezoidal(f, a, b, n)
I_simp = integrate_composite_simpson(f, a, b, n)
I_simp2 = integrate_composite_simpson(f2, a, b, n)

print(f"\ntrap: {round(I_trap, 2)} error: {I_exact-I_trap}")
print(f"simp: {round(I_simp, 2)} error: {I_exact-I_simp}")
print(f"simp2: {round(I_simp2, 2)} error: {I_exact2-I_simp2}")

# Error when using f(x) = -4x^2+2x+17 is 14.948384838207623