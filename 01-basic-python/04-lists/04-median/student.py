def median(ns):
    ns = sorted(ns)
    #ns.sort() is fout
    if (len(ns) % 2 == 0):
        # [a, b, c, d, e, f]
        # len(ns) = 6
        return (ns[len(ns)//2-1]+ns[len(ns)//2])/2
        #ns[3-1] = ns[2] = c 

    else:
        return ns[len(ns)//2]