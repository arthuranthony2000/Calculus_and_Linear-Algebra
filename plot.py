import matplotlib.pyplot as plt
from math import sin
x = []
y = []
f = lambda x: sin(x)

a = -10
b = 10

c = a
i = 0.001

try:
    v = abs((f(b)-f(a))/(b-a))
except ZeroDivisionError:
    v = abs((f(b) - 1) / (b - a))
h = 0.001


while c <= b:
    try:
        lg = (f(c-h)-f(c))/h
    except ZeroDivisionError:
        lg = (f(c-h) - 1)/h
    if abs(lg-v) < 0.001:
        plt.plot(c, f(c), 'og')
        plt.plot([c - (0.001 * 1000), c + (0.001 * 1000)], [f(c) - lg * (c - c - (0.001 * 1000)), f(c) - lg * (c - c + (0.001 * 1000))])
    x.append(c)
    y.append(f(c))
    c += i

plt.title("ANÁLISE TEOREMA LAGRANGE")
plt.xlabel('X')
plt.ylabel('F(X)')
plt.plot(x, y, 'r')
plt.plot([a, b], [f(a), f(b)])
plt.show()