//A empresa Hipot�ticos paga R$10,00 por hora normal trabalhada, e
//R$15,00 por hora extra. Fa�a um algoritmo para calcular e imprimir o sal�rio
//bruto e o sal�rio l�quido de um determinado funcion�rio. Considere que o
//sal�rio l�quido � igual ao sal�rio bruto descontando-se 10% de impostos. 

#include <stdio.h>
#include <locale.h>


float quantidade_de_h_trabalhadas, quantidade_de_h_extras, valor_da_h, valor_da_h_extra, salario_bruto, salario_liquido, imposto;

main(int argc, char *agv[]){
	
setlocale(LC_ALL, "");

printf("Digite a quantidade de horas que voc� trabalhou: \n");
scanf("%f", &quantidade_de_h_trabalhadas);
printf("Digite a quantidade de horas extra que voc� realizou: \n");
scanf("%f", &quantidade_de_h_extras);

valor_da_h=quantidade_de_h_trabalhadas*10;
valor_da_h_extra=quantidade_de_h_extras*15;

salario_bruto=valor_da_h+valor_da_h_extra;

imposto=salario_bruto*0.1;

salario_liquido=salario_bruto-imposto;

printf("O seu sal�rio bruto � de: %.2f", salario_bruto);
printf("O seu sal�rio l�quido � de: %.2f", salario_liquido);

return 0;
}
