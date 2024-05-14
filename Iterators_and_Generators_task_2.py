def in_range(start, end, step=1):
    result = []
    current = start
    while current < end if step > 0 else current > end:
        result.append(current)
        current += step
    return result


my_range = in_range(1, 10, 2)
print(my_range)
