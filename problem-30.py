# Digit fifth powers

upper_limit = 6 * 9**5
numbers_result = []

for i in range(10, upper_limit):
    digits = list(str(i))
    sum_pot = 0
    
    for j in digits:
        sum_pot += int(j)**5
    
    if(sum_pot == i):
        numbers_result.append(i)

print('Digit fifth powers: ' + str(numbers_result))

print('Resultado da soma dos números é: ' + str(sum(numbers_result)))