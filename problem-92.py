#Square digit chains
#Força bruta, muito lento

def generateProxNumber(number):
    digits = list(str(number))
    result = 0
    for elem in digits:
        result += int(elem)**2
    
    return result

limit = 10000000
result = 0
sequential_loop = False
data = 0
cache = []
sum_max_digits = (9**2)*7

for i in range(1, limit+1):
    sequential_loop = False
    print(i)
    if(i in cache):
        result += 1
    else:
        data = generateProxNumber(i)
        while(not sequential_loop):
            if(data == 89 or data in cache):
                result += 1
                sequential_loop = True
                if(i <= sum_max_digits):
                    cache.append(i)
            if(data == 1):
                sequential_loop = True
            data = generateProxNumber(data)

print(result)