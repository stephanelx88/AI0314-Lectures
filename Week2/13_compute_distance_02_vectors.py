# Section 13: List and Tuple
import math

# Question 1:

my_tuple1 = (2, 3)
my_tuple2 = (3, 6)

# Sum of 2 vectors
summation_vec = (my_tuple1[0] + my_tuple2[0], my_tuple1[1] + my_tuple2[1])

# Multiplication of vectors
mult_vec = (my_tuple1[0] * my_tuple2[0], my_tuple1[1] * my_tuple2[1])


def compute_distance(a: tuple, b: tuple) -> float:
    """Computes the distance between two vectors
    
    Args:

        a: vector 1
        b: vector 2

    Returns:
        distance: distance between vector a and b
    
    """
    distance = 0
    length = len(a)
    total_diff = 0
    for i in range(length):
        diff = (a[i] - b[i])**2
        total_diff += diff

    distance = math.sqrt(total_diff)

    return distance

print(summation_vec)
print(mult_vec)

print(compute_distance(my_tuple1, my_tuple2))