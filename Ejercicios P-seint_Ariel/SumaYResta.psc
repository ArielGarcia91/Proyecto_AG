Algoritmo SumaYResta
	Definir opcion Como Entero
	Definir a, b, resultado Como Real
	
	Repetir
		Escribir ""
		EScribir "=== Menú de Operaciones ==="
		Escribir "1) Suma"
		Escribir "2) Resta"
		Escribir "3) Salir"
		Escribir "Seleccione una opción del 1-3: "
		leer	opcion
		segun opcion Hacer
			1:
				Escribir "Ingrese el primer número: "
				leer a
				Escribir "Ingrese el segundo número: "
				Leer b
				resultado<- a + b
				Escribir "Resultado de la Suma: ", resultado
			2:
				Escribir "Ingrese el primer número: "
				leer a
				Escribir "Ingrese el segundo número: "
				Leer b
				resultado<- a - b
				Escribir "Resultado de la Resta: ", resultado
			3:
				Escribir "Su operación a finalizado"
			De Otro Modo:
				Escribir "opcion inválida. Intente nuevamente."
				
		FinSegun
	Hasta Que opcion = 3
	
FinAlgoritmo
