# Sum square difference

def square(number):
    return number ** 2


limit = 100
sum = 0
sum_squares = 0

for i in range(0, limit+1):
    sum_squares += square(i)
    sum += i

difference = (sum**2) - sum_squares
print('Diferença entre a soma dos quadrado e o quadrado da soma é: '+str(difference))
    