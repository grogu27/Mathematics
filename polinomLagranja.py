def lagrange_polynomial(x, xi_values, fi_values):
    n = len(xi_values)
    result = 0
    for i in range(n):
        term = fi_values[i]
        for j in range(n):
            if i != j:
                term *= (x - xi_values[j]) / (xi_values[i] - xi_values[j])
        result += term
    return result

def main():
    # Заданные точки
    xi_values = [0, 1, 3, 4]
    fi_values = [-4, 0.5, 0.5, 8]
    
    # Точка, в которой нужно вычислить значение функции
    x = 2
    
    # Вычисляем значение полинома Лагранжа в точке x
    result = lagrange_polynomial(x, xi_values, fi_values)

    print(f"The function value at x = {x} is f({x}) ≈ {result}")

if __name__ == "__main__":
    main()
