//A granja Frangote possui um controle automatizado de cada frango da sua
//produ��o. No p� direito do frango h� um anel com um chip de identifica��o;
//no p� esquerdo s�o dois an�is para indicar o tipo de alimento que ele deve
//consumir. Sabendo que o anel com chip custa R$4,00 e o anel de alimento
//custa R$3,50, fa�a um algoritmo para calcular o gasto total da granja para
//marcar todos os seus frangos. (4,0)

#include<stdio.h>
#include<locale.h>

int quantidade_de_galinhas, quantidade_aneis_alimentacao;
float valor_gasto_anel_chip, valor_gasto_anel_alimentacao, total_gasto, anel_com_chip, anel_de_alimento ;

main(int agrc, char *argv[]){
	
setlocale(LC_ALL, "");

printf("Digite a quantidade de frangos da granja:");
scanf("%i", &quantidade_de_galinhas);

quantidade_aneis_alimentacao=quantidade_de_galinhas*2;

anel_com_chip = 4.00;
anel_de_alimento = 3.50;

valor_gasto_anel_chip= anel_com_chip*quantidade_de_galinhas;
valor_gasto_anel_alimentacao= quantidade_aneis_alimentacao * anel_de_alimento;

total_gasto= valor_gasto_anel_chip+valor_gasto_anel_alimentacao;

printf("O valor total gasto com os an�is ser� de: %.2f", total_gasto);

return 0;
}
