#include <stdio.h>

int main(void)
{
  int a, b;
  printf("Digite um numero: ");
  scanf("%d", &a);
  printf("Digite outro numero: ");
  scanf("%d", &b);

  if (a > b)
  {
    printf("Ordem CRESCENTE:\n");
    printf("%d\n", b);
    printf("%d\n", a);
  }
  else if (b > a)
  {
    printf("Ordem CRESCENTE:\n");
    printf("%d\n", a);
    printf("%d\n", b);
  }
  else
  {
    printf("Os valores sao iguais!");
  }
}