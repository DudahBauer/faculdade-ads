#include <stdio.h> 
#include <locale.h>

float base, altura, area;

int main(int argc, char *argv[] ){
	
	setlocale(LC_ALL, "");
	
	printf("Digite a o tamanho da base do seu tri�ngulo \n");
	scanf("%f", &base);
	
	printf("Digite a altura do seu tri�ngulo:");
	scanf("%f", &altura);
	
	area=(base*altura)/2;
	
	printf("A area do seu tri�ngulo � de: %.2f", area);
	
	return 0;
	
}


