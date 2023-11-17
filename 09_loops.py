###  Loops  ###

# tambien llamadso bucles, ciclos, etc.

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:   #  Es opcional
    print("Mi condicio  es mayo o igual a 10")


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecucion")
        break
    print(my_condition)

print("se termino el Loop, continua ejecucion")


# FOR
print("Inicia FOR")

my_lyst = [35,24,62,52, 30,30,17]

for element in my_lyst:    #  element en los ejemplos son una vble cualquiera
    print(element)

    my_tuple = (35, 1.77, "Willmark", "Jimenez")
for element in my_tuple:
    print(element)

    my_set  = {"Juan", "Pedro", 35}
for element in my_set:
    print(element)

    my_dict = {
    "nombre":"Willmark", 
    "Apellido":"Jimenez", 
    "edad":52, 
    "Lenguajes":{"Python","Swift","Kotlin"},
    1:1.72
}
for element in my_dict:
    print(element)
    if element == "edad":
        break   #  Termina el ciclo FOR y continua el codigo

for element in my_dict:
    print(element)
    if element == "edad":
        continue   # para la iteracion y vuelve al for
    print("Se muestra")   # cuando tiene un Continue no se muestra estra instruccion


for element in my_dict.values():
    print(element)
else:
    print("EL bucle FOR ha finalizado")
