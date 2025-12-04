
// Cal valor de las ventas del día
// Sabiendo que cada producto cuesta C$1000
// La cantidad de producto se lea por la pantalla
Funcion precio<- calculo (n1)
	valProducto = 1000
	precio = n1*valProducto
Fin Funcion

Algoritmo retorno
	Definir total Como Real
	Escribir "Digite cantidad de productos"
	Leer parcial
	total = calculo(parcial)
	Escribir "El total vendido fue de ", total
FinAlgoritmo
