###  Tuples  ###
# Tupla es un conjunto de valores
# Se diferencia con las listas, que no permite la modificacion directa de la data
# Solo tine .count e .index como funciones, soporta + (une dos conjuntos de dato)


my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Willmark", "Jimenez")
my_other_tuple = (35, 52, 30, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Willmark"))
print(my_tuple.index("Jimenez"))

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# para cambiar una Tuple, se debe transmormar a List, modificar y regresar a Tuple

my_tuple =list(my_tuple)
print(type(my_tuple))
# aca ya se puede hacer todo de las listas

my_tuple = tuple(my_tuple)
print(type(my_tuple))


del my_tuple  #  OJO no borra la data, elimina la Tuple
# print(my_tuple)  da error por que ya no existe

      