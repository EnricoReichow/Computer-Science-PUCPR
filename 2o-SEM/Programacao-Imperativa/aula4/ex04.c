// calculadora
#include <stdio.h>

int main(void) {
  char operacaoEscolhida;
  double numero1, numero2;

  printf("-- Calculadora --\n");
  printf("Digite:\n");
  printf("A - Adicao\n");
  printf("S - Subtracao\n");
  printf("M - Multiplicacao\n");
  printf("D - Divisao\n");
  operacaoEscolhida = getchar();

  switch (operacaoEscolhida) {
  case 'A':
    printf("Digite o primeiro numero: ");
    scanf("%lf", &numero1);
    printf("Digite o segundo numero: ");
    scanf("%lf", &numero2);
    double soma = numero1 + numero2;
    printf("A soma é = %f\n", soma);
    break;

  case 'S':
    printf("Digite o primeiro numero: ");
    scanf("%lf", &numero1);
    printf("Digite o segundo numero: ");
    scanf("%lf", &numero2);
    double subtracao = numero1 - numero2;
    printf("A soma é = %f\n", subtracao);
    break;
  case 'M':;
    printf("Digite o primeiro numero: ");
    scanf("%lf", &numero1);
    printf("Digite o segundo numero: ");
    scanf("%lf", &numero2);
    double multiplicacao = numero1 * numero2;
    printf("A soma é = %f\n", multiplicacao);
    break;
  case 'D':
    printf("Digite o primeiro numero: ");
    scanf("%lf", &numero1);
    printf("Digite o segundo numero: ");
    scanf("%lf", &numero2);
    double divisao = numero1 / numero2;
    printf("A soma é = %f\n", divisao);
    break;
  }
}