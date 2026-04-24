# Módulos utilizados para manipulação e cálculo de dados do sistema
from utilidades import limpar_tela, para_minutos, agora
from financeiro import calcular_valor

# Execução da exibição dos veículos ativos
def mostrar_ativos(registros):

    # Limpa tela, para deixar fluído conforme uso, para não ficar bagunçado
    limpar_tela()

    print('\nVEÍCULOS ATIVOS:\n')

    # Filtra apenas veículos que ainda estão no estacionamento
    ativos = [r for r in registros if r['ativo']]

    # Caso não existam veículos ativos, encerra a função
    if not ativos:
        print('Nenhum veículo no estacionamento.')
        return

    # Ordena os veículos pelo horário de entrada (mais antigos primeiro)
    # Isso facilita a leitura e simula a ordem real de chegada
    # Aqui foi pensado para uma situação adversa, como pane no terminal ou algum contratempo
    # Uma vez que é permitido colocar o tempo de forma manual
    ativos.sort(key=lambda x: x['entrada'])

    # Variável acumuladora para projeção de arrecadação
    total_projetado = 0

    # Listagem de veículos
    for r in ativos:

        # Calcula o tempo atual de permanência no estacionamento
        # Converte horários para minutos para facilitar o cálculo
        tempo_atual = para_minutos(agora()) - para_minutos(r['entrada'])

        # Proteção contra inconsistências (ex: erro de horário)
        if tempo_atual < 0:
            tempo_atual = 0

        # Calcula o valor parcial com base no tempo atual
        valor_parcial = calcular_valor(tempo_atual)

        # Soma ao total projetado
        total_projetado += valor_parcial

        # Exibição individual
        print('-' * 30)
        print(f"{'Placa':<8}: {r['id']}")
        print(f"{'Tipo':<8}: {r['veiculo']}")
        print(f"{'Entrada':<8}: {r['entrada']}")
        print(f"{'Tempo':<8}: {tempo_atual:.0f} min")
        print(f"{'Parcial':<8}: R$ {valor_parcial:.2f}")
        print('-' * 30)

    # Resumo Operacional
    print('\nRESUMO OPERACIONAL:')
    print('-' * 30)

    # Total de veículos atualmente no estacionamento
    print(f"Veículos ativos   : {len(ativos)}")

    # Valor total estimado considerando o tempo atual de todos os veículos
    print(f"Arrecadação atual : R$ {total_projetado:.2f}")

    # Média de valor por veículo (indicador simples de desempenho)
    media = total_projetado / len(ativos) if ativos else 0
    print(f"Média por veículo : R$ {media:.2f}")

    # Interpretação do cenário atual
    if total_projetado == 0:
        print("Situação          : Apenas veículos dentro da tolerância")
    else:
        print("Situação          : Estacionamento gerando receita")

    print('-' * 30)