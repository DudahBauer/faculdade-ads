// Algoritmo Media Valor
//Dado uma série de 05 valores inteiros de temperatura, leia este 5 valores e calcule a média
//destes, e em seguida apresente esta média e caso esta seja maior e igual que 30 graus
//escreva “temperatura acima da média, calor”, caso esta média seja inferior ou igual a 15 graus
//“temperatura a baixo da média, frio “ e se esta estiver no intervalo entre estes dois valores,
////“temperatura mediana, temperatura agradável”

#include <stdio.h>
#include <locale.h>

typedef enum{
	TYPE_INT,
	TYPE FLOAT,
	TYPE_DOUBLE
	
}InputType;

float valor1, valor2, valor3, valor4, valor5, media, soma;

int main(int arc, char *argv[]){
	
	setlocale(LC_ALL, "");
	
	printf("Calcule a média de 5 temperaturas: \n");
	printf("Digite o primeiro valor da temperatura: \n");
	scanf("%f", &valor1);
	printf("Digite o segundo valor da temperatura: \n");
	scanf("%f", &valor2);
	printf("Digite o terceiro valor da temperatura: \n");
	scanf("%f", &valor3);
	printf("Digite o quarto valor da temperatura: \n");
	scanf("%f", &valor4);
	printf("Digite o quinto valor da temperatura: \n");
	scanf("%f", &valor5);
	
	soma=valor1+valor2+valor3+valor4+valor5;
	
	media=soma/5;
	
	printf("O valor da média dos valores colocador é de: %.2f \n", media);
	
	if(media>=30){
		printf("Temperatura acima da média, calor! \n");
	}
	if (media<=15){
		printf("Temperatura abaixo da media, frio! \n");
	}
	if(media>=15 && media<=30){
		printf("Temperatura mediana, temperatura agradável!! \n");
	}
	
	return 0;
}

