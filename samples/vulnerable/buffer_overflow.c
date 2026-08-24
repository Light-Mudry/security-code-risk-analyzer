#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    char buffer[10];

    if (argc < 2) {
        return 1;
    }

    strcpy(buffer, argv[1]);

    printf("Buffer: %s\n", buffer);

    return 0;
}