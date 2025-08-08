/*	2 – Algoritmo Preço de Automóvel
	O preço de um automóvel é calculado pela soma do preço de fábrica com o preço dos
	impostos (45% do preço de fábrica) e a percentagem do revendedor (28% do preço de fábrica).
	Faça um algoritmo que leia o nome do automóvel e o preço de fábrica e imprima o nome do
	automóvel e o preço final.
*/

#include <stdio.h>
#include <locale.h>

float preco_de_fabrica, impostos, parte_do_revendedor, preco_final;
char nome[258];

int main(int argc, char *argv[]){
	
	setlocale(LC_ALL,"");
	
	printf("Digite o nome do automóvel: \n");
	scanf("%s", &nome);
	printf("Digite o preço de fábrica do automovél\n");
	scanf("%f", &preco_de_fabrica);
	
	impostos= preco_de_fabrica*0.45;
	parte_do_revendedor=preco_de_fabrica*0.28;
	preco_final=impostos+parte_do_revendedor+preco_de_fabrica;
	
	
	printf("O nome do carro é: %s \n", nome);
	printf("O valor a ser pago de imposto é de: %.2f \n", impostos);
	printf("O valor referente ao vendedo é de: %.2f \n", parte_do_revendedor);
	printf("O preço final do automóvel é de: %.2f \n", preco_final);
	
	return 0;
};


 

