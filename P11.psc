Algoritmo sin_titulo
	Repetir
		Dimension vector(5)
		//Lectura delvector
		Para l<-1 Hasta 5 Con Paso 1 Hacer
			Escribir"Dame el numero"
			Leer vector(1) 
		Fin Para
		//Proceso para ordenar el factor
		Para actual=1 Hasta 5 Con Paso 1 Hacer		
			mayor=vector(actual)
			postmayor=actual
			Para siguiente<-actual Hasta 5 Con Paso 1 Hacer
				Si vector(siguiente)>mayor 
					mayor=vector(siguiente)
					postmayor=siguiente 
				Fin Si
			Fin Para
			Temporal=vector(actual)
			vector(actual)=mayor
			vector(postmayor)=Temporal
			Para l<-1 Hasta 5 Con Paso 1 Hacer
				Escribir"El numero es"
				Escribir vector(1)
			Fin Para
			leer pausa 
		FinPara
		Escribir"Desea repetir el vector siwon/nel"
		Leer continuar
		Hasta Que continuar="nel"
FinAlgoritmo
