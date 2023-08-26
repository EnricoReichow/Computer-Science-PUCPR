#include <stdio.h>

int main(void) {
  int a, b;
  printf("Digite um número: ");
  scanf("%d", &a);
  printf("Digite outro número: ");
  scanf("%d", &b);

  if (a > b) {
    printf("Ordem CRESCENTE:\n");
    printf("%d\n", a);
    printf("%d\n", b);
  } else if (b > a) {
    printf("Ordem CRESCENTE:\n");
    printf("%d\n", b);
    printf("%d\n", a);
  } else {
    printf("Os valores são iguais!");
  }
}