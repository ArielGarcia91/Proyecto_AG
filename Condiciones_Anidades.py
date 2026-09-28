print("=============")
print("CONVERSOR")
print("============= \n")

print("Menu de opciones:")
print("Presiona 1 para converir de número a palabra.")
print("Presiona 2 para convertir de palabra a número.")

opcion = int(input("Ingrese su opción: "))

if opcion == 1:
   print("\n Conversor de número a palabra \n")
   
   if opcion == 1:
       numero = int(input("Ingrese un número del 1 al 10: "))
       if numero == 1:
           print("El número es: 'uno'")
       elif numero == 2:
           print("El número es: 'dos'")
       elif numero == 3:
           print("El número es: 'tres'")
       elif numero == 4:
           print("El número es: 'cuatro'")
       elif numero == 5:
           print("El número es: 'cinco'")
       elif numero == 6:
           print("El número es: 'seis'")
       elif numero == 7:
           print("El número es: 'siete'")
       elif numero == 8:
           print("El número es: 'ocho'")
       elif numero == 9:
           print("El número es: 'nueve'")
       elif numero == 10:
           print("El número es: 'diez' ")
       else:
           print("Número fuera de rango. Por favor, ingrese un número del 1 al 10.")
elif opcion == 2:
   print("\n Conversor de palabra a número \n")
   opcion_dos = input("Ingrese una palabra del 1 al 10: ").lower()
   if opcion_dos == "uno":
       print("El número es: 1")
   elif opcion_dos == "dos":
       print("El número es: 2")
   elif opcion_dos == "tres":
       print("El número es: 3")
   elif opcion_dos == "cuatro":
       print("El número es: 4")
   elif opcion_dos == "cinco":
       print("El número es: 5")
   elif opcion_dos == "seis":
       print("El número es: 6")
   elif opcion_dos == "siete":
       print("El número es: 7")
   elif opcion_dos == "ocho":
       print("El número es: 8")
   elif opcion_dos == "nueve":
       print("El número es: 9")
   elif opcion_dos == "diez":
       print("El número es: 10")
   else:
       print("Palabra fuera de rango. Por favor, ingrese una palabra del 1 al 10.")
else:
   print("\n Opción inválida. Por favor, seleccione una opción válida del menú. \n")
print("Fin del programa. ¡Gracias por usar el conversor!")