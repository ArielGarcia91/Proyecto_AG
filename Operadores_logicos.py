# Conjución

print("Conjución (and)")

num_uno = int(input("Escriba un número mayor a 2 y menor a 5: "))

if num_uno > 2 and num_uno < 5:
    print("El número", num_uno, " cumple con la condición. \n")
    
else:
    print("El número", num_uno, " no cumple con la condición  \n")
    
#Disyución
print("Disyunción (or)")

palabra = input("Para cumplir con la condición escribe 'si' o 'yes': ")

if palabra == "si" or palabra == "yes":
    print("La condición se ha cumplido. \n")
    
#Negación
print("Negación (not)")

num_uno = int(input("Introduce un número igual a 5: "))

if not num_uno == 5:
    print("\n El número es diferente de cinco y si cumple la condición. \n")
else:
    print("\n El número es igual a cinco y no cumple la condición. \n")