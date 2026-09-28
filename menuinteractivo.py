for i in range(1, 6):

print("=========MENU INTERACTIVO=========")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")
opcion=int(input("Por favor, Ingrese una opcion[1-5]: ")) #int

if opcion=='1':
    num1=float(input("Ingrese el primer numero: ")) #float
    num2=float(input("Ingrese el segundo numero: ")) #float
    resultado=num1+num2 #float
    print(f"El resultado de la suma es: {resultado:.2f}") #float
elif opcion=='2':
    num1=float(input("Ingrese el primer numero: ")) #float
    num2=float(input("Ingrese el segundo numero: ")) #float
    resultado=num1-num2 #float
    print(f"El resultado de la resta es: {resultado:.2f}") #float
elif opcion=='3':
    num1=float(input("Ingrese el primer numero: ")) #float
    num2=float(input("Ingrese el segundo numero: ")) #float
    resultado=num1*num2 #float
    print(f"El resultado de la multiplicacion es: {resultado:.2f}") #float
elif opcion=='4':
    num1=float(input("Ingrese el primer numero: ")) #float
    num2=float(input("Ingrese el segundo numero: ")) #float
    if num2!=0:
        resultado=num1/num2 #float
        print(f"El resultado de la division es: {resultado:.2f}") #float
    else:
        print("Error: No se puede dividir entre cero.")
elif opcion=='5':
    print("Gracias por usar el programa.")
else:
    print("Opcion no valida. Por favor, ingrese una opcion valida.")