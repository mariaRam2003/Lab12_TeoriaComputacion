# Lista de diccionarios
D = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
     {'make': 'Apple', 'model': 2, 'color': 'Silver'},
     {'make': 'Huawei', 'model': 50, 'color': 'Gold'},
     {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

# Otro diccionario para probar
# D = [{'make': 'Toyota', 'model': 'Camry', 'year': 2022},
#      {'make': 'Honda', 'model': 'Civic', 'year': 2021},
#      {'make': 'Ford', 'model': 'Mustang', 'year': 2023},
#      {'make': 'Chevrolet', 'model': 'Malibu', 'year': 2020}]

# Clave para ordenar la lista de diccionarios
key_to_sort = 'make'

# otra clave para probar
# key_to_sort = 'year'


# Ordenar la lista de diccionarios con respecto a la clave indicada
D.sort(key=lambda x: x[key_to_sort])

# Imprimir la lista ordenada
for item in D:
    print(item)
