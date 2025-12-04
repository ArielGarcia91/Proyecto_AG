Algoritmo segun_sw
	Definir num1, num2, resul Como Real
	Escribir 'Digite numeros a operar'
	Leer num1, num2
	Escribir 'Digite que operacion quiere hacer'
	Escribir '1 sumar, 2 restar, 3 multiplicar, 4 dividir'
	Leer numero
	Según numero Hacer
		1:
			resul <- num1+num2
			Escribir resul
		2:
			resul <- num-num2
			Escribir resul
		3:
			resul <- num1*num2
			Escribir resul
		4:
			resul <- num1/num2
			Escribir reul
		De Otro Modo:
			Escribir 'Esta opción no esta disponible'
	FinSegún
FinAlgoritmo
