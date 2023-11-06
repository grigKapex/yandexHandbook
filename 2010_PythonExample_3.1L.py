porridgeList = ('Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая')
num = int(input('?_'))
lengthList = len(porridgeList)
for i in range(num):
    if i >= lengthList:
        ind = i % lengthList
        print(porridgeList[ind])
    else:
        ind = i
        print(porridgeList[ind])