#Special Pythagorean triplet

sum = 1000

result = 0

for i in range(1, int(sum/3)):
    for j in range(i+1, int(sum/2)):
        c = sum - i - j
        value = i ** 2 + j ** 2
        if( value == c**2 ):
            result = i * j * c

print(result)