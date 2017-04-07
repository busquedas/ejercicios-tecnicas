#Escribir el algoritmo que, a partir de la cantidad de bancos de un aula y la cantidad de alumnos inscriptos para un curso,
#permita determinar si alcanzan los bancos existentes. De no ser así informar cuantos bancos sería necesario agregar

bancos_aula = 30
alumnos = int (input ("agregue alumnos ingresados: "))
if (alumnos <= 30):
    sobran = bancos_aula - alumnos
    sobran_str = str (sobran)
    print ("sobran bancos: " + sobran_str)
else:
    faltan = alumnos - bancos_aula
    faltan_str = str (faltan)
    print ("faltan bancos: " + faltan_str)
