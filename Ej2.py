# Lista de enteros
lista_enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Potencia n
n = 3

# Calcular la potencia n-ésima de cada elemento en la lista
resultado = list(map(lambda x: x ** n, lista_enteros))

# Imprimir el resultado
print(resultado)


# Otra lista de enteros para probar
# Lista de enteros
otra_lista_enteros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Potencia n
otro_n = 2

# Calcular la potencia n-ésima de cada elemento en la otra lista
otro_resultado = list(map(lambda x: x ** otro_n, otra_lista_enteros))

# Imprimir el resultado
print(otro_resultado)   