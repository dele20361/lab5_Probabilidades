# Universidad Del Valle de Guatemala
# Teoría de Probabilidades
# Laboratorio 5
# Primer ejercicio

from sympy.stats import Poisson, E, variance, FiniteRV, density
from sympy import Symbol, simplify, diff

# Primer ejercicio
rate = Symbol('lambda', positive=True)
k = Symbol("k")
X = Poisson('x',1/2)
Den = density(X)(k)
V_esp = E(X)
Var = simplify(variance(X))

print("Density",Den)
print("Valor Esperado:", V_esp)
print("Varianza:", Var)
