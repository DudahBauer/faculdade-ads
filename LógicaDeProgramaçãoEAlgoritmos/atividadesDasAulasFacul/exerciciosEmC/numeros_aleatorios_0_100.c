// Leia um vetor de 10 posi��es com valores aleat�rios 0-100 e na
//sequ�ncia selecione aleatoriamente tr�s posi��es/�ndices deste vetor e
//apresente os seus valores e a multiplica��o destes.

#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int vetor[10], i=0;

int main(int argc, char*argv []) {
    srand(time(NULL));


    for (i = 0; i < 10; i++) {
        int r = rand() % 101;
        printf("N�mero %d: %d\n", i + 1, r);
    }

    return 0;
}
