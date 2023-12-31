def naive_multiply(a, b):
    n = len(a)
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(0,n):
      #Loop through the rows of matrix a and c
        for j in range(0,n):
          #Loop through the columns of matrix b and c
            for k in range(0,n):
              #Multiply and loop through rows of matrix b
                c[i][j] += a[i][k] * b[k][j]
    return c
a = [[1, 3],
     [5, 7]]
b = [[2, 4],
     [6, 8]]
c = naive_multiply(a, b)
print(c)