#include <stdio.h>
#include <stdbool.h>

int main() {
    short a = 10;
    double b = 45.9;
    char c = '$';
    bool d = true;

    short *pA = &a;
    printf("PA: %p\n", pA);
    printf("The content of PA: %d\n", *pA);

    double *pB = &b;
    printf("PB: %p\n", pB);
    printf("The content of PB: %d\n", *pB);

    char *pC = &c;
    printf("PC: %p\n", pC);
    printf("The content of PC: %d\n", *pC);

    bool *pD = &d;
    printf("PD: %p\n", pD);
    printf("The content of PD: %d\n", *pD);
    
    return 0;
}