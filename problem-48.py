# Self powers

sum_factors = 0

limit = 1000

for i in range(1, limit+1):
    sum_factors += i**i

digits_number = str(sum_factors)

result = digits_number[len(digits_number)-10: len(digits_number)]

print('últimos 10 items da série calculada é: '+ str(result))