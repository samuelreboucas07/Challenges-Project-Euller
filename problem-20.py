# Factorial digit sum

limit = 100
factorial = 1
sum_numbers = 0

for i in range (limit, 0, -1):
    factorial *= i

numbers = list(str(factorial))

for number in numbers:
    sum_numbers += int(number)

print('Soma dos dígitos do fatorial de 100: ' + str(sum_numbers))