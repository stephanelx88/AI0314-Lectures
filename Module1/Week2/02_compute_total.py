def compute_total(lst_data: list) -> float:
    '''Computes the total of numbers in lst_data

    Args:
        lst_data: a list of numbers to compute the total
    
    Returns:
        total: the total of the numbers in lst_data  
    '''

    total = 0
    for num in lst_data:
        total += num

    return total

lst_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

assert compute_total(lst_data) == 45
assert compute_total([-1, 9, 3]) == 11 
print('Unit test passed')

first_ten = [i for i in range(1, 11)]
print(compute_total(first_ten))