import random

def monte_carlo_integration(f, a, b, n):
    """Monte Carlo integration for numerical integration"""
    integral = 0
    for _ in range(n):
        x = random.uniform(a, b)
        integral += f(x)
    integral *= (b - a) / n
    return integral

# Example usage:
import math

def f(x):
    return math.sin(x)

a = 0
b = math.pi
n = 1000000

monte_carlo_integral = monte_carlo_integration(f, a, b, n)
print("Monte Carlo Method Integral:", monte_carlo_integral)
