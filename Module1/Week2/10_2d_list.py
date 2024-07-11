# Section 10: 2D List


def matrix_3by3():
    '''Returns a 3x3 matrix filled with numbers from 1 to 9

    Args:
        None

    Returns:
        matrix: 3x3 matrix filled with numbers from 1 to 9
    '''
    matrix = []

    num = 1
    for i in range(3):
        row = []
        for j in range(3):
            row.append(num)
            num += 1
        matrix.append(row)
        

    return matrix


lst_data = matrix_3by3()

def filter_02(lst_data):
    '''Remove column with index = 1'''

    for i in range(len(lst_data)):
        for j in range(len(lst_data[i])):
            if j == 1:
                value = lst_data[i][j]
                lst_data[i].remove(value)

    return lst_data

print(filter_02(lst_data))