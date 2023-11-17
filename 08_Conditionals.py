### Conditionals ###

my_condition = False

if my_condition: # Si es True se ejecuta
    print("se ejecuta la condicion del if")

my_condition = 5 * 5
if my_condition >10: # Si es cierto
    print("se ejecuta la condicion del if")
else:
    print("Es menor o igual a 10")


if my_condition >10 and my_condition < 20:
    print("se ejecuta la condicion del if")
elif my_condition == 25:   # segunda validacion de algo especifico
    print("Es igual a 25")

else:
    print("Es menor o igual a 10 o >= que 20 y distinto de 25")

    
print("La ejecucion continua")


my_string = "Mi cadena de texto"

if my_string:
    print("Mi cadena de texto no es vacia")

if my_string == "Micadena de textooooo":
    print("Estas cadenas de texto coinciden")

    


