# Largest palindrome product

def verifyPalindrome(number):
    number_str = str(number)
    size_number = len(number_str)

    part_1 = number_str[0: int(size_number/2)]
    
    if(size_number % 2 == 0):
        part_2 = number_str[int(size_number/2): size_number]
        part_2_reversed = ''.join(reversed(part_2))
        
    else:
        part_2 = number_str[int(size_number/2)+1: size_number]
        part_2_reversed = ''.join(reversed(part_2))

    if(part_1 == part_2_reversed):
        return True
    else:
        return False



smaller_number_interval = 100
largest_number_interval = 999

smaller_number_product = smaller_number_interval ** 2

largest_number_palindrome = 0

for i in range (largest_number_interval, smaller_number_interval-1, -1):
    for j in range (largest_number_interval, smaller_number_interval-1, -1):
        product = i*j
        if(verifyPalindrome(product) == True and product > largest_number_palindrome):
            largest_number_palindrome = product



print('O maior número palindrome no referente intervalor é: ' +str(largest_number_palindrome))