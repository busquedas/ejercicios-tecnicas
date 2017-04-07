#Diseñar un programa que permita al usuario cotizar valores en dólares y euros.
#Considerando que el dólar esta a $15.60 y el euro a $17.90 ,
#calcular el valor en pesos del monto ingresado por el usuario en la moneda seleccionada.

dolar = 15.60
dolar_actual = float (dolar)
euro = 17.90
euro_actual = float (euro)
print ("calcular dolar a pesos: ingrese 1")
print ("calcular euro a pesos: ingrese 2")
dolar1 = 1
euro1 = 2
seleccion = input ()
if (dolar1):
    ingreso_pesos1 = input ("ingrese cantidad de dólares: ")
    ingreso_pesos11 = float (ingreso_pesos1)
    monto_total = ingreso_pesos11 * dolar_actual
    print ("cantidad de pesos: " + str (monto_total))
    if (euro1):
        ingreso_pesos2 = input ("ingrese cantidad de euros: ")
        ingreso_pesos22 = float (ingreso_pesos2)
        monto_total = ingreso_pesos22 * euro_actual
        print ("cantidad de pesos: " + str (monto_total))

else:
    print ("elija 1 para pasar dólar a pesos, o 2 para pasar euros a pesos")
