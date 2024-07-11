# Check if a number is an Armstrong number

def is_armstrong(num: int) -> int:
    '''Returns 1 if num is an Armstrong number, 0 otherwise

    Args:
        num: The number to be checked

    Returns:
        result: 1 if num is an Armstrong number, Fal0se otherwise
    '''

    # Initialize result
    result = 0
    
    # Convert number to string and split into digits
    num_str = str(num)
    digits = [int(d) for d in num_str]
    
    # Legth of the digits
    n = len(digits)

    # Calulate sum of the digits with the power of n
    total = sum([digit**n for digit in digits])
    
    if total == num:
        result = 1

    return result

def extract_armstrong(lst_data: list) -> list:
    '''Returns a list of Armstrong numbers from the list input
    
    Arg:
        lst_data: input list of numbers

    Returns:
        arm_nums: list of Armstrong numbers
    '''
    arm_nums = [num for num in lst_data if is_armstrong(num)]

    return arm_nums


lst_data = [130 , 270 , 153 , 407 , 177 , 371 , 1000 , 1634 , 370]
print(extract_armstrong(lst_data))