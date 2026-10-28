def is_armstrong_number(number):
    digits = str(number)
    power = len(digits)
    total = 0

    for digit in digits:
        value = int(digit)
        total += value ** power

    return total == number
