// Leia um vetor de 10 posi��es com valores aleat�rios 0-100 e na
//sequ�ncia selecione aleatoriamente tr�s posi��es/�ndices deste vetor e
//apresente os seus valores e a multiplica��o destes.

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>

int vetor[10], i=0, multiplicacao;

int main(int argc, char*argv[]) {
	
	setlocale(LC_ALL, "");
	
	
//usu�rio digita os 10 valores
    printf("Digite 10 n�meros inteiros de 0 a 100:\n");
    
//loop para "adicionar" os valores aos indices
    for (i = 0; i < 10; i++) {
        printf("Valor %d: ", i + 1);
        scanf("%d", &vetor[i]);
    }
//loop para printar o vetor completo na tela 
    printf("\nValores digitados:\n");
    for (i = 0; i < 10; i++) {
        printf("%d \n", vetor[i]);
    }

//gerador de n�meros aleat�rios
    srand(time(NULL));

//sorteia 3 posi��es aleat�rias diferentes
    int i1, i2, i3;

    i1 = rand() % 10;

    do {
        i2 = rand() % 10;
    } while (i2 == i1);

    do {
        i3 = rand() % 10;
    } while (i3 == i1 || i3 == i2);

    printf("Os valores sorteados foram: %d, %d, %d\n", vetor[i1], vetor[i2], vetor[i3]);

    multiplicacao = vetor[i1] * vetor[i2] * vetor[i3];
    printf("A multiplica��o desses valores �: %d\n", multiplicacao);

    return 0;
}

