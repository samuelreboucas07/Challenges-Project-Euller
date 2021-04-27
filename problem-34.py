#Digit factorials

def calculateFatorial(number):
    fatorial = 1
    for i in range(number, 0, -1):
        fatorial *= i
    return fatorial

limit_upper = calculateFatorial(9) * 7


result = 0

for j in range(limit_upper, 9, -1):
    digits_number = list(str(j))
    sum_factorial_digits = 0
    for k in digits_number:
        sum_factorial_digits += calculateFatorial(int(k))
    if(sum_factorial_digits == j):
        result += j

print(result)