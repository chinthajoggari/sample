import math

def is_strong_number(num):
    """
    Checks if a given number is a strong number.
    A strong number is a number whose sum of the factorial of its digits is equal to the number itself.
    """
    if num < 0:
        return False  # Strong numbers are typically defined for non-negative integers

    original_num = num
    sum_of_factorials = 0

    # Handle the case of 0 separately as math.factorial(0) is 1
    if num == 0:
        return True # 0 is considered a strong number (0! = 1, sum of factorials = 1, not equal to 0)
                    # However, in some contexts, 0 is not considered a strong number.
                    # For this program, we will exclude 0 from the range 1 to 5000.

    while num > 0:
        digit = num % 10
        sum_of_factorials += math.factorial(digit)
        num //= 10

    return sum_of_factorials == original_num

print("Strong numbers from 1 to 5000:")
for i in range(1, 5001):  # Iterate from 1 up to and including 5000
    if is_strong_number(i):
        print(i)