#include <stdio.h> 
#include <locale.h>

float base, altura, area;

int main(int argc, char *argv[] ){
	
	setlocale(LC_ALL, "");
	
	printf("Digite a o tamanho da base do seu triângulo \n");
	scanf("%f", &base);
	
	printf("Digite a altura do seu triângulo:");
	scanf("%f", &altura);
	
	area=(base*altura)/2;
	
	printf("A area do seu triângulo é de: %.2f", area);
	
	return 0;
	
}


