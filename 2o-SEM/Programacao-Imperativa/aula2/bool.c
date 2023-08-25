#include <stdio.h>
#include <stdbool.h>

int main() {
    bool winter = true;
    bool summer = false;

    printf("%d\n", winter);
    printf("%d\n", summer);

    printf("%zu\n", sizeof(winter));
    printf("%zu\n", sizeof(summer));


    return 0;
}