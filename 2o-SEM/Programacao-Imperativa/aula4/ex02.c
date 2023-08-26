#include <stdio.h>

int main(void) {
  char a, b, c;
  printf("Digite um número: ");
  scanf("%d", &a);
  printf("Digite outro número: ");
  scanf("%d", &b);
  printf("Digite outro número: ");
  scanf("%d", &c);

  if (a < b && a < c) {
    printf("Ordem ALFABÉTICA:\n");
    printf("%d\n", a);
    printf("%d\n", b);
    printf("%d\n", c);
  } else if (b < a && b < c) {
    printf("Ordem ALFABÉTICA:\n");
    printf("%d\n", b);
    printf("%d\n", a);
    printf("%d\n", c);

  } else if (c < a && c < b) {
    printf("%d\n", c);
    printf("%d\n", a);
    printf("%d\n", b);
  }
}

// NAO FINALIZEI, PAREI NAS COMPARAÇÕES