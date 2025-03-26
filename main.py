
print("Ingrese el primer digito")
numero1 = int(input())

print("Ingrese el segundo digito")
numero2 = int(input())

suma = numero1 + numero2
print("La suma es igual a:", suma)

resta = numero1 - numero2
print("La resta es igual a:" , resta)

multiplicacion = numero1 * numero2
print("La multiplicacion es igual a:" , multiplicacion)

division = numero1 / numero2
print("La division es igual a:" , division)

modulo = numero1 % numero2
print("El modulo es igual a:", modulo)


print("Operacion suma, resta, multiplicacion, division")
operacion = input()

if operacion == "suma":
    print(suma)
elif operacion == "resta":
    print(resta)
elif operacion == "multiplicacion":
    print(multiplicacion)
else: 
  print(division)    

print("Ingresa 1 numero para sumar:")
numero3 = int(input())

print("Ingresa otro numero para sumar:")
numero4 = int(input())

print("Ingresa otro numero para sumar:")
numero5 = int(input())

suma3 = numero3 + numero4 + numero5
print("La suma de los tres numeros es:", suma3)




