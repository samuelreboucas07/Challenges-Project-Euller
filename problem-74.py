# Digit factorial chains
#Força bruta com cache, ainda asim é lento

def calculateFactorial(digit):
    factorial = 1
    for i in range(1, digit+1):
        factorial *= i
    return factorial

def sumFactorialDigits(number):
    total_factorial_digits = 0
    for i in str(number):
        total_factorial_digits += calculateFactorial(int(i))

    return total_factorial_digits

limit = 1000000
factor = 60
result = 0

cache = {
    169: 3,
    363601: 3,
    1454: 3,
    871: 2,
    45361: 2,
    872: 2,
    45362: 2,
}

for i in range(1, limit):
    stack = [i]
    value = i
    while(len(stack) <= factor):
        value = sumFactorialDigits(value)

        if(cache.get(value)):
            if(len(stack) + cache.get(value) == factor):
                result += 1
                break
            else:
                break
        if(value in stack):
            if(len(stack) < factor):
                break;
            elif(len(stack) == factor):
                result += 1
                break

        stack.append(value)

print(result)
    