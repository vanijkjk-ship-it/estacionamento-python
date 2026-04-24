# Importação de módulos padrão para sistema, regex e manipulação de data/hora
import os
import re
from datetime import datetime

# Limpa o terminal (compatível com Windows e Linux)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Valida se o horário está no formato correto e dentro do funcionamento (08:00 às 18:00)
def validar_horario(horario):
    try:
        h, m, s = map(int, horario.split(':'))

        if not (0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
            return False

        if h < 8:
            return False

        if h > 18:
            return False

        if h == 18 and (m > 0 or s > 0):
            return False

        return True

    except ValueError:
        return False

# Valida placa no padrão brasileiro (antigo e Mercosul)
def validar_placa(placa):
    # Normaliza a placa em maiúsculas para evitar inconsistências na comparação
    placa = placa.upper()

    padrao_antigo = r'[A-Z]{3}[0-9]{4}'
    padrao_mercosul = r'[A-Z]{3}[0-9][A-J][0-9]{2}'

    return bool(
        re.fullmatch(padrao_antigo, placa) or
        re.fullmatch(padrao_mercosul, placa)
    )

# Converte horário para minutos inteiros
def para_minutos(horario):
    h, m, s = map(int, horario.split(':'))
    return (h * 60) + m

# Retorna o horário atual formatado (HH:MM:SS)
def agora():
    return datetime.now().strftime('%H:%M:%S')
