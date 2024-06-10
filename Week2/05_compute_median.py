# Section 5: Computing median for a list of numbers

def median(lst_data: list) -> float:
    '''Returns the median of the numbers in lst_data
    
    Args:
        lst_data: a list of numbers to calculate the median of

    Returns:
        med: the median of the numbers in lst_data
    '''

    med = None

    # Length of the data
    length = len(lst_data)
    
    if length % 2 == 0:
        index = int(length / 2) - 1
        first_center = lst_data[index]
        second_center = lst_data[index + 1]
        med = (first_center + second_center) / 2
    else:
        index = int(length / 2)

        med = lst_data[index]

    return med

lst_data = [num for num in range(1, 11)]
print(lst_data)

median_value = median(lst_data)
print('Median', median_value)

lst_odd_filter = sorted([num for num in lst_data if num %2 != 0], reverse=True)
print(lst_odd_filter)