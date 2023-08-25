#include <stdio.h>

int main() {
    int temperature = 20;
    temperature = -10;

    unsigned int age = 30;
    age = 40;

    printf("%d %d\n", temperature, age); // %d means DECIMAL

    printf("%zu\n", sizeof(int));

    return 0;
}