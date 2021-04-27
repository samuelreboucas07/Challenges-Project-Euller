# Path sum: two ways
# Programação dinâmica

file = open('matrix.txt', 'r')
matriz = []
for line in file:
    line = line.replace('\n', '').split(',')
    line_int = [int(item) for item in line]
    
    matriz.append(line_int)


dimension = len(matriz) - 1
for i in range(dimension, -1, -1):
    for j in range(dimension, -1, -1):
        if( i < dimension and j < dimension):
          matriz[i][j] += min(matriz[i+1][j], matriz[i][j+1])
        elif (i < dimension):
            matriz[i][j] += matriz[i+1][j]
        elif (j < dimension):
            matriz[i][j] += matriz[i][j+1]

print(matriz[0][0])

              
    