def matrix_addition(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def matrix_subtraction(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def matrix_multiply(a, b):
    result = [[0] * len(b[0]) for _ in range(len(a))]
    
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]

    return result

def split(matrix):
    row, col = len(matrix), len(matrix[0])
    row2, col2 = row // 2, col // 2
    return (
        [matrix[i][:col2] for i in range(row2)], 
        [matrix[i][col2:] for i in range(row2)],  
        [matrix[i][:col2] for i in range(row2, row)], 
        [matrix[i][col2:] for i in range(row2, row)] 
    )

def strassen2(a, b):
    if len(a) == 1:
        return matrix_multiply(a, b)

    a00, a01, a10, a11 = split(a)
    b00, b01, b10, b11 = split(b)

    m1 = strassen2(matrix_addition(a00, a11), matrix_addition(b00, b11))
    m2 = strassen2(matrix_addition(a10, a11), b00)
    m3 = strassen2(a00, matrix_subtraction(b01, b11))
    m4 = strassen2(a11, matrix_subtraction(b10, b00))
    m5 = strassen2(matrix_addition(a00, a01), b11)
    m6 = strassen2(matrix_subtraction(a10, a00), matrix_addition(b00, b01))
    m7 = strassen2(matrix_subtraction(a01, a11), matrix_addition(b10, b11))

    c00 = matrix_addition(matrix_subtraction(matrix_addition(m1, m4), m5), m7)
    c01 = matrix_addition(m3, m5)
    c10 = matrix_addition(m2, m4)
    c11 = matrix_addition(matrix_subtraction(matrix_addition(m1, m3), m2), m6)

    c = (
        [c00[i] + c01[i] for i in range(len(c00))] +
        [c10[i] + c11[i] for i in range(len(c10))]
    )

    return c

a = [[1, 3], [5, 7]]
b = [[2, 4], [6, 8]]
c = strassen2(a, b)
print(c)
