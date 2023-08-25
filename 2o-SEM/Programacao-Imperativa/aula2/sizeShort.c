#include <stdio.h>

int main() {
    short temperature = 20;
    temperature = -10;

    unsigned short age = 30;
    age = 40;

    printf("%d %d\n", temperature, age); // %d means DECIMAL

    printf("%zu\n", sizeof(short));

    return 0;
}