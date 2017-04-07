#Calcular el promedio de 5 notas ingresadas (notas del 1 al 10).
#Si el promedio es mayor a 7, aprobó la materia, sino reprobó.
ingresar_notas = 0
notas = int ()
while (ingresar_notas < 5):
    ingresar_notas = ingresar_notas +1
    notas = input ("ingresar nota: " )
    notas = int (notas)
    notas_totales = notas + notas + notas + notas + notas
    notas_promedio = int (notas_totales) /5
print ("el promedio es: " + str (notas_promedio))
if (notas_promedio >= 7):
    print ("aprobó la materia... FELICITACIONES")
else:
    print ("reprobó... i´m sorry")
