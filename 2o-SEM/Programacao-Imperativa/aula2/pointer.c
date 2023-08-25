#include <stdio.h>

int main() {
    int a = 10;
    printf("The memory adress of a: %p\n", &a);
    printf("The size of a: %zu\n", sizeof(a));

    int *p = &a;
    printf("Value of p: %p\n", p);
    printf("Value pointed by p: %d\n", *p);
    printf("The memory adress of p: %p\n", &p);
    printf("The size of p: %zu\n", sizeof(p));
}