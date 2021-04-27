#Concealed Square
import math

def verify(number):
    number_str = str(number)
    if(len(number_str) != 19):
        return False
    else:
        number_check = number_str[::2]
        if(number_check == "1234567890"):
            return number_check

smaller_number = int(math.sqrt(1020304050607080900)/10)
upper_number = int(math.sqrt(19293949596979899900)/10)

result = 0

for i in range(smaller_number, upper_number+1, 2):
    data = i * 10
    # print(data)
    if(verify(data**2)):
        result = data
        break

print(result)