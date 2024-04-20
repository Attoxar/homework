def reverse(input_str: str) -> str:
    if len(input_str) <= 1:
        return input_str
    return input_str[-1] + reverse(input_str[:-1])


print(reverse("hello"))
print(reverse("o"))
