numString = input('?_')
numberList = numString.split()
i = 0
while i < len(numberList):
    if not numberList[i].isdigit():
        a = int(numberList[i - 2])
        b = int(numberList[i - 1])
        match numberList[i]:
            case '+':
                c = a + b
            case '-':
                c = a - b
            case '*':
                c = a * b
            case _:
                c = 0
        numberList.insert(i - 2, str(c))
        del numberList[i - 1:i + 2]
        i = 0
    i = i + 1
print(int(numberList[0]))