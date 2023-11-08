def gcd(*numbers):
    delitels = list()
    flag = None
    for i in range(1, min(numbers) + 1):
        for number in numbers:
            if number % i == 0:
                flag = i
            else:
                flag = None
                break
        if flag is not None:
            delitels.append(flag)
        flag = None
    return max(delitels)