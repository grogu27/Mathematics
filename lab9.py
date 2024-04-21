import math
import random

def f(x, y):
    return x * y

def euler_method(f, x0, y0, h, n):
    """Euler's method for solving ordinary differential equations"""
    x_values = [x0]
    y_values = [y0]
    for i in range(1, n+1):
        x = x0 + i * h
        y = y_values[-1] + h * f(x_values[-1], y_values[-1])
        x_values.append(x)
        y_values.append(y)
    return x_values, y_values

def runge_kutta_method(f, x0, y0, h, n):
    """Runge-Kutta method (4th order) for solving ordinary differential equations"""
    x_values = [x0]
    y_values = [y0]
    for i in range(1, n+1):
        x = x0 + i * h
        k1 = h * f(x_values[-1], y_values[-1])
        k2 = h * f(x_values[-1] + 0.5 * h, y_values[-1] + 0.5 * k1)
        k3 = h * f(x_values[-1] + 0.5 * h, y_values[-1] + 0.5 * k2)
        k4 = h * f(x_values[-1] + h, y_values[-1] + k3)
        y = y_values[-1] + (k1 + 2*k2 + 2*k3 + k4) / 6
        x_values.append(x)
        y_values.append(y)
    return x_values, y_values

def modified_euler_method(f, x0, y0, h, n):
    """Modified Euler's method for solving ordinary differential equations"""
    x_values = [x0]
    y_values = [y0]
    for i in range(1, n+1):
        x = x0 + i * h
        y_predictor = y_values[-1] + h * f(x_values[-1], y_values[-1])
        y_corrector = y_values[-1] + h * 0.5 * (f(x_values[-1], y_values[-1]) + f(x, y_predictor))
        x_values.append(x)
        y_values.append(y_corrector)
    return x_values, y_values

def monte_carlo_integration(f, a, b, n):
    """Monte Carlo integration for numerical integration"""
    integral = 0
    for _ in range(n):
        x = random.uniform(a, b)
        integral += f(x)
    integral *= (b - a) / n
    return integral

# Пример использования всех методов:
x0 = 0
y0 = 1
h = 0.1
n = 10

# Метод Эйлера
x_values_euler, y_values_euler = euler_method(f, x0, y0, h, n)

# Метод Рунге-Кутты 4-го порядка
x_values_rk4, y_values_rk4 = runge_kutta_method(f, x0, y0, h, n)

# Метод Эйлера с перерасчетами
x_values_modified_euler, y_values_modified_euler = modified_euler_method(f, x0, y0, h, n)

# Метод Монте-Карло для вычисления интеграла sin(x) от 0 до pi
a = 0
b = math.pi
n_integral = 1000000
monte_carlo_integral = monte_carlo_integration(math.sin, a, b, n_integral)

# Вывод результатов
print("Euler's Method:")
for x, y in zip(x_values_euler, y_values_euler):
    print(f"x = {x}, y = {y}")

print("\nRunge-Kutta Method (4th Order):")
for x, y in zip(x_values_rk4, y_values_rk4):
    print(f"x = {x}, y = {y}")

print("\nModified Euler's Method:")
for x, y in zip(x_values_modified_euler, y_values_modified_euler):
    print(f"x = {x}, y = {y}")

print("\nMonte Carlo Method Integral (sin(x) from 0 to pi):", monte_carlo_integral)
