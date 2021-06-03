import sys
import re


def remove_comments(filename):
    with open(filename, 'r') as r:
        content = r.read()
    contents = re.sub(r'#.*', '', content, flags=re.MULTILINE)

    with open(filename, 'w') as w:
        w.write(contents)


for file in sys.argv[1:]:
    remove_comments(file)
