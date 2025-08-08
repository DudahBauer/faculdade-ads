//Uma empresa de desenvolvimento de software está codificando um sistema
//de geração de folhas de pagamento dos colaboradores de uma empresa de
//Suprimentos de Informática, para isto pede alguns dados de entrada do setor de
//gestão de pessoas e assim gera a folha do mês. Pede o Nome do Colaborador,
//quantidade de horas trabalhadas no mês, valor da Hora/trabalho, qual o % de
//INSS a descontar e qual o % do Imposto de renda a descontar. Com estas
//informações inseridas no sistema, este gera e mostra na tela a folha do
//colaborador com os seguintes dados: Nome, Horas/Trabalhas, Valor Hora,
//salário bruto, % INSS, % IR, e salário líquido. (5,0 pontos)

#include <stdio.h>
#include <locale.h>

char nome[100];
float horas, valor_da_hora, parte_INSS, parte_imposto_de_renda,  salario_bruto, desconto_imposto_de_renda, desconto_INSS;
float salario_liquido_final,salario_liquido_1_desconto, salario_liquido_2_desconto;

main(int argc, char *argv[]){
	
	setlocale(LC_ALL, "");
	
	printf("Digite o nome do colaborador:\n");
	scanf("%s", &nome);
	printf("Digite a quantidade de horas trabalhadas no mês: \n");
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
	printf("O valor da hora é de: %.2f", valor_da_hora);
	printf("O salário liquído é de: %.2f \n", salario_liquido_final);
	printf("O salário bruto é de: %.2f \n", salario_bruto); 
	
	return 0;
	
	}


