########################################################################################
#  TRY
########################################################################################
#
#  
#  
#
#   
#      
#       
#########################################################################################




numero1 = 100
numero2 = 0

print("inicio")

try:
    raise ValueError("Mi error")
    f = open('myfile.txt')
    print(numero1 / numero2)
except ZeroDivisionError:              #Tengo que conocer el tipo de Error
    print("Error al dividir entre 0")
except FileNotFoundError:
    print("Fichero no encontrado")
except Exception as err:
    print("Error.")
    print(err)
else:                                  #Este sobra
    print("La division se calcula correctamente.")
finally:
    print("Fin del Programa.")

print("Fin")