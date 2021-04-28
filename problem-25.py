#1000-digit Fibonacci number

fibonacci = [1, 1]
result = 0

while(result == 0):
    next_item = fibonacci[len(fibonacci) - 1 ] + fibonacci[len(fibonacci) - 2 ]
    fibonacci.append(next_item);
    amount_digits = len(list(str(next_item)))
    if(amount_digits == 1000):
        result = len(fibonacci)

print(result)