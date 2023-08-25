#include <stdio.h>

int main() {
    float PI = 3.14;
    float radius = 10.0;
    float area = PI * (radius * radius);
    
    printf("%f\n", area);
    printf("%zu\n" , sizeof(float)); // 4 bytes

    return 0;
}