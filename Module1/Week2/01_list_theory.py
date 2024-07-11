# Section 2: Theories
# SSection 1:
# Question 1: Create a list of intergers from 1 to 10

first_ten = [num for num in range(1, 11)]




my_lst = [1, 'a', 3]
another_lst = list((3, 3, 'control', 'panel'))

another_lst.append('welcome')
another_lst.insert(1, 'stephane trinh')
another_lst.remove(3)
another_lst.pop(-1)
another_lst[2] = 'long xuyen city'
print(another_lst)


# Exercises

# Create a list of even numbers from 1 to 12
lst_data = [number for number in range(1, 13) if number % 2 == 0]
print('Question 1:', lst_data)
# Remove numbers divisible by three from lst_data

# For loop
for num in lst_data:
    if num % 3 == 0:
        lst_data.remove(num)

# List comprehension
lst_data = [num for num in lst_data if num % 3 != 0]
print('Question 2:', lst_data)


# Append 1, 2, 3 to lst_data
lst_data = lst_data + [1, 2, 3]

lst_data = lst_data[:3] + [6, 7, 8] + lst_data[3:]
print('Question 3|:', lst_data)


# If number in lst_data is divisible by 2 or 5, update it to 0
lst_data = [0 if num % 2 == 0 or num % 5 == 0 else num for num in lst_data]
print('Question 4:', lst_data)
