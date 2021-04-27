#Smallest multiple

#A resolução ficou mais rápida pq das propriedades
smallest_divisible = 11 #propriedade matemática
upper_divisible = 20

#O número tbm deverá ser divisível entre 1 e 10, logo podemos iniciar a partir de 2520 e somar o mesmo valor para adiantar o processo.
i = 2520

while(True):
    cont = 0
    for j in range(smallest_divisible, upper_divisible+1):
        if(i%j == 0):
            cont += 1
        else:
            break
    if(cont == 10):
        break
    i += 2520

print(i)

