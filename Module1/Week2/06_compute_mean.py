# Section 6: Comnputing mean for a list of numbers

def mean(lst_data: list) -> float:
    '''Computes the mean of a list of numbers in lst_data
    
    Args:
        lst_data: A list of numbers

    Returns:
        mean_value: The mean value of the list of numbers
    '''

    total = 0

    for num in lst_data:
        total += num

    mean_value = total / len(lst_data)

    return mean_value


lst_data = [i for i in range(1, 11)]
# print(lst_data)

odds = [i for i in lst_data if i % 2 != 0]
evens = [i for i in lst_data if i % 2 == 0]

print(f"Odds: {odds}")
print(f"\tMean for odd numbers: {mean(odds)}")
print(f"Evens: {evens}")
print(f"\tMean for even numbers: {mean(evens)}")

print(f'\nWhole lst_data: {lst_data}')
print(f"\tMean: {mean(lst_data)}")
print(f"\tMedian: {median(lst_data)}")