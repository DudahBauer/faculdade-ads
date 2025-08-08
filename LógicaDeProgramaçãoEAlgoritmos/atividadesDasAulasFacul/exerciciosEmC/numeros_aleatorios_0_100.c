// Leia um vetor de 10 posições com valores aleatórios 0-100 e na
//sequência selecione aleatoriamente três posições/índices deste vetor e
//apresente os seus valores e a multiplicação destes.

#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int vetor[10], i=0;

int main(int argc, char*argv []) {
    srand(time(NULL));


    for (i = 0; i < 10; i++) {
        int r = rand() % 101;
        printf("Número %d: %d\n", i + 1, r);
    }

    return 0;
}
