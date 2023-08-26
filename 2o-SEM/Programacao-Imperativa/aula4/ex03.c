#include <stdio.h>

int main(void) {
  float PI = 3.1416;
  int R = 0;

  do {
    float volume = 4 / 3 * PI * (R * R * R);
    printf("%d %.4f\n", R, PI);
    R = R + 2;
  } while (R <= 6);
}