from sympy import *
import math

x = Symbol('x')
m, n = 1, 1
a = 1

# INICIO - LETRA A

la1 = (x ** 2) - (5*x) + 10
la2 = (x ** 2) - 25

print("LETRA A")
print(limit(la1/la2, x, 5))
print("\n\n")

# FIM - LETRA A


# INICIO - LETRA B

lb1 = 1/(1 - x)
lb2 = 3/(1 - (x ** 3))

print("LETRA B")
print(limit(lb1-lb2, x, 1))
print("\n\n")


# FIM - LETRA B

# INICIO - LETRA C

lc1 = sqrt((x ** 2) - (2*x) + 6) - sqrt((x ** 2) + (2*x) - 6)
lc2 = (x ** 2) - (4 * x) + 3

derivada1 = lc1.diff(x)
derivada2 = lc2.diff(x)

print("LETRA C")
print("L'HOPITAL:",limit(derivada1/derivada2, x, 3))
print("SEM L'HOPITAL:", limit(lc1/lc2, x, 3))
print("\n\n")


# FIM - LETRA C


# INICIO - LETRA D #

ld = sqrt(x * (x + a)) - x

print("LETRA D")
print(limit(ld, x, +oo))
print("\n\n")

# FIM - LETRA D #


# INICIO - LETRA E #

le1 = 1 - sqrt(cos(x))
le2 = x ** 2

derivada1 = le1.diff(x)
derivada2 = le2.diff(x)

print("LETRA E")
print("L'HOPITAL:",limit(derivada1/derivada2, x, 0))
print("SEM L'HOPITAL:", limit(le1/le2, x, 0))
print("\n\n")

# FIM - LETRA E #

# INICIO - LETRA F #

lf1 = cos(m*x) - sin(n*x)
lf2 = x ** 2

derivada1 = lf1.diff(x)
derivada2 = lf2.diff(x)

print("LETRA F")
print("L'HOPITAL:", limit(derivada1/derivada2, x, 0))
print("SEM L'HOPITAL:", -limit(lf1/lf2, x, 0))
print("\n\n")

# FIM - LETRA F #

# INICIO - LETRA G #

lg1 = 1 - (x ** 2)
lg2 = sin(x*math.pi)

derivada1 = lg1.diff(x)
derivada2 = lg2.diff(x)

print("LETRA G")
print("L'HOPITAL:", int(limit(derivada1/derivada2, x, 1)))
print("SEM L'HOPITAL:", limit(lg1/lg2, x, 1))
print("\n\n")

# FIM - LETRA G #


