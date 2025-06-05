nombre,edad,cedula,dinero_solicitado,numero_de_cuenta = (input(" ingrese su nombre "),int(input("ingrese su edad ")),int(input("ingrese su cedula")),float(input("iingrese el dinero que desea solicitar ")),int(input("ingrese su numero de cuenta ")))
if edad < 18:
    print(f"lo sentimos {nombre} pero no permitimos prestamos a menores de edad, tenga un buen dia ")
else:
    print ("consultando su solicitud denos un momento")
    if dinero_solicitado > 6000000 :
        print ("lo sentimos su solicitud exede su puntaje, su solicitud fue rechazada que tenga un buen dia ")
    elif dinero_solicitado <= 0 :
        print("la opcion solicitada es invalida ")
    else :
        print(f"su prestamo fue aprovado, sera concignado en la cuenta numero {numero_de_cuenta} que tenga un buen dia ")
        