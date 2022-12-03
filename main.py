import string


def count_digits(line: str) -> int:
    """
    Counts number of ASCII-digits in line

    :param line: string to count digits in
    :return: number of digits
    """
    assert isinstance(line, str)
    total = 0
    for char in line:
        if char in string.digits:
            total += 1
    return total
