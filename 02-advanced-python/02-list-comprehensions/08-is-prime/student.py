def is_prime(n):
    return all( [ n % k != 0 for k in range(2, n)] ) and n > 1