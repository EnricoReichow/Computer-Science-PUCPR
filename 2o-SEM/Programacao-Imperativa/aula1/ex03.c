#include <stdio.h>
#include <stdbool.h>

int main() {
    short a = 10;
    double b = 45.9;
    char c = '$';
    bool d = true;

    printf("%p\n", &a);
    printf("%zu\n", sizeof(a));

    printf("%p\n", &b);
    printf("%zu\n", sizeof(b));

    printf("%p\n", &c);
    printf("%zu\n", sizeof(c));

    printf("%p\n", &d);
    printf("%zu\n", sizeof(d));
    
    return 0;
}