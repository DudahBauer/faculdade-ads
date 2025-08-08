//Fa�a um programa onde o usu�rio entra com um n�mero decimal e o
//mesmo calcula e imprime o n�mero no sistema bin�rio .


#include <stdio.h>
#include <locale.h>


int numero, resto;
int binario[32];
int i=0;

main(int argc, char  *argv[]){
	
	setlocale(LC_ALL, "");
	
	printf("Digite o n�mero decimal que voc� deseja transformar em bin�rio: \n");
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
	printf("O n�mero decimal que voc� digitou, fica assim em c�digo bin�rio:");
	
	int j=i-1;
	for(; j >= 0; j--){
		printf("%i", binario[j]);
	}
	 return 0;
	 
}


