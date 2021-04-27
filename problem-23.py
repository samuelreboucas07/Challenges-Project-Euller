#Non-abundant sums
#Complexidade grande, resolução lenta demais.

limit = 28123
sum_not_abundant = 0

def defineListAbundants():
    abundants = []
    for i in range(1, limit+1):
        sum_divisors = 0
        for j in range(1, i):
            if(i % j == 0):
                sum_divisors += j
            
        if(sum_divisors > i):
            abundants.append(i)
    return abundants

def generateListSuAbundants(list_abundants):
    sum_abundants = []
    for i in range(0, len(list_abundants)):
        for j in range(i, len(list_abundants)):
            value = list_abundants[i]+list_abundants[j]
            if((value > limit)):
                break    
            else:
                sum_abundants.append(value)
    return sum_abundants

print('Criando lista de números abundantes...')
list_abundants = defineListAbundants()

print('Criando lista de somas dos números abundantes...')
list_sum_abundants = generateListSuAbundants(list_abundants)

print('Verificando números que faltam')
for i in range(1, limit):
    if(i not in list_sum_abundants):
        sum_not_abundant += i

print(sum_not_abundant)