# 10001st prime
import math

def definedPrime(number):
    prime = True
    for i in range (2, int(math.sqrt(number))+1):
        if(number % i == 0):
            prime = False
            break
    return prime


limit = 10001
position_prime = 0
number = 1

while(position_prime < limit):
    number += 1
    if(definedPrime(number)):
        position_prime += 1


print(number)