# Section 8: Algorithms on List

def search_first_none(lst_data: list) -> int:
    '''Search for the first None value in lst_data and return its index
    or return -1 if not found
    
    Args:
        lst_data: list of values to search for None

    Returns:
        result: the index of the first None value, or -1 if not found
    '''

    result = -1

    # Loop through lst_data and search for the first None value
    for index, val in enumerate(lst_data):
        if val is None:
            return index

    return result


def search_all_none(lst_data: list) -> list[int]:
    '''Search for the all None values in lst_data and return its index
    or return a blank list if not found
    
    Args:
        lst_data: list of values to search for None

    Returns:
        result: the index of the first None value, or [] if not found
    '''

    result = []

    # Loop through lst_data and search for the None values
    for index, val in enumerate(lst_data):
        if val is None:
            result.append(index)

    return result

# lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]

# assert search_first_none(lst_data) == 2
# assert search_first_none([1, 2, 3]) == -1

# assert search_all_none(lst_data) == [2, 4, 6]

# print('All unit tests passed!')