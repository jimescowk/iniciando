###  Functions  ###

def my_function ():
    print("Esto es una funcion")

my_function()

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")

def sum_two_values_with_return (first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(10, 5)
print(my_result)


def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname = "Jimenez", name = "Willmark")

def print_name_with_default (name, surname, alias = "Sin Alisa"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Willmark", "Jimenez")
print_name_with_default("Willmark", "Jimenez", "Willy")

def print_texts(*texts):
   for text in texts:
    print(text.upper())

print_texts("Hola", "Paython", "Willmark")
print_texts("Todo Sale")




