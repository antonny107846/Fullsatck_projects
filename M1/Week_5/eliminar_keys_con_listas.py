list_of_keys = ['precio', 'disponibilidad']
producto = {
    'nombre': 'Celular',
    'marca': 'Samsung',
    'precio': 500,
    'disponibilidad': True
}

nuevo_diccionario = {}

for key in producto:
    if key not in list_of_keys:  
        nuevo_diccionario[key] = producto[key]  

print(nuevo_diccionario)
