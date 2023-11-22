### Modules   ###

#  son los ficheros o librerias externas que se pueden usar

#  no se pueden importar ficheros que inician por numero, Python no aceta nomenclatura iniciando con numero

import module   # hay que imortar para poder usar funcionea o clases ya generadas en otro fichero

module.sum(5, 3, 1)
module.printValue("Hola Python!")

#  otra forma de importar una funcion especifica

from module import sum, printValue

sum(5, 3, 1)   # no requiere anteponer el nombre del fichero
printValue("Hola Mundo")


import math  # importar modules ya establecidos en Python o descargados de otro lado


print(math.pi)
print(math.pow(2, 8))

from math import pi as PI_VALUE

print(PI_VALUE)



