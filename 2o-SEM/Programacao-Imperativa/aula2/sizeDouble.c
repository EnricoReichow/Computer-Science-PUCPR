#include <stdio.h>

int main() {
    double PI = 3.14;
    double radius = 10.0;
    double area = PI * (radius * radius);

    printf("%f\n", area);
    printf("%zu\n" , sizeof(double)); // 8 bytes

    return 0;
}