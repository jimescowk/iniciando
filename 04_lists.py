### Lists  ###

my_list =  list()
my_other_list = []

print(len(my_list))


my_list = [35, 24,62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

my_other_list = [35, 1.72, "willmark", "jimenez"]
print(type(my_other_list))
print(type(my_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
#print(my_other_list[4])    da error de Index porque solo hay cuatro datos y comienza en posicion 0
#print(my_other_list[-5])   da error de index, por que solo hay 4 datos en la lista

print(my_other_list.count("willmark"))
print(my_list.count(30))

# desempaquetar la lista
age, height, name, surname = my_other_list
print(name)

name, height,age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]

print(name)


print(my_list + my_other_list)  # no funciona -, ni *, ni / : solo suma, por que genera la lista poniendo todos los elementos

my_other_list.append("Innkua")   # añade al final de la lista
print(my_other_list)

my_other_list.insert(1, "Rojo")    # Agrega en la posicion deseada en la lista
my_other_list[1] = "Azul"   # asiganra a una posicion de la lista un dato
print(my_other_list)

my_other_list.remove("Azul")  # remueve el primer elemeto que encuentre de ese item "Azul", sia hay mas azul, solo borra el primero
print(my_other_list)




my_list.pop()   # elimina el ultimo valor de la lista
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()  # Copiamos una lista

my_list.clear()   # con clear borramos toda la lista
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])








