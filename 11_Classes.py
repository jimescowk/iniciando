### Classes   ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())


class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname
 
my_person = Person("Willmark", "Jimenez")
print(f"{my_person.name} {my_person.surname}")


class Person2:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"
        self.__name = name    ###  con .__ queda propiedad privada, no se puede modificar, se puede leer con get_name
       
    def get_name (self):
        return self.__name

    def walk (self):
        print(f"{self.full_name} esta caminando")

my_person2 = Person2("Willmark", "Jimesco")
print(my_person2.full_name)
print(my_person2.get_name())
my_person2.walk()



