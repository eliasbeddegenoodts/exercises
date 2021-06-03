def is_increasing(ns):
    for (x, y) in zip(ns, ns[1:]):
        if x > y:
            return False
    return True

# def is_increasing(ns):
#     for (x, y) in zip(ns, ns[1:]):
#         if x < y:
#             return True
#     return False
# WHY IS THIS NOT WORKING?
# uw eerste geeft true zodra er 1 paar (x,y) is die omhoog gaat
# ge wilt dat alle paren (x,y) omhoog gaan


