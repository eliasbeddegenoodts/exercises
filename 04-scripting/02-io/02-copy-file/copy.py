import sys

with open(sys.argv[1], 'r') as readFile:
    with open(sys.argv[2], 'w') as writeFile:
        writeFile.write(readFile.read())
        # writeFile.writelines(readFile.read()) verschil?
