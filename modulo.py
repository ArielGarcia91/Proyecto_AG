"""
Pedrir al usuario un numero y luego muestre si es par o impar.
"""

numero=int(input("Ingrese un numero: ")) #int
residuo=numero%2 #int

print(f"El residuo de la division es: {residuo}") #int
if residuo==0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")  