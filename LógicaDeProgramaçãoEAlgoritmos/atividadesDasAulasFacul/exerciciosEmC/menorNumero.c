// Algoritmo 3 Menores
//Fa�a um algoritmo que leia 3 n�meros inteiros e imprima o menor deles.
#include <stdio.h>
#include <locale.h>

int numero1, numero2, numero3;

int main(int arc, char *argv[]){
	setlocale(LC_ALL, "");
	
	printf("Digite o primeiro n�mero: \n");
	scanf("%i",  &numero1);
	printf("Digite o segundo n�mero: \n");
	scanf("%i",  &numero2);
	printf("Digite o terceiro n�mero: \n");
	scanf("%i",  &numero3);
	
	if(numero1<numero2 && numero1<numero3){
		printf("O n�mero %.2i � o menor dos n�meros digitados", numero1);
	}
	if(numero2<numero1 && numero2<numero3){
		printf("O n�mero %.2i � o menor dos n�meros digitados", numero2);
	}
	if(numero3<numero2 && numero3<numero1){
		printf("O n�mero %.2i � o menor dos n�meros digitados", numero3);
	}
	if(numero1==numero2 && numero2==numero3){
		printf("Os tr�s n�meros que voc� digitou s�o iguais! Portanto, n�o h� um menor n�mero");
	}
	
	return 0;
}


