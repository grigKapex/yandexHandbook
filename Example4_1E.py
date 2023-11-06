def merge(cortage1, cortage2):
    lst_result = list(cortage1 + cortage2)
    for i in range(1, len(lst_result)):
        value = lst_result[i]
        j = i - 1
        while j >= 0 and value < lst_result[j]:
            lst_result[j + 1] = lst_result[j]
            j -= 1
        lst_result[j + 1] = value
    return tuple(lst_result)