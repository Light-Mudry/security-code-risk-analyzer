#include <stdio.h>
#include <string.h>

int main(void) {
    char source[] = "Hello";
    char destination[20];

    snprintf(destination, sizeof(destination), "%s", source);

    printf("%s\n", destination);

    return 0;
}