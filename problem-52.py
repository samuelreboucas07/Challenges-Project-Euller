# Permuted multiples

def verify_permuted_digits(number, multiple):
    list_number = list(str(number))
    list_permuted_number = list(str(multiple))
    if(set(list_number).symmetric_difference(list_permuted_number)):
        return False
    else:
        return True
    
result = 0
number_permuted = 10
multiple_2 = 0
multiple_3 = 0
multiple_4 = 0
multiple_5 = 0
multiple_6 = 0

while(result == 0):
    multiple_2 = 2 * number_permuted
    multiple_3 = 3 * number_permuted
    multiple_4 = 4 * number_permuted
    multiple_5 = 5 * number_permuted
    multiple_6 = 6 * number_permuted

    if( verify_permuted_digits(number_permuted, multiple_2) and 
        verify_permuted_digits(number_permuted, multiple_3) and 
        verify_permuted_digits(number_permuted, multiple_4) and 
        verify_permuted_digits(number_permuted, multiple_5) and 
        verify_permuted_digits(number_permuted, multiple_6) ):
        result = number_permuted
    
    number_permuted += 1

print('Menor numero positivo que seus múltiplos de 2 - 6 são tem seus dígitos permutados: ' + str(result))
