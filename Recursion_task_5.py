def sum_of_digits(digit_string: str) -> int:
    if not digit_string.isdigit():
        raise ValueError("Must be digit string")
    if len(digit_string) == 1:
        return int(digit_string)
    return int(digit_string[0]) + sum_of_digits(digit_string[1:])


print(sum_of_digits('26'))
try:
    print(sum_of_digits('test'))
except ValueError as e:
    print(e)
