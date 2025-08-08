//A empresa Hipotéticos paga R$10,00 por hora normal trabalhada, e
//R$15,00 por hora extra. Faça um algoritmo para calcular e imprimir o salário
//bruto e o salário líquido de um determinado funcionário. Considere que o
//salário líquido é igual ao salário bruto descontando-se 10% de impostos. 

#include <stdio.h>
#include <locale.h>


float quantidade_de_h_trabalhadas, quantidade_de_h_extras, valor_da_h, valor_da_h_extra, salario_bruto, salario_liquido, imposto;

main(int argc, char *agv[]){
	
setlocale(LC_ALL, "");

printf("Digite a quantidade de horas que você trabalhou: \n");
scanf("%f", &quantidade_de_h_trabalhadas);
printf("Digite a quantidade de horas extra que você realizou: \n");
scanf("%f", &quantidade_de_h_extras);

valor_da_h=quantidade_de_h_trabalhadas*10;
valor_da_h_extra=quantidade_de_h_extras*15;

salario_bruto=valor_da_h+valor_da_h_extra;

imposto=salario_bruto*0.1;

salario_liquido=salario_bruto-imposto;

printf("O seu salário bruto é de: %.2f", salario_bruto);
printf("O seu salário líquido é de: %.2f", salario_liquido);

return 0;
}
