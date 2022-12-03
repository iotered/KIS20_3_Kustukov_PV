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


if __name__ == '__main__':
    example = "03.12.2022: testing..."
    print(f"Test string: '{example}'\nDigits: {count_digits(example)}")
