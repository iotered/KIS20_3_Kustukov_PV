import string


def count_digits(line: str) -> int:
    assert isinstance(line, str)
    total = 0
    for char in line:
        if char in string.digits:
            total += 1
    return total
