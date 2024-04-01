def aitken_interpolation(x, y, xi):
    n = len(x)
    q = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        q[i][0] = y[i]

    for j in range(1, n):
        for i in range(n-j):
            q[i][j] = ((xi - x[i+j])*q[i][j-1] - (xi - x[i])*q[i+1][j-1]) / (x[i] - x[i+j])
    #for row in q:
        #print(row)
        
            print("P", min(i, j), max(i, j), ":", q[i][j])
    return q[0][n-1]

x = [1, 2, 3, 4]
y = [1.0000, 1.4142, 1.7321, 2.0000]
xi = 2.56

result = aitken_interpolation(x, y, xi)
print(f"The function value at x = {xi} is f({xi}) ≈ {result}")
