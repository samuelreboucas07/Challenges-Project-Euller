# Multiples of 3 and 5

factor_3, factor_5 = 3, 5
limit_inferior, limit_upper = 3, 1000

sum_multiples = 0

for number in range(limit_inferior, limit_upper):
    if( (number % factor_3 == 0) or (number % factor_5 == 0)):
        sum_multiples += number

print('A soma dos números múltiplos de 3 ou 5 abaixo de 1000 é: ' + str(sum_multiples))