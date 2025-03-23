Print_message = "I'm a global variable"

print(f"Original global variable: {Print_message}")


#Intentar accesar variable definida en una funcion desde fuera de la misma.
def local_variable():
    x = "Hola"
    print(f"Local variables aren't accessible from outside {x}")

local_variable()
'''print(x)''' #da error por estar fuera del scope


#editando la variable global
def edit_global_variable():
    global Print_message
    Print_message = "I can be changed at any time"
    print(f"Modified global variable inside anothe varialbe: {Print_message}")

edit_global_variable()




