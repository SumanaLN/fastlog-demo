#include <stdio.h>
#include "fastlog.h"

int count_chars(char str[]) {
    int count = 0;

    for (int i = 0; str[i] != '\0'; i++) {
        count++;
    }

    return count;
}

int main() {
    char text[] = "FastLog Demo";

    printf("Character Count: %d\n", count_chars(text));

    return 0;
}