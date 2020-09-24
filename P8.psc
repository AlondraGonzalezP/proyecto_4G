Algoritmo sin_titulo
	Repetir
		Escribir 'Dame el primer numero'
		Leer Num1
		Escribir 'Dame el segundo numero'
		Leer Num2
		Resultado <- 0
		Resto <- Num1
		Mientras (Resto>=Num2) Hacer
			Resto <- Resto-Num2
			Resultado <- Resultado+1
		FinMientras
		Escribir Resultado
		Escribir 'Deeea continuar Si/No'
		Leer Continuar
	Hasta Que Continuar='No'
FinAlgoritmo

