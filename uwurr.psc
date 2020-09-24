Algoritmo sin_titulo
	Repetir
		Dimension vector(5)
		// lectura del vector
		Para i<-1 Hasta 5 Con Paso 1 Hacer
			Escribir "dame el numero "
			Leer vector(i)
		Fin Para
		// Proceso para ordenar el factor
		para actual<-1 hasta 5 con paso 1 hacer
			mayor=vector(actual)
			posmayor=actual
			para siguiente<-actual hasta 5 con paso 1 hacer
				// Proceso donde se cambira la variable por el numero mayor 
				si vector(siguiente)>mayor entonces
					mayor<-vector(siguiente)
					posmayor<-siguiente
				FinSi
			FinPara
			// Proceso donde se intercambia posiciones con el numero mas grande
			temporal=vector(actual)
			vector(actual)=mayor
			vector(posmayor)=temporal
			Para i<-1 Hasta 5 Con Paso 1 Hacer
				Escribir "el numero es "
				Escribir vector(i)
			Fin Para
			Leer Pausa 
		FinPara
		Escribir"Desea repetir el vector siwon/nel"
		Leer continuar 
	Hasta Que continuar="nel"
FinAlgoritmo
