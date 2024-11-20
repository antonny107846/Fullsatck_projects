list_a = ['producto', 'precio', 'disponibilidad']
list_b = ['Laptop', 800, True]


resultado = {}


indice = 0
while indice < len(list_a):
    key = list_a[indice]
    value = list_b[indice]
    resultado[key] = value  
    indice += 1 


print(resultado)