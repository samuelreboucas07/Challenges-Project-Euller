# Triangular, pentagonal, and hexagonal

def calculateTriangule(number):
    result = (number*(number+1))/2;
    return int(result)

def calculatePentagonal(number):
    result = (number*(3*number - 1))/2
    return int(result)


def calculateHexagonal(number):
    result = number*(2*number -1)
    return int(result)

interator = 143

values_triangle = []
values_pentagonal = []
values_hexagonal = []

number_equal = 0

while(number_equal == 0):
    interator += 1
    values_pentagonal.append(calculatePentagonal(interator))
    values_hexagonal.append(calculateHexagonal(interator))
    number_triangle = calculateTriangule(interator)
    if(number_triangle in values_hexagonal and number_triangle in values_pentagonal):
        number_equal = number_triangle

print(number_equal)
