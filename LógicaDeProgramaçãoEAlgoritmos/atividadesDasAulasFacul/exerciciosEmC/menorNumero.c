// Algoritmo 3 Menores
//Faça um algoritmo que leia 3 números inteiros e imprima o menor deles.
#include <stdio.h>
#include <locale.h>

int numero1, numero2, numero3;

int main(int arc, char *argv[]){
	setlocale(LC_ALL, "");
	
	printf("Digite o primeiro número: \n");
	scanf("%i",  &numero1);
	printf("Digite o segundo número: \n");
	scanf("%i",  &numero2);
	printf("Digite o terceiro número: \n");
	scanf("%i",  &numero3);
	
	if(numero1<numero2 && numero1<numero3){
		printf("O número %.2i é o menor dos números digitados", numero1);
	}
	if(numero2<numero1 && numero2<numero3){
		printf("O número %.2i é o menor dos números digitados", numero2);
	}
	if(numero3<numero2 && numero3<numero1){
		printf("O número %.2i é o menor dos números digitados", numero3);
	}
	if(numero1==numero2 && numero2==numero3){
		printf("Os três números que você digitou são iguais! Portanto, não há um menor número");
	}
	
	return 0;
}


