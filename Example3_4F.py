from itertools import product

oneSuite = input()
itemCard = [ind for ind in range(2, 11)] + ['валет', 'дама', 'король', 'туз']
cardSuite = ['пик', 'треф', 'бубен', 'червей']
values = list(product(itemCard, cardSuite))
for id, item in values:
    if item != oneSuite:
        print(f'{id} {item}')