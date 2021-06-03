def divisors(n):
    return [ k for k in range(1, n + 1) if n % k == 0 ]
    # in range(1, n+1)
    # Stel n = 5, dan in range 1 tot 6, dus 1 tot en met 5