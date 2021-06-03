import re


def collect_links(string):
    return  re.findall(r'<a href="(.*)">', string)
    # Geeft een lijst terug met alle regexen die worden gevonden
    # Findall kijkt naar de haakjes (capturing), dus zal enkel dat geven wat in de haakjes staat
    # Vaak voorkomend is dat we de haakjes zetten om er een * of + achter te zetten
    # vb. (\.[a-zA-Z]+)*
    # Probleem is dat findall dit zal zien als een capturing
    # Oplossing = (?:\.[a-zA-Z]+)* --> ?:
    # Zo zeggen we aan python da het geen capturing group is
