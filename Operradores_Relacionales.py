print("Introduce dos números para compararlos \n")

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

print(f"\n Los números a comparar son: {numero1} y {numero2} \n")
if numero1 == numero2:
    print(f"El número {numero1} es igual a {numero2}")
if numero1 != numero2:
    print(f"El número {numero1} es diferente a {numero2}")
if numero1 < numero2:
    print(f"El número {numero1} es menor que {numero2}")
if numero1 > numero2:
    print(f"El número {numero1} es mayor que {numero2}")
if numero1 <= numero2:
    print(f"El número {numero1} es menor o igual a {numero2}")
if numero1 >= numero2:
    print(f"El número {numero1} es mayor o igual a {numero2}")