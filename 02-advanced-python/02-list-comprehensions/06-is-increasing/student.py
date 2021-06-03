def is_increasing(ns):
    return all( [ x <= y for x, y in zip(ns, ns[1:]) ] )

# The all() function returns True if all items in an iterable are true
# The zip() function returns a zip object, which is an iterator 
# of tuples where the first item in each passed iterator is 
# paired together, and then the second item in each passed 
# iterator are paired together etc.

def is_increasing(ns):
    for (x, y) in zip(ns, ns[1:]):
        if x > y:
            return False
    return True