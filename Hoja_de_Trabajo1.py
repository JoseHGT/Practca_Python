# Python 3: Hoja de trabajo 0
peso = input ("¿Cuál es su peso en Kg?")
estatura = input ("¿Cuál es su estaruta en metros?")

#Para calcular IMC = peso/(estatura*estarura)
imc= round(float (peso)/float (estatura)**2,2 )
print(" Su indice de masa corporal es: IMC =",imc)
