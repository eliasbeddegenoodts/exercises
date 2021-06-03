def includes(xs, ys):
    if all(item in xs for item in ys):
        return True
    return False

def includes(xs, ys):
    for y in ys:
        if y not in xs:
            return False

    return True