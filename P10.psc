Algoritmo sin_titulo
	Repetir
		Escribir "Dime el numero limite de la serie de Fibonacci"
		Leer Limite1
		numero1=0
		numero2=1
		Para contador<-1 Hasta Limite1 Con Paso 1 Hacer
			Escribir numero2
			numero3=numero2+numero2
			numero1<-numero2
			numero2<-numero3
		Fin Para
		Escribir "Tu resultado"
		Escribir numero1
		Escribir "Desea repetir el proceso Siwon/Nel"
		Leer Continuar
	Hasta Que Continuar="Nel"
FinAlgoritmo
