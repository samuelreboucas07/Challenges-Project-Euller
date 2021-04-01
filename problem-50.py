# Consecutive prime sum
import math

limit_smallest = 2
limit = 1000000

# Usando propriedade decorrente da teoria dos números que afirma que ou número composto terá um fator multiplativo
# menor ou igual a raiz quadrado dele, caso contrário o número será primo.
# Deste forma diminuo a complexidade ao definir se um número primo de O(n) para O(raiz(n)).
def definedPrime(number):
    prime = True
    for i in range(limit_smallest, int(math.sqrt(number))+1):
        if(number % i == 0):
            prime = False
            break
    return prime

sum_primes = []
interval_larger = 0
result = 0

for i in range (limit_smallest, limit):
    if(definedPrime(i)):
        if(len(sum_primes) == 0):
             sum_primes.append(i)
        else:
           sum_primes.append(sum_primes[len(sum_primes) -1 ] + i)

for i in range(0, len(sum_primes)):
    for j in range(len(sum_primes)-1, 0, -1):
        factor = sum_primes[j] - sum_primes[i]
        if(factor < limit and j-i > interval_larger and factor > 0 and definedPrime(factor) ):
            interval_larger = j - i
            result = factor
            break
    if(j-i < interval_larger):
        break
    
print(result)