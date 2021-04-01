# Largest prime factor
import math

def verifyNumberPrime(number):
    prime = True
    for i in range(2, int(math.sqrt(number))):
        if(number % i == 0):
            prime = False
            break

    return prime


number_final = 600851475143;
largest_factor = 1;

for i in range(2, int(math.sqrt(number_final))):
    if(number_final % i == 0 and i > largest_factor):
        if(verifyNumberPrime(i) == True):
            largest_factor = i;

print('Maior fator primo de ' +str(number_final)+ ' é: ' +str(largest_factor));