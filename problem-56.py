# Powerful digit sum

limit = 100

number = 0
power_number = 0
result = 0

for i in range(limit, number, -1):
    sum_digits = 0
    for j in range(limit, number, -1):
        data = i ** j
        list_digits = list(str(data))
        list_digits_int = [int(k) for k in list_digits]
        sum_digits = sum(list_digits_int)
        if(sum_digits > result or result == 0):
            result = sum_digits

print(result)