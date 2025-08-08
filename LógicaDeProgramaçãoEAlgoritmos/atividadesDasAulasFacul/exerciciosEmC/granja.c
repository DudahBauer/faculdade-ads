//A granja Frangote possui um controle automatizado de cada frango da sua
//produção. No pé direito do frango há um anel com um chip de identificação;
//no pé esquerdo são dois anéis para indicar o tipo de alimento que ele deve
//consumir. Sabendo que o anel com chip custa R$4,00 e o anel de alimento
//custa R$3,50, faça um algoritmo para calcular o gasto total da granja para
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

printf("O valor total gasto com os anéis será de: %.2f", total_gasto);

return 0;
}
