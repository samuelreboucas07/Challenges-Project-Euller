# Even Fibonacci numbers

limit_upper = 4000000
number_fibonacci = 1
sequence_fibonacci = [1]

sum_even_fibonacci = 0

while (number_fibonacci < limit_upper):
    if(len(sequence_fibonacci) == 1):
        number_fibonacci = sequence_fibonacci[0] + 1
    else:
        size_sequence = len(sequence_fibonacci)
        number_fibonacci = sequence_fibonacci[size_sequence - 1] + sequence_fibonacci[size_sequence - 2] 
    if(number_fibonacci <= limit_upper):
        sequence_fibonacci.append(number_fibonacci)

for element in sequence_fibonacci:
    if(element % 2 == 0):
        sum_even_fibonacci += element

print('A soma dos números pares da sequência de fibonacci menores que 4000000 é: ' +str(sum_even_fibonacci))