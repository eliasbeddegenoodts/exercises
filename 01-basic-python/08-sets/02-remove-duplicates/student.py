def remove_duplicates(xs):
    found = set()
    result = []
    for x in xs:
        if x not in found:
            found.add(x)
            result.append(x)

    return result


# .add is om iets toe te voegen aan een set
#  .append voor iets toe te voegen aan list
        