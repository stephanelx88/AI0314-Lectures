mat_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mat_b = [
    [2, 4, 6],
    [1, 3, 5],
    [1, 0, 1]
]


def plus(mat_a, mat_b):
    '''Adds two matrices mat_a and mat_b together
    
    Args:
        mat_a: Matrix 1
        mat_b: Matrix 2

    Returns:
        result: A matrix summing of mat_a and mat_b
    '''

    n_row = len(mat_a)
    n_col = len(mat_a[0])
    
    result = []

    for i in range(n_row):
        row = []

        for j in range(n_col):
            value = mat_a[i][j] + mat_b[i][j]
            row.append(value)

        result.append(row)

    return result

def substract(mat_a, mat_b):
    '''Adds two matrices mat_a and mat_b together
    
    Args:
        mat_a: Matrix 1
        mat_b: Matrix 2

    Returns:
        result: A matrix summing of mat_a and mat_b
    '''

    n_row = len(mat_a)
    n_col = len(mat_a[0])
    
    result = []

    for i in range(n_row):
        row = []

        for j in range(n_col):
            value = mat_a[i][j] - mat_b[i][j]
            row.append(value)

        result.append(row)

    return result

def transpose(matrix):
    '''Converts rows to columns of a matrix'''

    n_row = len(matrix)
    n_col = len(matrix[0])

    result = [[0 for _ in range(n_col)] for _ in range(n_row)]
    

    for i in range(n_row):
        for j in range(n_col):
            value = matrix[i][j]
            result[j][i] = value
    
    return result
            
    

def dot(mat_a, mat_b):
    '''Multipy two matrices mat_a and mat_b together
    
    Args:
        mat_a: Matrix 1
        mat_b: Matrix 2

    Returns:
        result: A matrix multiplying of mat_a and mat_b
    '''

    n_row = len(mat_a)
    n_col = len(mat_a[0])
    result = [[0 for _ in range(n_col)] for _ in range(n_row)]
    mat_b_transposed = transpose(mat_b)

    for i in range(n_row):
        for j in range(n_col):
            for m in range(n_row):
                for k in range(n_col):
                    print(f"i={i}, j={j}, m={m}, k={k}")
                print()


    return result


print(plus(mat_a, mat_b))
print(substract(mat_a, mat_b))


