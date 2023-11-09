### Dictionaries ###
# Un dictionary es un tipo de estructura donde se almacenan datos de tipo "Keys" clabe:valor y el valor puede ser un Set

my_dict =  dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"nombre":"Willmark", "Apellido":"Jimenez", "edad":52, 1:"Python"}

my_dict = {
    "nombre":"Willmark", 
    "Apellido":"Jimenez", 
    "edad":52, 
    "Lenguajes":{"Python","Swift","Kotlin"},
    1:1.72
}
print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))  # da 5 por que solo cuantas las claves, no importa cantidad de data


print(my_dict["nombre"])
my_dict["nombre"] = "Pedro"
print(my_dict["nombre"])

print(my_dict[1])

# para agregar una clabe al dict

my_dict["Calle"] = "La Inferior"
print(my_dict)

del my_dict["Calle"]  #  del permite borrar un dato especificado
print(my_dict)


# print("Willmark" in my_dict)  No se busca la data, se busca la clabe
print("Juan" in my_dict)
print("Apellido" in my_dict)


print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys(("nombre",1)))

my_new_dict = dict.fromkeys(my_dict)   # para crear un nuevo dictionary en blanco, solo clabes
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "Jimenez")   # no se puede pasarle data y clabe a la vez, pone la data igual para todas las clabes
print(my_new_dict)





