print("Hola" + " mundo")

##str_int = ("Hola" + 5)
##print(str_int) TypeError: can only concatenate strings (not"inter") to strings.

##int_str = (5 + "Hola")
## print (int_str) TypeError: unsupported operand type(s) for +: 'int' and 'str'

mis_listas = [1, 2, 3, 4] + [8, 7, 6, 5]
print(mis_listas)

##string_list = ("Hola" + [3,6,8,9])
##print(string_list) TypeError: can only concatenate strings (not "list") to strings.

float_int = (3.333 + 5)
print(float_int)

bool_bool = (False + True)
print(bool_bool)

##En Python, los valores booleanos True y False también se interpretan como números enteros cuando se usan en operaciones aritméticas: True se comporta como 1 y False como 0. Entonces, cuando sumas False + True, en realidad estás sumando 0 + 1, lo cual da como resultado 1