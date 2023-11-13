# Matriz X
X = [[1, 2, 3, 4],
     [4, 5, 6, 0],
     [7, 8, 9, -1]]

# Calcular la matriz transpuesta XT usando funciones lambda
XT = list(map(lambda *row: list(row), *X))

# Imprimir la matriz transpuesta
for row in XT:
    print(row)
