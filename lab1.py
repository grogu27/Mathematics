def dot_product(vec1, vec2):
    return sum(x * y for x, y in zip(vec1, vec2))


def simple_iteration(A, b, x0, tol=1e-6, max_iter=1000):
    n = len(b)
    x = x0.copy()

    for k in range(max_iter):
        x_new = [0] * n
        for i in range(n):
            s = dot_product(A[i], x)
            s -= A[i][i] * x[i]
            x_new[i] = (b[i] - s) / A[i][i]

        if max(abs(x_new[i] - x[i]) for i in range(n)) < tol:
            return x_new

        x = x_new

    raise ValueError("Метод не сошёлся за указанное количество итераций")

A = [[10, 1, -1],
     [1, 10, -1],
     [-1, 1, 10]]
b = [11, 10, 10]
x0 = [0, 0, 0]

solution, iterations = simple_iteration(A, b, x0, tol=1e-12, max_iter=10000)
print("Решение:", solution)
