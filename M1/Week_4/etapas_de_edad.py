#Datos del usuario

nombre = input("Digite su nombre: ")
apellido = input("Digite su apellido: ")

while True:
    try:
        edad = int(input("Digite su edad: "))
        break
    except ValueError:
        print("Edad debe estar en numeros enteros. Por favor vuelva a intentar.")

#Rango de edades

if edad <= 2:
    etapa = "es un bebé"
elif 3 <= edad <= 9:
    etapa = "es un niño"
elif 10 <= edad <= 12:
    etapa = "es un preadolescente"
elif 13 <= edad <= 19:
    etapa = "es un adolescente"
elif 20 <= edad <= 35:
    etapa = "es un adulto joven"
elif 36 <= edad <= 64:
    etapa = "es un adulto"
else:
    etapa = "es un adulto mayor"

print(f"{nombre} {apellido} {etapa}.")
