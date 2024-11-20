numeros = []
contador = 0

while contador < 10:
    print(f'Por favor, ingrese el número {contador + 1}:')
    numero_ingresado = int(input())
    numeros.append(numero_ingresado)
    contador += 1 

numero_mas_alto = numeros[0]  

for numero in numeros:
    if numero > numero_mas_alto:
        numero_mas_alto = numero

print(f'Los números ingresados fueron: {numeros}')
print(f'El número más alto fue: {numero_mas_alto}')
