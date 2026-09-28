print("===========================")
print("Calculadora de una Variable")
print("============================= \n")

print("1. Suma")
print("2. Resta")
print("3. Multiplicción")
print("4. División")
print("5. División Entera")
print("6. Exponente")
print("7. Resto")

opcion=int(input("Seleccione una opción para continuar: "))

if opcion==1:
    print("Ha elegido sumar \n")
elif opcion==2:
        print("Ha elegido restar \n")
elif opcion==3:
        print("Ha elegido multiplicar \n")
elif opcion==4:
    print("Ha elegido dividir \n")
elif opcion==5:
    print("Ha elegido dividir entera \n")
elif opcion==6:
    print("Ha elegido exponente \n")
elif opcion==7:
    print("Ha elegido resto \n")
else:
    print("La opción selecionada no existe")
    
num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese el segundo número: "))
if opcion==1:
    suma=num1 + num2
    print("El resultado de la suma es: ", suma)
if opcion==2:
    resta=num1 - num2
    print("El resultado de la resta es: ", resta)
if opcion==3:
    producto=num1 * num2
    print("El resultado de la multiplicación es: ", producto)
if opcion==4:
    cociente=num1 / num2
    print("El resultado de la división es: ", cociente)
if opcion==5:
    cociente1=num1 // num2
    print("El resultado de la división entera es: ", cociente1)
if opcion==6:
    exponente=num1 ** num2
    print("El resultado de la exponente es: ", exponente)
if opcion==7:
    resto=num1 % num2
    print("El resultado del módulo o resto es: ", resto)