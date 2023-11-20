#include <stdio.h>

int main(void) {
    char a, b, c;
    printf("Digite uma letra:\n");
    a = getchar();
    getchar(); // Captura o caractere de nova linha pendente
    printf("Digite outra letra:\n");
    b = getchar();
    getchar(); // Captura o caractere de nova linha pendente
    printf("Digite mais uma letra:\n");
    c = getchar();
    getchar(); // Captura o caractere de nova linha pendente

    if (a <= b && a <= c) {
        if (b <= c) {
            printf("Ordem ALFABETICA:\n");
            putchar(a);
            putchar('\n');
            putchar(b);
            putchar('\n');
            putchar(c);
        } else {
            printf("Ordem ALFABETICA:\n");
            putchar(a);
            putchar('\n');
            putchar(c);
            putchar('\n');
            putchar(b);
        }
    } else if (b <= a && b <= c) {
        if (a <= c) {
            printf("Ordem ALFABETICA:\n");
            putchar(b);
            putchar('\n');
            putchar(a);
            putchar('\n');
            putchar(c);
        } else {
            printf("Ordem ALFABETICA:\n");
            putchar(b);
            putchar('\n');
            putchar(c);
            putchar('\n');
            putchar(a);
        }
    } else if (c <= a && c <= b) {
        if (a <= b) {
            printf("Ordem ALFABETICA:\n");
            putchar(c);
            putchar('\n');
            putchar(a);
            putchar('\n');
            putchar(b);
        } else {
            printf("Ordem ALFABETICA:\n");
            putchar(c);
            putchar('\n');
            putchar(b);
            putchar('\n');
            putchar(a);
        }
    }

    return 0;
}
