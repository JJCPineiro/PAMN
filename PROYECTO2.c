#include <stdio.h>
#include <stdlib.h>
#include <string.h>

	struct Dato{ 		//Estructura para los datos
		char d_codigo[6];
		char d_asenta[50];
		char d_tipo_asenta[50];
		char D_mnpio[50];
		char d_estado[50];
		char d_ciudad[50];
		char d_CP[5];
		char c_estado[5];
		char c_oficina[5];
		char c_CP[5];
		char c_tipo_asenta[5];
		char c_mnpio[5];
		char id_asenta_cpcons[5];
		char d_zona[10];
		char c_cve_ciudad[5];
	};

int main(){
	FILE *cp;
	int i;
	char codigo[6];
	char salto1[250];
	char salto2[500];

	cp = fopen("CP1.txt", "r");	//Abrir archivo

	system("cls");		//Limpiar pantalla WINDOWS
	//system("clear");	//Limpiar pantalla UNIX

	if(cp == NULL){		//Comprobación de archivo
		printf("\nNo existe el archivo");
		return 1;
	}

	printf("========LECTOR DE CODIGO POSTAL========");	//Título



    struct Dato cps; //Estructura a utilizar

	printf("\n\nIngrese su C%cdigo postal [S%clo 5 digitos]:  ", 162, 162);	//Pide al usuario CP
	scanf("%s", codigo);
	printf("\n\n");

	fscanf(cp, "%[^\n]\n%[^\n]\n", salto1, salto2);	//Saltar las líneas de introducción

	while(!feof(cp)){		//Hasta que termine el documento

		printf("\r~~~\tProcesando:\t'%s'\t~~~", codigo);	//"Cargando..."
		
		fscanf(cp,"%[0-9\x20]|%[0-9a-zA-Z\x2f\x20\x22\x23\x28\x29-.°´]|%[0-9a-zA-Z\x20-]|%[0-9a-zA-Z\x20-.]|%[a-zA-Z\x20\x28\x29.-]|%[0-9a-zA-Z\x20\x22\x28\x29-.°]|%[0-9\x20]|%[0-9\x20]|%[0-9\x20]|%[0-9\x20]|%[0-9\x20]|%[0-9\x20]|%[0-9\x20]|%[a-zA-Z\x20-]|%[0-9\x20]\n", cps.d_codigo, cps.d_asenta, cps.d_tipo_asenta,cps.D_mnpio,cps.d_estado,cps.d_ciudad,cps.d_CP,cps.c_estado,cps.c_oficina, cps.c_CP, cps.c_tipo_asenta,cps.c_mnpio,cps.id_asenta_cpcons,cps.d_zona, cps.c_cve_ciudad);

			//  \x20 Lectura de (espacios)
			//	\x22 Lectura de " "
			//	\x23 Lectura de #
			//	\x28	\x29 	Lectura de ( )
			//	\x2f Lectura de /

		if(strcmp(codigo,cps.d_codigo)==0){		//Comparación de cadenas
			printf(" \n\n\n Codigo Postal.......%s", cps.d_codigo);		//Impresión de información
			printf(" \n Asentamiento.......%s", cps.d_asenta);
			printf(" \n Tipo asentamiento.......%s", cps.d_tipo_asenta);
			printf(" \n Municipio.......%s", cps.D_mnpio);
			printf(" \n Estado.......%s", cps.d_estado);
			printf(" \n Ciudad.......%s", cps.d_ciudad);
			printf(" \n Codigo.......%s", cps.d_CP);
			printf(" \n Codigo Estado.......%s", cps.c_estado);
			printf(" \n Codigo Oficina.......%s", cps.c_oficina);
			printf(" \n Codigo P.......%s", cps.c_CP);
			printf(" \n Codigo Tipo Asentamiento.......%s", cps.c_tipo_asenta);
			printf(" \n Codigo Municipio.......%s", cps.c_mnpio);
			printf(" \n ID Asentamiento.......%s", cps.id_asenta_cpcons);
			printf(" \n Zona..........%s", cps.d_zona);
			printf(" \n Clave Ciudad..........%s\n\n", cps.c_cve_ciudad);
            break;			//Detener la lectura
		}

	}
	if(strcmp(codigo,cps.d_codigo)!=0)
			printf("\n\n\tNo encontrado...\n\n");
	return 0;
}
