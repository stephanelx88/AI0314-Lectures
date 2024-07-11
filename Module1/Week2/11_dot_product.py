# Implement a function to compute the dot product of 2 matrices

def dot_product(mat_a, mat_b) -> list:
    '''
    Returns the dot product of 2 matrices

    Args:
        mat_a: The first matrix
        mat_b: The secon matrix

    Returns:
        dot_product: The dot product of matrix a and matrix b
    '''

    # Check if the 2 matrices are eligible to run dot product
    if len(mat_a) == len(mat_b[0]):
        dot_product = []

        for i in range(len(mat_a)): # i is the row index of matrix A
            product_row = []
    
            for j in range(len(mat_b[0])): # j is column index of matrix B
                total = 0
                for k in range(len(mat_b)): # k is row index of matrix B
                    a_value = mat_a[i][k]
                    b_value = mat_b[k][j]
            
                    total += a_value*b_value
                product_row.append(total)
        
            dot_product.append(product_row)
        return dot_product

    return 'Invalid matrices'


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


print(dot_product(mat_a, mat_b))