def mult(a: int, n: int) -> int:
    if n < 0:
        raise ValueError("It works only with positive integers")
    if n == 0:
        return 0
    if n == 1:
        return a
    return a + mult(a, n - 1)


print(mult(2, 4))
print(mult(2, 0))
try:
    print(mult(2, -4))
except ValueError as e:
    print(e)
    