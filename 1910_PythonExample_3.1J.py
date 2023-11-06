listOfText = []
fullText = ''
while (one := input('?_')) != 'ФИНИШ':
    listOfText.append(''.join(one.lower().split()))
for i in listOfText:
    fullText = fullText + i
print(f'fullText:{fullText}')
maxLetter = fullText[0]
maxCount = 0
for letter in fullText:
    tempMax = fullText.count(letter)
    if maxCount < tempMax:
        maxCount = tempMax
        maxLetter = letter
print(maxLetter)