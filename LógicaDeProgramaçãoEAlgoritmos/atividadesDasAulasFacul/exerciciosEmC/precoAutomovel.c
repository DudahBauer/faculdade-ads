/*	2 � Algoritmo Pre�o de Autom�vel
	O pre�o de um autom�vel � calculado pela soma do pre�o de f�brica com o pre�o dos
	impostos (45% do pre�o de f�brica) e a percentagem do revendedor (28% do pre�o de f�brica).
	Fa�a um algoritmo que leia o nome do autom�vel e o pre�o de f�brica e imprima o nome do
	autom�vel e o pre�o final.
*/

#include <stdio.h>
#include <locale.h>

float preco_de_fabrica, impostos, parte_do_revendedor, preco_final;
char nome[258];

int main(int argc, char *argv[]){
	
	setlocale(LC_ALL,"");
	
	printf("Digite o nome do autom�vel: \n");
	scanf("%s", &nome);
	printf("Digite o pre�o de f�brica do automov�l\n");
	scanf("%f", &preco_de_fabrica);
	
	impostos= preco_de_fabrica*0.45;
	parte_do_revendedor=preco_de_fabrica*0.28;
	preco_final=impostos+parte_do_revendedor+preco_de_fabrica;
	
	
	printf("O nome do carro �: %s \n", nome);
	printf("O valor a ser pago de imposto � de: %.2f \n", impostos);
	printf("O valor referente ao vendedo � de: %.2f \n", parte_do_revendedor);
	printf("O pre�o final do autom�vel � de: %.2f \n", preco_final);
	
	return 0;
};


 

