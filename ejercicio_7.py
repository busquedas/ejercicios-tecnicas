#Crear una calculadora. El usuario deberá ingresar un valor, luego una operación
#(1 para sumar, 2 para restar, 3 para dividir, 4 para multiplicar)
#y un segundo valor para completar el calculo. El sistema deberá mostrar el resultado.

valor = input ("ingrese un valor: " + str ())
valor = float (valor)
opcion = input ("1 para sumar, 2 para restar, 3 para dividir, 4 para multiplicar: " + str ())
opcion = int (opcion)
sumar = 1
restar = 2
dividir = 3
multiplicar = 4
segundo_valor = input ("ingrese segundo valor: " + str ())
segundo_valor = float (segundo_valor)
if (opcion == 1):
    valor_total_suma = float (valor + segundo_valor)
    print (valor_total_suma)
elif (opcion == 2):
    valor_total_resta = float (valor - segundo_valor)
    print (valor_total_resta)
elif (opcion == 3):
    valor_total_dividir = float (valor / segundo_valor)
    print (valor_total_dividir)
elif (opcion ==4):
    valor_total_multiplicar = float (valor * segundo_valor)
    print (valor_total_multiplicar)
