#include <stdio.h>

int main()
{
    double PI = 3.14;
    double radius = 10.0;
    double area = PI * (radius * radius);

    printf("%f\n", area); // %f to show Real Numbers

    printf("%p\n", &area);
    printf("%p\n", &radius); // %p to acess Memory Adress
    printf("%p\n", &PI);


    printf("%zu\n", sizeof(area));
    printf("%zu\n", sizeof(radius)); // %zu to use SIZEOF
    printf("%zu\n", sizeof(PI));
    printf("%zu\n", sizeof(double));

    return 0;
}