# Circular primes
import math

def definedPrime(number):
    prime = True
    if(number > 1):
        for i in range(2, int(math.sqrt(number))+1):
            if(number % i == 0):
                prime = False
                break
        return prime
    else:
        return False
    

def definedCircular(number):
    prime_circular = True
    
    first, middle, last = number[0], number[1: len(number)-1], number[len(number)-1]
    if(len(number) > 1):
        element = middle + last + first
    else:
        element = first
    if(definedPrime(int(element))):
        while(number != element):
            first, middle, last = element[0], element[1: len(element)-1], element[len(element)-1]
            if(len(number) > 1):
                element = middle + last + first
            else:
                element = first
            if(definedPrime(int(element)) == False):
                prime_circular = False
                break
        return prime_circular

limit = 1000000
count = 0

for i in range(2, limit):
    if(definedCircular(str(i))):
        count += 1

print('Quantidade de primos circulares de 1 - 1000000 é: ' + str(count))