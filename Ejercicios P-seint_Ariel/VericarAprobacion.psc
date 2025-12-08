Algoritmo VericarAprobacion
	Definir edad Como Entero
	Definir nacionalidad Como Cadena
	Definir hijos Como Entero
	
	Escribir "Ingrese la edad: "
	Leer edad
	Escribir "Ingrese la nacionalidad: "
	Leer nacionalidad
	Escribir "Ingrese número de hijos: "
	Leer hijos
	
	Si edad > 18 Entonces
		si nacionalidad = "colombiano" Entonces
			si hijos > 0 Entonces
				Escribir "Aprobado"
		    Sino 
				Escribir "No aprobado"
	        FinSi
		Sino
			Escribir "No aprobado"
	    FinSi
	Sino
		Escribir "No aprobado"
		finsi	
FinAlgoritmo
