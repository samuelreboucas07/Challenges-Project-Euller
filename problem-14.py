#Longest Collatz sequence

limit = 1000000
size_sequencia_total = 0
result = 0

for i in range(1, limit):
    factor = i
    sequence = 1
    while(factor != 1):
        if(factor % 2 == 0):
            factor = int(factor / 2)
        else:
            factor = int(3*factor + 1)
        sequence += 1

    if(sequence > size_sequencia_total):
        size_sequencia_total = sequence
        result = i

print('O número '+str(result)+' produz uma sequência de ' +str(size_sequencia_total)+' números.')