def recursive_sum(*numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[-1] + recursive_sum(*numbers[:-1])