import re


def parse_link(string):
    match = re.match(r'<a href="(.*)">(.*)</a>', string)

    if match:
        link, caption = match.groups()
        return (caption, link)
    else:
        return None