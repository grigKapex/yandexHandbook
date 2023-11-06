import itertools

N = int(input(''))
foods = [input('')for ind in range(N)]
values = list(itertools.combinations(foods, 2))
for ind in values:
    print(f'{ind[0]} - {ind[1]}')