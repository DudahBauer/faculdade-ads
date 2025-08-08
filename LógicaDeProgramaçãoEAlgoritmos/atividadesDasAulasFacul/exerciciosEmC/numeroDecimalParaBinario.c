//Faça um programa onde o usuário entra com um número decimal e o
//mesmo calcula e imprime o número no sistema binário .


#include <stdio.h>
#include <locale.h>


int numero, resto;
int binario[32];
int i=0;

main(int argc, char  *argv[]){
	
	setlocale(LC_ALL, "");
	
	printf("Digite o número decimal que você deseja transformar em binário: \n");
	scanf("%i", &numero);
	
	if (numero==0){
		printf("%i \n", numero);
		
		return 0;
	}
	
	while(numero!=0){
		resto=numero%2;
		binario[i]=resto;
		numero=numero/2;
		i++;
	}
	printf("O número decimal que você digitou, fica assim em código binário:");
	
	int j=i-1;
	for(; j >= 0; j--){
		printf("%i", binario[j]);
	}
	 return 0;
	 
}


