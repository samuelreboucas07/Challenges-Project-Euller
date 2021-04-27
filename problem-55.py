#!/usr/bin/python3

#Lychrel numbers

def generateInversal(number):
    number_list = list(str(number));
    number_list.reverse()
    number_reverse = ''.join(number_list)
    return int(number_reverse)


def verifyPalindrome(number):
    number_list = list(str(number))
    size_list = len(number_list)

    if(len(number_list) % 2 == 0):
        fraction_1 = number_list[0 : int(size_list/2)]
        fraction_2 = number_list[int(size_list/2): size_list]
        fraction_2.reverse()
        if(fraction_1 == fraction_2):
            return True
        else:
            return False
    else:
        fraction_1 = number_list[0 : int(size_list/2)]
        fraction_2 = number_list[int(size_list/2)+1: size_list]
        fraction_2.reverse()
        if(fraction_1 == fraction_2):
            return True
        else:
            return False


limit = 10000
start = 47
interations = 50
result = 0


for i in range(start, limit):
    sum_reverse = i
    number_Lychrel = True
    for j in range(0, interations):
        sum_reverse += generateInversal(sum_reverse)
        if(verifyPalindrome(sum_reverse)):
            number_Lychrel = False
            break
    if(number_Lychrel):
        result += 1
        
print(result)