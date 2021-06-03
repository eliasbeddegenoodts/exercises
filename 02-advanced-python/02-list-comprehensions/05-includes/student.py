def includes(xs, ys):
    if all(x in xs for x in ys):
        return True
    return False