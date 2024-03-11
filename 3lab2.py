import sympy as sp

# Функция уравнения
def equation(x):
    return x**2 - 3 - 7

# Определение переменной и функции
x_sym = sp.Symbol('x')
f_sym = x_sym**2 - 3

# Вычисление производной
f_derivative_sym = sp.diff(f_sym, x_sym)

# Преобразование выражения производной в функцию Python
f_derivative_func = sp.lambdify(x_sym, f_derivative_sym)

# Функция для решения уравнения методом половинного деления
def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("Функция должна принимать разные знаки на концах интервала")
    
    for _ in range(max_iter):
        x_mid = (a + b) / 2
        if abs(f(x_mid)) < tol:
            return x_mid
        if f(x_mid) * f(a) < 0:
            b = x_mid
        else:
            a = x_mid
    raise ValueError("Метод не сошелся")

# Функция для решения уравнения методом хорд
def chord_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("Функция должна принимать разные знаки на концах интервала")
    
    for _ in range(max_iter):
        x_new = b - (f(b) * (b - a)) / (f(b) - f(a))
        if abs(f(x_new)) < tol:
            return x_new
        a, b = b, x_new
    raise ValueError("Метод не сошелся")

# Функция для решения уравнения методом Ньютона
def newton_method(f, f_prime, x0, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        x_new = x0 - f(x0) / f_prime(x0)
        if abs(f(x_new)) < tol:
            return x_new
        x0 = x_new
    raise ValueError("Метод не сошелся")

# Решение уравнения на интервале [0, 5] тремя методами
a, b = 0, 5
x0 = (a + b) / 2  # Начальное приближение для метода Ньютона

# Решение методом половинного деления
solution_bisection = bisection_method(equation, a, b)
print("Решение методом половинного деления:", solution_bisection)

# Решение методом хорд
solution_chord = chord_method(equation, a, b)
print("Решение методом хорд:", solution_chord)

# Решение методом Ньютона
solution_newton = newton_method(equation, f_derivative_func, x0)
print("Решение методом Ньютона:", solution_newton)

# Вывод производной функции
print("Производная функции f(x):", f_derivative_sym)
