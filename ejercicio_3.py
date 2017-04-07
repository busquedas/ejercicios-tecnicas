#Diseñar un algoritmo que aplique un descuento del 10% al monto total de una compra si el pago es de contado
monto_total = input ("ingrese monto total: ")
monto_total1 = int (monto_total)
contado = input ("pago contado?: s/n: " )
descuento = int (monto_total1) * 10 /100
descuento_total = monto_total1 - descuento
if (contado == "s"):
    print ("su descuento es de: " + str (descuento))
    print ("su monto total con descuento es de: " + str (descuento_total))
