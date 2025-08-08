//Leia um vetor de 16 posições e troque os 8 primeiros valores pelos 8 últimos e vice-e-versa. Escreva ao final o vetor obtido.4

#include<stdio.h>
#include<locale.h>

int vetor[16]={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}, i;
int vetor_invertido[16];

main(int argc, char*argv[]){

for(i=0; i<16; i++){
	
	if(i<8){
		vetor_invertido[8+i]=vetor[i];
	}
	
	if(i>=8){
		vetor_invertido[i-8]=vetor[i];
	}
	
	//preciso fazer  outro if para inverter o resto do vetor
	
}
for(i=0; i<16; i++){
	
	printf("%i, ", vetor_invertido[i]);
}
	
}



