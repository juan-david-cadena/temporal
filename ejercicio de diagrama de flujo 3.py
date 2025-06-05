#calculadora de parentesis
simbolo = input("ingrese el simbolo de la operacion que desee realizar ").upper()
if simbolo == "S" :
    resul = [int(input("ingrese el primer numero a sumar")) + int(input(" ingrese el segundo valor a sumar "))]
    print (f"el resultado de {resul[0]} mas {resul[1]} es {resul}")