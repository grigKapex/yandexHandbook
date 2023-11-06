N = int(input('N_'))
child = ''
porridgeName = list()
children = dict()

for i in range(N):
    child = input()
    key = child.split()[0]
    value = child.split()[1:]
    children[key] = value
porridge = input()

for key, value in children.items():
    print(f'[key]={key} valued:{value}')
for name, por in children.items():
    if porridge in por:
        porridgeName.append(name)

if len(porridgeName) == 0:
    print("Таких нет")
else:
    porridgeName.sort()
print('\n'.join(porridgeName))