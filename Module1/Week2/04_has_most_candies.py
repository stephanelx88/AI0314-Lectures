def has_most_candies(candy_lst, extra_candies=3) -> list[bool]:
    '''Checks if the number of candies of each person has plus
    extra candies exceeds the max number of candies all people have.
    
    Args:
        candy_lst: list of candies each person has
        extra_candy: number of extra candies

    Returns:
        result: list of boolean values
    '''

    max_candies = max(candy_lst)
    
    result = [True if n_candies + extra_candies >= max_candies else False\
               for n_candies in candy_lst]
    
    return result



print(has_most_candies([2, 3, 5, 1, 3], extra_candies=3))
print(has_most_candies([4, 2, 1, 1, 2], extra_candies=1))
print(has_most_candies([12 , 1, 12], extra_candies=10))