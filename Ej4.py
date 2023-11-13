# Lista inicial
lista_inicial = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']

# Lista de elementos a borrar
elementos_a_borrar = ['amarillo', 'café', 'blanco']

# Eliminar elementos indicados usando funciones lambda
lista_resultante = list(filter(lambda x: x not in elementos_a_borrar, lista_inicial))

# Imprimir la lista resultante
print(lista_resultante)
