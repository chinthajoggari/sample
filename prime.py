def is_prime(num):
    """
    Checks if a given number is prime.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    """
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # If divisible by any number other than 1 and itself, it's not prime
    return True  # If no divisors found, it's prime

def print_primes_up_to_n(n):
    """
    Prints all prime numbers from 1 up to a given number n.
    """
    print(f"Prime numbers from 1 to {n}:")
    for number in range(1, n + 1):
        if is_prime(number):
            print(number, end=" ")
    print() # For a new line after printing all primes

# Call the function to print prime numbers up to 100
print_primes_up_to_n(100)