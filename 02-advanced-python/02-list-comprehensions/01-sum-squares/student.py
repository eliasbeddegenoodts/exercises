def sum_squares(ns):
    squares =  [n ** 2 for n in ns]
    teller = 0
    for i in range(len(squares)):
        teller += squares[i]
    return teller

def sum_squares2(ns):
    return sum([i ** 2 for i in ns ])