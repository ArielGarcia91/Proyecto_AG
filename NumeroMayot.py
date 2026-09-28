print("******************************************************")
print("Programa para determinar el número mayor de tres números")
print("****************************************************** \n")

num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))
num3 = int(input("Introduce el tercer número entero: "))

if num1 > num2 and num1 > num3:
    print(f"El número {num1} es el mayor de los tres.")
elif num2 > num3:
    print(f"El número {num2} es el mayor de los tres.")
else:
    print(f"El número {num3} es el mayor de los tres.")
