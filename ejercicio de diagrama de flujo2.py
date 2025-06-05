#sistema de clasificacion de pagos para sala de juegos
print(f"Bienvenido a nuestras salas de juegos donde todo es diversion \n por favor ingrese su edad ")
edad = int(input("ingresa tu edad "))
if edad < 4 :
    print ("su ingreso es gratuito que tenga un feliz dia")
elif edad < 18 :
    print("debes de pagar 5 euros para ingresar, que tengas un feliz dia")
else :
    print("debes de pagar 18 euros que tengas un feliz dia")