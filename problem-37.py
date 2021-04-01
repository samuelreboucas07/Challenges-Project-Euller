# Truncatable primes

import math

def definedPrime(number):
    prime = True
    if(number > 1):
        for i in range(2, int(math.sqrt(number)) + 1):
            if(number % i == 0):
                prime = False
                break
        return prime
    else:
        return False

def definedLeftToRight(number):
    all_digits_primes = True
    list_left_right = []
    prime = str(number)
    while(len(prime) >= 1):
        prime = prime[0: len(prime)-1]
        if(prime):
            list_left_right.append(prime)
    for number in list_left_right:
        if(definedPrime(int(number)) == False):
            all_digits_primes = False
            break
    return all_digits_primes


def definedRightToLeft(number):
    all_digits_primes = True
    list_right_left = []
    prime = str(number)
    while(len(prime) >= 1):
        prime = prime[1: len(prime)]
        if(prime):
            list_right_left.append(prime)
    for number in list_right_left:
        if(definedPrime(int(number)) == False):
            all_digits_primes = False
            break
    return all_digits_primes


sum_truncatable_prime = 0
cont_truncatable_prime = 0
limit_number = 11
cont = 10

while(cont_truncatable_prime < limit_number):
    list_right_left = []
    if(definedPrime(cont)):
        if(definedRightToLeft(cont) and definedLeftToRight(cont)):
            cont_truncatable_prime += 1
            sum_truncatable_prime += cont
        
    cont += 1

print('A soma dos 11 primeiros primos truncáveis ​​é '+str(sum_truncatable_prime))