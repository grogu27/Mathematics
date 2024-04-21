def left_rectangle_method(f, a, b, n):
    """Left Rectangle Method for numerical integration"""
    h = (b - a) / n
    integral = 0
    for i in range(n):
        integral += f(a + i * h)
    integral *= h
    return integral

def middle_rectangle_method(f, a, b, n):
    """Middle Rectangle Method for numerical integration"""
    h = (b - a) / n
    integral = 0
    for i in range(n):
        integral += f(a + (i + 0.5) * h)
    integral *= h
    return integral

def right_rectangle_method(f, a, b, n):
    """Right Rectangle Method for numerical integration"""
    h = (b - a) / n
    integral = 0
    for i in range(1, n + 1):
        integral += f(a + i * h)
    integral *= h
    return integral

def trapezoidal_method(f, a, b, n):
    """Trapezoidal Method for numerical integration"""
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

# Example usage:
def f(x):
    return x ** 2

a = 0
b = 1
n = 100

left_integral = left_rectangle_method(f, a, b, n)
middle_integral = middle_rectangle_method(f, a, b, n)
right_integral = right_rectangle_method(f, a, b, n)
trapezoidal_integral = trapezoidal_method(f, a, b, n)

print("Left Rectangle Method Integral:", left_integral)
print("Middle Rectangle Method Integral:", middle_integral)
print("Right Rectangle Method Integral:", right_integral)
print("Trapezoidal Method Integral:", trapezoidal_integral)
