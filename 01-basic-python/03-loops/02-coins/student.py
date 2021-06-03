def coins(one, two, five, goal):
    for x in range (0, one+1):
        #in range(0,5) geeft 0 tot en met 4 terug, dus van daar 
        #in range(0, one+1), dan geeft hij effectief de waarde van one terug
        for y in range(0, two+1):
            for z in range(0, five+1):
                if x + 2 * y + 5 * z == goal:
                    return True
    return False
