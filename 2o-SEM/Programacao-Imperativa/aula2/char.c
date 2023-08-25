#include <stdio.h>

int main() {
    char letter = 'A';
    printf("%c\n", letter);
    printf("%d\n", letter);

    letter = letter + 1;
    printf("%c\n", letter); // %c use to char
    printf("%d\n", letter);

    letter = letter / 2;
    printf("%c\n", letter);
    printf("%d\n", letter);

    return 0;
}