//Uma empresa de desenvolvimento de software est� codificando um sistema
//de gera��o de folhas de pagamento dos colaboradores de uma empresa de
//Suprimentos de Inform�tica, para isto pede alguns dados de entrada do setor de
//gest�o de pessoas e assim gera a folha do m�s. Pede o Nome do Colaborador,
//quantidade de horas trabalhadas no m�s, valor da Hora/trabalho, qual o % de
//INSS a descontar e qual o % do Imposto de renda a descontar. Com estas
//informa��es inseridas no sistema, este gera e mostra na tela a folha do
//colaborador com os seguintes dados: Nome, Horas/Trabalhas, Valor Hora,
//sal�rio bruto, % INSS, % IR, e sal�rio l�quido. (5,0 pontos)

#include <stdio.h>
#include <locale.h>

char nome[100];
float horas, valor_da_hora, parte_INSS, parte_imposto_de_renda,  salario_bruto, desconto_imposto_de_renda, desconto_INSS;
float salario_liquido_final,salario_liquido_1_desconto, salario_liquido_2_desconto;

main(int argc, char *argv[]){
	
	setlocale(LC_ALL, "");
	
	printf("Digite o nome do colaborador:\n");
	scanf("%s", &nome);
	printf("Digite a quantidade de horas trabalhadas no m�s: \n");
	scanf("%f", &horas);
	printf("Qual o valor da sua hora de trabalho?:\n");
	scanf("%f", &valor_da_hora);
	printf("Qual a porcentagem de INSS a ser descontada?: \n");
	scanf("%f", &parte_INSS);
	printf("Qual a porcentagem do imposto de renda a ser descontada?: \n");
	scanf("%f", &parte_imposto_de_renda);
	
	salario_bruto= horas*valor_da_hora;
	
	desconto_imposto_de_renda= parte_imposto_de_renda/100;
	desconto_INSS= parte_INSS/100;
	
	salario_liquido_1_desconto= salario_bruto-(salario_bruto*desconto_imposto_de_renda);
	salario_liquido_2_desconto= salario_bruto-(salario_bruto*desconto_INSS);
	salario_liquido_final=(salario_bruto-(salario_liquido_1_desconto+salario_liquido_2_desconto))*-1;
	
	printf("- - - - -FOLHA-DO-COLABORADOR- - - - -: \n");
	printf("Nome do colaborador: %s \n", nome);
	printf("Horas trabalhadas: %f \n", horas);
	printf("O valor da hora � de: %.2f", valor_da_hora);
	printf("O sal�rio liqu�do � de: %.2f \n", salario_liquido_final);
	printf("O sal�rio bruto � de: %.2f \n", salario_bruto); 
	
	return 0;
	
	}


