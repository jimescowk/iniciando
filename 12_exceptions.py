###  Exceptions Handling ###

# Manejo de errores #

#   try:
#           se ejecuta codigo
#   except:   (si se produce un error en el codigo anterior)
#           execute this code when exception
#   else:
#           si no hay error, ejecuta este codigo
#   finally:
#           Siempre ejecute este codigo

numberone = 5
numbertwo= 1
numbertwo = "1"

# try except
try:
    print(numberone + numbertwo)
except:                             # se ejecuta si hay un error en el codigo anteior
    print("Se ha producido un error")

# try except else
try:
    print(numberone + numbertwo)
except:
    print("Se ha producido un error")
else:      # opcional                                 # se ejecuta si no hay exception
    print("La ejecucion continua correctamente")
finally:   # opcional                                # se ejecuta siempre
    print("La ejecucion continua")


# Captura de excepciones por tipo
try:
    print(numberone + numbertwo)
    print("NO se ha producido error")
except TypeError:                             # se ejecuta si hay un error en el codigo anteior
    print("Se ha producido un error TypeError")
except ValueError:
    print("Se ha producido un error ValueErrror")

# Captura de excepciones por tipo
try:
    print(numberone + numbertwo)
    print("NO se ha producido error")
#except TypeError:                             # se ejecuta si hay un error en el codigo anteior
   # print("Se ha producido un error TypeError")
except Exception as error:
    print(error)
    print("Se ha producido un error en la data")


