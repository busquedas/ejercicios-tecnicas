#Diseñar un programa que solicite al operador un usuario. Los posibles nombres de usuario son "admin" y "operador".
#En caso de ser admin, se muestra la leyenda "Bienvenido Administrador", en caso de ser operador, "Bienvenido Operador",
#y en caso de ser otro usuario distinto, se muestra "Usuario desconocido". En caso de que el usuario haya ingresado admin u operador,
#se le solicita la contraseña, sino, se termina la ejecución.
usuario1 = str ("admin")
usuario2 = str ("operador")
password = 1234
menu = input ("escriba su nombre usuario: " )

if (menu == usuario1):
    print ("Bienvenido Administrador")
    input ("escriba password: ")
    if (password == 1234):
        print ("ingreso correcto")
    else:
        print ("ingreso incorrecto")
elif (menu == usuario2):
    print ("Bienvenido Administrador")
    input ("escriba password: ")
    if (password == 1234):
        print ("ingreso correcto")
    else:
        print ("ingreso incorrecto")

else:
    print ("usuario desconocido")
