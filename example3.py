def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers():
    primes = [num for num in range(1, 1001) if is_prime(num)]
    return primes

def is_perfect(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

def perfect_numbers():
    perfects = [num for num in range(1, 1001) if is_perfect(num)]
    return perfects

def print_numbers(numbers, label):
    print(f"{label} numbers:")
    print(numbers)

def perfect_decorator(func):
    def wrapper():
        perfects = perfect_numbers()
        print_numbers(perfects, "Perfect")
        func()
    return wrapper

@perfect_decorator
def print_primes():
    primes = prime_numbers()
    print_numbers(primes, "Prime")

# Asal sayıları yazdır
print_primes()
