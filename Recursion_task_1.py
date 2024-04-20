from typing import Union


def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    if exp < 0:
        raise ValueError("Works only with exp >= 0.")
    if exp == 0:
        return 1
    if exp == 1:
        return x
    return x * to_power(x, exp - 1)


print(to_power(2, 3))
print(to_power(3.5, 2))
try:
    print(to_power(2, -1))

except ValueError as e:

    print(e)
