
cantidad_notas = int(input("¿Cuántas notas deseas ingresar? "))

total_notas = 0
suma_aprobadas = 0
suma_desaprobadas = 0
cantidad_aprobadas = 0
cantidad_desaprobadas = 0


for contador in range(cantidad_notas):
    nota = int(input(f"Ingrese la nota {contador+1}: "))
    total_notas += nota 
    
    if nota >= 70:
        suma_aprobadas += nota
        cantidad_aprobadas += 1
    else:
        suma_desaprobadas += nota
        cantidad_desaprobadas += 1


promedio_total = total_notas / cantidad_notas


if cantidad_aprobadas > 0:
    promedio_aprobadas = suma_aprobadas / cantidad_aprobadas
else:
    promedio_aprobadas = 0 

if cantidad_desaprobadas > 0:
    promedio_desaprobadas = suma_desaprobadas / cantidad_desaprobadas
else:
    promedio_desaprobadas = 0 

print(f"Cantidad de notas aprobadas: {cantidad_aprobadas}")
print(f"Cantidad de notas desaprobadas: {cantidad_desaprobadas}")
print(f"Promedio total de notas: {promedio_total:.2f}")
print(f"Promedio de notas aprobadas: {promedio_aprobadas:.2f}")
print(f"Promedio de notas desaprobadas: {promedio_desaprobadas:.2f}")
