first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']

posicion_actual = 0

while posicion_actual < len(first_list):
    palabra1 = first_list[posicion_actual]
    palabra2 = second_list[posicion_actual]
    print(palabra1, palabra2)
    posicion_actual += 1 