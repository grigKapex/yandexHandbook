'''Яндекс пишет, что решено не правильно, но разница в том, что они спускаются до 0, а я 
до последнего значащего разряда числа'''
def recursive_sum(number):
    if len(str(number)) == 1:
        return number
    else:
        return (number % 10) + recursive_sum(number // 10)