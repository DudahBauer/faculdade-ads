//Leia um vetor de 20 posi��es e em seguida um valor X qualquer. Seu
//programa dever� fazer uma busca do valor de X no vetor lido e informar a
//posi��o em que foi encontrado ou se n�o foi encontrado.

#include<stdio.h>
#include<locale.h>

int vetor[20], numero, i=0, encontrado=0;

main(int argc, char*argv []){
	
	setlocale(LC_ALL, "");

for (i = 0; i < 20; i++) {
    vetor[i] = i * 2;
    
}

printf("Digite um n�mero inteiro qualquer: \n");
scanf("%i", &numero);

i=0;
	
for(i=0; i<20; i++){
	if(vetor[i]==numero){
	printf("Valor encontrado na posi��o %i \n", i);
	encontrado=1;
	break;
}
}

	
if(encontrado==0){
	printf("N�mero n�o encontrado no vetor \n");
}
	return 0;
	
}
	
