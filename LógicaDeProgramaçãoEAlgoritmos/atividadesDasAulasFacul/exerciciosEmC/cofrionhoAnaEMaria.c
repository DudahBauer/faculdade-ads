//Ana e Maria, cada uma delas tem um cofrinho com muitas moedas, e elas
//querem saber quantos reais conseguiram poupar individualmente e juntas. Faça
//um algoritmo para ler a quantidade de cada tipo de moeda, e imprimir o valor
//total economizado por Ana, por Maria e por ambas, em reais. Considere que elas
//somente guardaram moedas de 50 centavos e 1 real. Construa um algoritmo
//codificado na linguagem C que leia para Ana as respectivas quantidades de
//moedas de cada valor, assim como para a Maria e por fim calcule o valor em
//reais e centavos economizado por Ana, e por Maria e por ambas, mostrando nas
//telas tais informações

#include <stdio.h>
#include <locale.h>

float moedas_um_real_ana, moedas_50_centavos_ana, moedas_um_real_maria, moedas_50_centavos_maria;
float cinquenta_centavos_ana, cinquenta_centavos_maria, total_de_um_real, total_de_centavos;
float total_de_ana, total_de_maria, total;

main(int argc, char *agrv[]){
	
setlocale(LC_ALL, "");

printf("Digite a quantidade de moedas de um real que ANA tem: \n");
scanf("%f", &moedas_um_real_ana);
printf("Digite a quantidade de moedas de cinquenta centavos que ANA tem: \n");
scanf("%f", &moedas_50_centavos_ana);
printf("Digite a quantidade de moedas de um real que MARIA tem: \n");
scanf("%f", &moedas_um_real_maria);
printf("Digite a quantidade de moedas de cinquenta centavos que MARIA tem: \n");
scanf("%f", &moedas_50_centavos_maria);


cinquenta_centavos_ana= moedas_50_centavos_ana/2;
cinquenta_centavos_maria= moedas_50_centavos_maria/2;

total_de_um_real= moedas_um_real_ana+moedas_um_real_maria;

total_de_centavos= cinquenta_centavos_ana+cinquenta_centavos_maria;


total_de_ana= moedas_um_real_ana+cinquenta_centavos_ana;
total_de_maria= moedas_um_real_maria+cinquenta_centavos_maria;

total= total_de_ana+total_de_maria;

printf("O total de moedas de Ana é de: %.2f \n", total_de_ana);
printf("O total de moedas de Maria é de: %.2f \n", total_de_maria);
printf("As duas tem juntas: %2.f reais \n", total);

}
