# Counting summations

limit = 100
list_numbers = [1] + [0]*limit

for i in range(1, limit):
    for j in range(i, limit+1):
        list_numbers[j] += list_numbers[j - i]

print(list_numbers[len(list_numbers) - 1])