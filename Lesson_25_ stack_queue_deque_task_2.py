def is_balanced(sequence):
    stack = []
    opening = "([{"
    closing = ")]}"
    for char in sequence:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            last_opening = stack.pop()
            if opening.index(last_opening) != closing.index(char):
                return False
    return not stack


if __name__ == "__main__":
    sequence = input("enter symbols here: ")
    if is_balanced(sequence):
        print("Sequence is balanced.")
    else:
        print("<Sequence is not balanced.")

        # tested with () balanced
        # ()) not balanced
        # )( not balanced
        # ([]) balanced
        # ([{}]) balanced
        # ([{]}) not balanced
        # [(){}[]]() balanced
