import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip("\n"))
findWord = lines.pop(-1)
for ind in lines:
    if findWord.lower() in ind.lower():
        print(ind)