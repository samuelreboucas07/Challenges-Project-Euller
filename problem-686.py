# Powers of Two
#Demora pq o objectivo é grande, e foi implementado em força bruta.
#Não avlidado para o pior caso, muito lento
prefix = 123
order_position = 678910
numbers_accept = 0
number_potential = 0

while numbers_accept != order_position:
    print(numbers_accept)
    number_potential += 1
    data = str(2 ** number_potential)[0:3];
    if(len(data) >= 3):
        if(int(data[0:3]) == prefix):
            numbers_accept += 1

print(number_potential)