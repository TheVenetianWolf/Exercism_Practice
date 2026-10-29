def is_valid_triangle(sides):
    a, b, c = sides

    positive = a > 0 and b > 0 and c > 0
    triangle_inequality = (
            a + b >= c
            and a + c >= b
            and b + c >= a
        )
    
    return positive and triangle_inequality
    
def equilateral(sides):
    a, b, c = sides
    return is_valid_triangle(sides) and a == b == c

def isosceles(sides):
    a, b, c = sides
    return is_valid_triangle(sides) and (
        a == b or a == c or b == c
    )

def scalene(sides):
    a, b, c = sides
    return is_valid_triangle(sides) and (
        a != b and a != c and b != c
    )
