N = int(input('N_'))
M = int(input('M_'))
children = []
onePorridge = list()
for i in range(N + M):
    children.append(input())
print(f'children: {children}')
porridge = set(children)
print(f'porridge: {porridge}')

if len(porridge) == (len(children) - len(porridge)):
    print("Таких нет")
else:
    for i in porridge:
        if children.count(i) == 1:
            onePorridge.append(i)
print(f'onePorridge before sorting: {onePorridge}')
onePorridge.sort()
print('\n'.join(onePorridge))