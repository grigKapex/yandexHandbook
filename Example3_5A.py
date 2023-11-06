import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip("\n"))
print(sum([int(j) for ind in lines for j in ind.split(" ")]))