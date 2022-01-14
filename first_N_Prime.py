def is_prime(num):
    if (num < 2):
        return False
    for i in range(2, num):
        if (num % i == 0):
            return False

    return True

def first_n_primes(n):
    result = []
    num = 2
    if n == 0:
        return result
    while len(result) < n:
        if is_prime(num):
            result.append(num)
        num += 1
    return result

def sum_of_n_primes(n):
    arr = first_n_primes(n)
    result = 0
    if len(arr) == 0:
        return 0
    for number in arr:
        result += number 

    return result

print(sum_of_n_primes(4))