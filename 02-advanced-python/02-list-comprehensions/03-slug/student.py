def slug(name):
    parts = name.split(' ')
    first_name = parts[0]
    last_name = parts[1:]

    return '-'.join(element.lower() for element in last_name + [first_name])
    # we zetten first name tussen vierkante haken omdat we anders niet kunnen concatenaren
    # can only concatenate list (not "str") to list
    #First name is een string
    #Last_name is een list omdat we hier aan slicing doen
