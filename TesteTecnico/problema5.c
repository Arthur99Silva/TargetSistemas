#include <stdio.h>

void identificar_interruptores() {
    int lampada_1_quente = 0;
    int lampada_2_acesa = 0;

    // Liga interruptor 1
    printf("Liguei o Interruptor 1 e esperei um tempo.\n");
    lampada_1_quente = 1; // Lampada fica quente

    // Desliga interruptor 1 e liga interruptor 2
    printf("Desliguei o Interruptor 1 e liguei o Interruptor 2.\n");
    lampada_2_acesa = 1;

    // Vai a sala pela primeira vez
    printf("Vou até a sala das lâmpadas:\n");

    // Verifica qual lampada ficou acessa
    if (lampada_2_acesa) {
        printf("A lâmpada 2 está acesa, então o Interruptor 2 controla essa lâmpada.\n");
    }

    // Verifica qual lampada ficou quente
    if (lampada_1_quente) {
        printf("A lâmpada 1 está quente, então o Interruptor 1 controla essa lâmpada.\n");
    }

    // A lâmpada 3 foi a que sobrou
    printf("A lâmpada 3 está fria e apagada, então o Interruptor 3 controla essa lâmpada.\n");
}

int main() {
    identificar_interruptores();
    return 0;
}
