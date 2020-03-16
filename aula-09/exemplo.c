#include <stdio.h>
#include <stdlib.h>

int main(void) {
    char nome[100] = "Joao";
    int idade = 21;
    float valor = 34.82;

    printf("%s tem %d anos e possui R$ %.2f na carteira \n", nome, idade, valor);
}