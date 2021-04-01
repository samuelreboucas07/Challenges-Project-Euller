# Summation of primes
import math

limit = 2000000
sum = 0

def definedPrime(number):
    prime = True
    for i in range(2, int(math.sqrt(number))+1):
        if(number % i == 0):
            prime = False
            break
    return prime

for i in range(2, limit):
    if(definedPrime(i)):
        sum += i
    
print('Soma de números primos abaixo de '+str(limit)+ ' é: ' +str(sum))