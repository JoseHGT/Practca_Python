
# Python 3: Hoja de trabajo 2 Ejercicio 1
print()
n = int(input ("Ejercicio 1, Ingrese un numero entero Positivo, para la altura del triangulo: "))
for k in range(n):
    for l in range (k+1):
        print("*", end="")
    print("")
print ("Fin Ejercicio 1")
print()

# Python 3: Hoja de trabajo 2 Ejercicio 2
n = int(input ("Ejercicio 2, Ingrese un numero entero Positivo: "))

for i in range (n,-1,-1):
    print(i,end=", ")

print("Fin Ejercicio 2")
print()

# Python 3: Hoja de trabajo 2 Ejercicio 3
n = int(input ("Ingrese un número entero mayor que 2:  "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " Es primo")
else:
    print(str(n) + " No es primo")
print ("Fin Ejercicio3")
print()

