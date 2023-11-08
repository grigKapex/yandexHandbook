#у Яндекса не принимает, т.к. хочет, чтобы передали строку, но не предъявляет тербования к строке
def make_list(length, value=0):
    if isinstance(length, int):
        return [[value for i in range(length)] for j in range(length)]
    if isinstance(length, tuple):
        return [[value for i in range(length[0])] for j in range(length[1])]