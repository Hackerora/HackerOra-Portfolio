#include <stdio.h>

int main() {

int port;

printf("Simple Port Scanner\n");

for(port=1; port<=1024; port++){
printf("Checking port %d\n", port);
}

return 0;
}