###  STRINGS ###

my_string = "Mi String"

print(my_string)

my_new_line_string = " Este es un salto \n de linea"
print(my_new_line_string)


my_tab_string = "\t Este es un string con tabulacion"
print(my_tab_string)


#Formateo

name, surname, age ="Willmark", "Jimenez", 52

print("Mi nombre es {} {}, y mi edad es {}".format(name,surname,age))
print("Mi nombre es %s %s, y mi edad es %d" %(name,surname,age))
print("mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname}, y mi edad es {age}")


# Desempaquedato de caracteres

language= "python"
a, b ,c ,d ,e ,f = language
print(a)
print(e)

# Division caracteres

language_slice= language[1:3]
print(language_slice)

language_slice= language[1:]
print(language_slice)

language_slice= language[-2]
print(language_slice)

language_slice= language[0:6:2]
print(language_slice)

# reverse
language_slice= language[::-2]
print(language_slice)


# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print(language.lower())
print(language.isupper())
print(language.startswith("py"))