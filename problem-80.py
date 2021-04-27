# Square root digital expansion
import math
from decimal import Decimal, localcontext

limit = 100
total = 0

for i in range(1, limit+1):
    with localcontext() as ctx: #Trava o contexto atual em 100 casas decimais de precisão
        ctx.prec = 110 #minimizando o efeito do arredondamento

        digit_integer = str(Decimal(i).sqrt())[0]
        digits_decimal = list(str(Decimal(i).sqrt())[2:101])

        if(len(digits_decimal) > 0):
            for j in digits_decimal:
                total += int(j)
                
            total += int(digit_integer)
print(total)