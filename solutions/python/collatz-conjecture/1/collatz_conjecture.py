def steps(number):
    steps_counter = 0

    if number == 0 or number < 0:
        raise ValueError("Only positive integers are allowed")
    
    # loop until number reaches 0
    while number != 1:

        if number % 2 == 0:
            number = number // 2
            steps_counter += 1

        elif number % 2 == 1:
            number = 3 * (number) + 1
            steps_counter += 1

    return steps_counter
            
