def is_prime(n):
    for i in range(2, n):
        # stel n = 16
        # 16 % 2
        if n % i == 0:
            return False
    return n > 1
