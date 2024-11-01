#Modulos
import random

#Variables

num_secreto = random.randint(1, 10)

intentos = 5

#ciclo del juego

while intentos > 0:
    numero_usuario = int(input("Adivina el número secreto (entre 1 y 10): "))
    intentos -= 1

    if numero_usuario == num_secreto:
        print("¡Felicidades! Adivinaste el número secreto.")
        break

    elif intentos == 0:
        print("Te has quedado sin intentos.")
        print(f"El número secreto era: {num_secreto}")
    
    else:
        print("El número ingresado no es el número secreto, vuelva a intentarlo.")
