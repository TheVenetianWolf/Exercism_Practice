"""Module providing a function to calculate grains on a chessboard"""

def square(number):
    """Function that calculates grain on individual squares."""
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    exponent = number - 1
    return 2 ** exponent

def total():
    """Function to calculate the total number of grains."""
    grains = 0

    for number in range(1, 65):
        grains += square(number)
        
    return grains
