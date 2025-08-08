//Declare um vetor de 10 posições e o preencha com os 10 primeiros
//números impares e o escreva.

#include<stdio.h>
#include<locale.h>

int vetor[10], i=0;

main(int argc, char *argv[]){
	
	vetor[0]= 0;
	vetor[1]= 3;
	vetor[2]= 5;
	vetor[3]= 7;
	vetor[4]= 9;
	vetor[5]= 11;
	vetor[6]= 13;
	vetor[7]= 15;
	vetor[8]= 17;
	vetor[9]= 19;
	
	for(i=0; i<10; i=i+1){
		
		printf("vetor[%i]= %i \n", i, vetor[i]);
	}
	
	return 0;
	
}
