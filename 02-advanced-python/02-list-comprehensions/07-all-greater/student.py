def all_greater(ns, ms):
    ns = sorted(ns)
    ms = sorted(ms)

    return all([ x > y for x in ns for y in ms])