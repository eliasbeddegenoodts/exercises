import re


def ababa(string):
    return re.fullmatch(r'(.+)(.+)\1\2\1', string)
    # ababa --> eerste haakjes is a, 2de = b dus 
    # dan a + b + a(want \1) dan terug b (want \2) 
    # en nog eens a 