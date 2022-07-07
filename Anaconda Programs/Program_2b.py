# Program 2b: the logistic equation.
from sympy import *
t=symbols('t');a=symbols('a');b=symbols('b')
P=symbols('P',cls=Function)
sol=dsolve(Eq(P(t).diff(t),P(t)*(a-b*P(t))),P(t))
print(sol)