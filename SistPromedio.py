print("Sistema para calcular el promedio de un alumno")

nombre = input("Para comenzar, Cual es tu nombre?: ")

matematicas = int(input(nombre + ", Cual estu calificación en matemáticas?: "))
quimica = int(input(nombre + "Cual estu calificación en química?:" ))
biologia = int(input(nombre + ", Cual estu calificación en biología?: "))

promedio= (matematicas + quimica + biologia)/3
if promedio >= 6:
    print('Felicitaciones ' + nombre + ' "Aprobaste" con promedio de: ', promedio)
print('Fin')
