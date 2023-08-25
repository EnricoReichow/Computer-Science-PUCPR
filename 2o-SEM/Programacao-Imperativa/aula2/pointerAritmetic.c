#include <stdio.h>

int main(){
    int a = 1, b = 2, c = 3;

    printf("The adress of a: %p\n", &a);
    printf("The adress of a: %p\n", &b);
    printf("The adress of a: %p\n", &c);

    int *p = &c;
    printf("p: %p\n", p);
    printf("content of p: %d\n", *p);

    p = p + 1;
    printf("p: %p\n", p);
    printf("content of p: %d\n", *p);

    p = p + 1;
    printf("p: %p\n", p);
    printf("content of p: %d\n", *p);
}