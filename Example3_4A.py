import itertools

goods = input('?_').split(" ")
for value in itertools.count():
    if value < len(goods):
        print(f'{value + 1}. {goods[value]}')
    else:
        break