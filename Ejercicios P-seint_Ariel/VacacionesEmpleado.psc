Algoritmo VacacionesEmpleado
	Definir cargo Como cadena
	Definir tiempo como cadena
	
	Escribir "Ingrese el cargo del empleado (directivo u operario)"
	Leer cargo
	si cargo = "directivo" Entonces
		Escribir "¿Lleva más de un año en la empresa? (si/no): "
		Leer tiempo
		si tiempo = "si" Entonces
			Escribir "Tiene derecho a 30 días de vacaciones"
		SiNo
			Escribir "No tiene derecho a vacaciones"
		FinSi
	SiNo
		si cargo = "operario" Entonces
			Escribir "¿Lleva más de un año en el cargo? (si/no): "
			Leer tiempo
			si tiempo = "si" Entonces
				Escribir "Tiene derecho a 15 días de vacaciones"
			SiNo
				Escribir "No tiene derecho a vacaciones"
			FinSi
		SiNo
			Escribir "Cargo no válido"
		FinSi
	FinSi
	
FinAlgoritmo
