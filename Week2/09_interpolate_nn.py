# Section 9: Interpolation for List (Time-series)

from _09_search_none import search_first_none

def interpolate_nn(lst_data):
    '''Interpolate nearest neighbor for None values in lst_data
    
    Args:
        lst_data: data to interpolate
        
    Returns:
        lst_data: list of data filled with nearest neighbors
    '''

    for _ in range(len(lst_data)):
        none_position = search_first_none(lst_data)
        
        # Case: None is not in the list
        if none_position == -1:
            return lst_data
        
        begin = none_position - 1
        # end = search_end(lst_data, none_position)
        

        lst_data[none_position] = lst_data[begin]

    return lst_data



lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]


print(interpolate_nn(lst_data))
print(interpolate_nn([1, 1.1, None, 1.4, None, 1.5, None, 2.0, None]))