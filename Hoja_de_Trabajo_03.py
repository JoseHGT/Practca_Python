#HOJA DE TRABAJO 3, EJERCICIO 1.
print()
Contraseña = input("Ingrese la contraseña a Guardar: ")
Validacion = input("Ingrese nuevamente la contraseña para validar: ")
if Validacion == Contraseña:
    print("Contraseña ingresada satisfactoriamente")
else:
    print("La contraseña  ingresada es incorrecta" )
print ("Fin Ejercicio 1")
print ()

#HOJA DE TRABAJO 3, EJERCICIO 2.
#asignacion de grupos segun la letra inicial de su nombre
Nombre= input("Ingrese su primer nombre: ")
Genero= input("Ingrese el sexo al que pertenece (M 0 F): ")
if Genero == "F":
    if Nombre <= "M":
        grupo = "A"
    else:
        grupo = "B"
else:
    if Genero == "M":
        if Nombre >="N":
            grupo = "A"
        else:
            Nombre < "N"
            grupo = "B"
print("Tu grupo es:" + grupo)
print ("Fin Ejercicio 2")
print ()