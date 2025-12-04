Algoritmo Secuencia_AG
	Definir n, suma Como Real
	Definir conteo Como Entero
	suma <- 0
	conteo <-0
	Repetir
		Escribir "Escriba un número positivo (0 o número negativo parea terminar)"
		leer n
		si n > 0 Entonces
			suma <- suma + n
			conteo <- conteo + 1
		FinSi
	Hasta Que n <= 0
	Si conteo = 0 Entonces
		Escribir "No ingresó ningún número positivo"
	SiNo
		Escribir "Suma total de números positivos: ", suma
		Escribir "Cantidad de números positivos ingresados: ", conteo
	FinSi
	
FinAlgoritmo
