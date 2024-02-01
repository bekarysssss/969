def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# Example usage:
input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 16, 23, 123, 22, 34]
prime_numbers = filter_prime(input_numbers)

print(prime_numbers)