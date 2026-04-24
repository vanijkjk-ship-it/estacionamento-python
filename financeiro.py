# Modulo utilizado para cálculo matemático
from math import ceil

# Constantes utilizadas para definir regras de cobrança do estacionamento
TOLERANCIA = 15
PRIMEIRA_HORA = 60
VALOR_BASE = 1.50
VALOR_HORA_EXTRA = 1.00

# Função gerada para chamar o cálculo dentro do programa
def calcular_valor(tempo):
    # Normaliza o tempo em minutos inteiros para garantir precisão no cálculo da tarifa
    tempo = int(tempo)
    if tempo <= TOLERANCIA:
        return 0

    elif tempo <= PRIMEIRA_HORA:
        return VALOR_BASE

    else:
        horas_extras = ceil((tempo - PRIMEIRA_HORA) / 60)
        return VALOR_BASE + (horas_extras * VALOR_HORA_EXTRA)
