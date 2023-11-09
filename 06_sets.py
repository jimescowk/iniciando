###  Sets ####
#  Un set no es una estructura ordenada
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))   # Inicialmente es un diccionario

my_other_set = {"Willmark", "Jimenez", 52}
print(my_other_set)
print(type(my_other_set))

print(len(my_other_set))
my_other_set.add("Innkua")
print(my_other_set)

my_other_set.add("Innkua") # Un set no admite repetidos
print(my_other_set)

print("Willmark" in my_other_set)
print("Juan" in my_other_set)

my_other_set.remove("Jimenez")
print(my_other_set)

my_other_set.clear()  # limpia la data  del set  # con del borramos el Set
print(my_other_set)
# como convertir un Set a lista
my_set  = {"Juan", "Pedro", 35}
my_list = list(my_set)   # Es muy peligroso por que no se conoce el orden de la data, para minipularla
print(my_list)

my_other_set = {"Kotklin", "Swit", "Python"}

#my_new_set = set()
my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union({"JavaScript", "C#"})) # solo se le puede adicionar data distinta, no duplica data

print(my_new_set.difference(my_set))






