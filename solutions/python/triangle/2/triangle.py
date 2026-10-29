def is_valid_triangle(sides):
    side_a, side_b, side_c = sides

    positive = side_a > 0 and side_b > 0 and side_c > 0
    triangle_inequality = (
            side_a + side_b >= side_c
            and side_a + side_c >= side_b
            and side_b + side_c >= side_a
        )
    
    return positive and triangle_inequality
    
def equilateral(sides):
    side_a, side_b, side_c = sides
    return is_valid_triangle(sides) and side_a == side_b == side_c

def isosceles(sides):
    side_a, side_b, side_c = sides
    return is_valid_triangle(sides) and (
        side_a == side_b or side_a == side_c or side_b == side_c
    )

def scalene(sides):
    side_a, side_b, side_c = sides
    return is_valid_triangle(sides) and (
        side_a != side_b and side_a != side_c and side_b != side_c
    )
