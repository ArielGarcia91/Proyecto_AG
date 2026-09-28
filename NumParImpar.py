Numero=int(input("Ingrese un número: "))
if Numero % 2 == 0 and Numero>0:
    print("El número es par y positivo")
elif Numero % 2 == 0 and Numero<0:
    print("El número es par y negativo")
elif Numero % 2 != 0 and Numero>0:
    print("El número es impar y positivo")
else:
    print("El número es impar y negativo")
    
