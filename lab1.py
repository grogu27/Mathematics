import math

def f(x):
    return x**2 - 3 - 7

def df(x):
    return 2*x

def newton_method(x0, epsilon, max_iterations):
    x = x0
    for i in range(max_iterations):
        fx = f(x)
        if abs(fx) < epsilon:
            print(f"Решение найдено после {i+1} итераций: x = {x}")
            return x
        dfx = df(x)
        if dfx == 0:
            print("Производная равна нулю. Метод Ньютона не сходится.")
            return None
        x = x - fx / dfx
    print(f"Метод не сошелся после {max_iterations} итераций.")
    return None

x0 = 2 
epsilon = 1e-3  
max_iterations = 100 

root = newton_method(x0, epsilon, max_iterations)
