import itertools

foods = [input('?_').split(", ")for ind in range(3)]
goods = [y for ind in itertools.chain(foods) for y in ind]
goods.sort()
for value in itertools.count(0, 1):
    if value < len(goods):
        print(f'{value + 1}. {goods[value]}')
    else:
        break