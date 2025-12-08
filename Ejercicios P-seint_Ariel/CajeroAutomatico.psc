Algoritmo CajeroAutomatico
	
	Definir opcionMoneda, i, cantidadBilletes Como Entero
	Definir montoRetiro, resto Como Entero
	Definir billetes Como Entero
	Definir hayError Como Logico
	
	Dimensionar billetesCordobas[7]
	billetesCordobas[1] <- 1000
	billetesCordobas[2] <- 500
	billetesCordobas[3] <- 200
	billetesCordobas[4] <- 100
	billetesCordobas[5] <- 50
	billetesCordobas[6] <- 20
	billetesCordobas[7] <- 10
	
	
	Dimensionar billetesDolares[5]
	billetesDolares[1] <- 100
	billetesDolares[2] <- 50
	billetesDolares[3] <- 20
	billetesDolares[4] <- 10
	billetesDolares[5] <- 1
	
	Repetir
		Limpiar Pantalla
		Escribir "=========================================="
		Escribir "       CAJERO AUTOMÁTICO - BIENVENIDO     "
		Escribir "=========================================="
		Escribir "Seleccione la moneda para el retiro: "
		Escribir "1. Córdobas (C$)"
		Escribir "2. Dólares ($)"
		Escribir "3. Salir"
		Escribir "=========================================="
		Leer opcionMoneda
		
		si opcionMoneda = 1 o opcionMoneda = 2 Entonces
			Escribir "Ingrese la cantidad a retirar (solo números enteros): "
			Leer montoRetiro
			
			hayError <- Falso
			
			si	montoRetiro <= 0 Entonces
				Escribir "Error: La cantidad debe ser maayor 0."
				hayError <- Verdadero
			FinSi
		    
			Si opcionMoneda = 1 Y (montoRetiro MOD 10 <> 0) Entonces
				Escribir "Error: En Córdobas solo dispensamos billetes de 10 en adelante."
				Escribir "Por favor ingrese un monto múltiplo de 10 (ej: 150, 320)."
				hayError <- Verdadero
			FinSi
			
			
			si no hayError Entonces
				Escribir "_________________________________"
				Escribir "Desglose de billetes a entregar: "
				Escribir "_________________________________"
				
				resto <- montoRetiro
				
				si opcionMoneda = 1 Entonces
					
					Para i <- 1 Hasta 7 Hacer
						
						cantidadBilletes <- trunc(resto / billetesCordobas[i])
						
						si cantidadBilletes > 0 Entonces
							Escribir cantidadBilletes, " billete(s) de C$ ", billetesCordobas[i]
							
							resto <- resto MOD billetesCordobas[i]
						FinSi
					FinPara
				SiNo
					
					Para i <- 1 Hasta 5 Hacer
						cantidadBilletes <- trunc(resto / billetesDolares[i])
						
						si cantidadBilletes > 0 Entonces
							Escribir cantidadBilletes, " billete(s) de $ ", billetesDolares[i]
							resto <- resto MOD billetesDolares[i]
						FinSi
					FinPara
				FinSi
				
				Escribir "________________________________"
				Escribir "Retiro exitoso. ¡Tome su retiro!"
			FinSi
			
			Escribir ""
			Escribir "Presione una tecla para continuar..."
			Esperar Tecla
			
		FinSi
		
	Hasta Que opcionMoneda = 3
	
	Escribir "Gracias por usar nuestro cajero."
FinAlgoritmo
