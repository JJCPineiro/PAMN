#include <stdio.h>
#include <stdlib.h>

/*____Programa para Sistemas Windows____*/

int main(){

	int *M; 		//Para matriz
	int m=0, n=0;	//m renglones n columnas
	int i, j; 		//Contadores
	int total=0; 	//Suma de ceros
	int columnas = 0;
	system("cls");	//SOLO WINDOWS
	printf("%c==========================================%c\n",201,187); 	//Imprime el formato de bienvenida del programa
	printf("%c===========     BIENVENIDO     ===========%c\n",204,185);
	printf("%c==========================================%c\n\n",200,188);
	system("pause");	//SOLO WINDOWS

	do{							//Verifica que el número de renglones sean mayores que cero		
		printf("\nCuantos renglones tiene su matriz?\n");
		scanf("%d", &m); 		//Valor de m	
		if(m<=0)
			printf("Inserte un valor entero positivo...\n");	//Mensaje menor de cero
	}while(m<=0);			//Repite si es menor

	do{						//Verifica que el número de columnas sean mayores que cero
		printf("\nCuantas columnas tiene su matriz?\n");
		scanf("%d", &n);	//valor de n
		if(n<=0)
			printf("Inserte un valor entero positivo...\n");	//Mensaje menor de cero
	}while(n<=0);			//Repite si es menor

	M = (int *)malloc((m*n)*sizeof(int));						//Tamaño de M

	printf("\n");

	//Introducir los datos

	for(i=0;i<m;i++){
		for(j=0;j<n;j++){
			printf("Ingrese el valor de M[%d][%d]:  ", i+1, j+1); 	//Entrada de valores
			scanf("%d", M+i+j+columnas);
			printf("%d-----%p\n",i+j+columnas, M);
		}
		columnas = columnas + (n - 1); //Avance de las columnas
	}

	//Impresión de los datos

	columnas = 0;

	for(i=0;i<m;i++){
		for(j=0;j<n;j++){
			//Moviendo sólo el apuntador
			if(*M == 0)
				total = total + 1;
			printf(" %d ", *M);
			M++;
		}
		printf("\n");
	}

	printf("\n\n\tSe ingresaron %d ceros\n\n", total); 	//Muestra el total de ceros
	system("pause");									//SOLO WINDOWS
	return 0;
}
