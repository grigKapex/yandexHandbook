import itertools

N = int(input(''))

foods = [input('').split(", ")for ind in range(N)]
goods = [y for ind in itertools.chain(foods) for y in ind]
goods.sort()
menu = list(itertools.permutations(goods, 3))
for ind in menu:
    print(f'{ind[0]} {ind[1]} {ind[2]}')