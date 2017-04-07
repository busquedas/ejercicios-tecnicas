#Pedir al usuario que ingrese 10 números, almacenarlos en un array y
#mostrarlos en pantalla al finalizar la carga.

usuario = 0
numeros = int ()
lista_numeros = []
while (usuario < 10):
    usuario = usuario +1
    numeros = input ("ingrese número: ")
    lista_numeros.append (numeros)
print (lista_numeros)
