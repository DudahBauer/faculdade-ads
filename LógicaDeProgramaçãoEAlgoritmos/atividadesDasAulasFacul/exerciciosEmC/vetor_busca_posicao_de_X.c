//Leia um vetor de 20 posições e em seguida um valor X qualquer. Seu
//programa deverá fazer uma busca do valor de X no vetor lido e informar a
//posição em que foi encontrado ou se não foi encontrado.

#include<stdio.h>
#include<locale.h>

int vetor[20], numero, i=0, encontrado=0;

main(int argc, char*argv []){
	
	setlocale(LC_ALL, "");

for (i = 0; i < 20; i++) {
    vetor[i] = i * 2;
    
}

printf("Digite um número inteiro qualquer: \n");
scanf("%i", &numero);

i=0;
	
for(i=0; i<20; i++){
	if(vetor[i]==numero){
	printf("Valor encontrado na posição %i \n", i);
	encontrado=1;
	break;
}
}

	
if(encontrado==0){
	printf("Número não encontrado no vetor \n");
}
	return 0;
	
}
	
