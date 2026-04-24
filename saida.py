# Importações organizadas por modulos existentes e criados com chamada de função
from financeiro import calcular_valor
from datetime import datetime
from utilidades import para_minutos, validar_horario, limpar_tela

# Função criada para chamar no menu e repartir código, para facilitar manutenção
def registrar_saida(registros):

    while True:
        # Limpa tela, para deixar fluído conforme uso, para não ficar bagunçado
        limpar_tela()

        print('\nVEÍCULOS NO ESTACIONAMENTO:\n')

        # Variável utilizada para filtrar ativos
        ativos = [r for r in registros if r['ativo']]
        ativos.sort(key=lambda x: para_minutos(x['entrada']))

        # Condição criada para verificar se tem veículos ativos
        if not ativos:
            print('Nenhum veículo no estacionamento!')
            input('\nPressione ENTER para voltar...')
            return

        # Laço criado para exibir de forma organizada os dados para o usuário
        for i, r in enumerate(ativos, start=1):
            print(f"[{i}]")
            print(f"{'Placa':<8}: {r['id']}")
            print(f"{'Tipo':<8}: {r['veiculo']}")
            print(f"{'Entrada':<8}: {r['entrada']}")
            print('-' * 30)

        # MENU DE SELEÇÃO
        print()
        print('\nComo deseja selecionar o veículo?')
        print()
        print('[1] Escolher pelo número')
        print('[2] Buscar por placa/chassi')
        print('[3] Voltar')
        print()
        # Variável criada para digitar escolha do Menu
        metodo = input('Opção: ').strip()

        # Retorno ao menu principal
        if metodo == '3':
            return

        # Condição simulando escolha por numeração
        if metodo == '1':
            escolha = input('Digite o número do veículo: ').strip()
            # Condição para verificar se usuário não escolheu uma entrada inválida
            # Caso ocorra o programa dá uma pausa e pede enter para continuar e chamar novamente a tela
            if not escolha.isdigit():
                print('Entrada inválida!')
                input('\nENTER...')
                continue
            # Variável para converter a escolha para número inteiro
            escolha = int(escolha)
            if escolha < 1 or escolha > len(ativos):
                print('Opção fora da lista!')
                input('\nENTER...')
                continue

            r = ativos[escolha - 1]


        # Opção de escolha por placa ou chassi
        elif metodo == '2':
            id_busca = input('Digite a placa/chassi: ').strip().upper()
            # Laço para encontrar veículo por placa ou chassi percorrendo a lista
            for veiculo in ativos:
                if veiculo['id'] == id_busca:
                    r = veiculo
                    break
            else:
                print('Veículo não encontrado!')
                input('\nENTER...')
                continue
        # Condição gerada para quando o usuário escolhe algo fora do Menu
        else:
            print('Opção inválida!')
            input('\nENTER...')
            continue

        # Validações com while para confirmar a hora da saída
        while True:
            print('\n[1] Digitar horário')
            print('[2] Usar horário atual')
            #Variável para micromenu
            escolha = input('Escolha: ').strip()
            # Condição aberta para escolha da forma como será feito registro da hora da saída
            if escolha == '2':
                saida = datetime.now().strftime('%H:%M:%S')
                print(f'Saída automática: {saida}')
                break

            elif escolha == '1':
                saida = input('Hora de saída (HH:MM:SS): ').strip()
                # Condição chamada para validar corretamente a hora e informar erro da digitação
                if validar_horario(saida):
                    break
                else:
                    print('Formato inválido! Use HH:MM:SS')

            else:
                print('Opção inválida!')

        # Variável para converter hora em minuto para cálculo
        entrada_min = para_minutos(r['entrada'])
        saida_min = para_minutos(saida)
        # Condição aberta para evitar uma saída menor que a entrada
        if saida_min < entrada_min:
            print('\nERRO: saída menor que entrada!')
            print('Operação cancelada.')
            input('\nPressione ENTER para continuar...')
            continue
        # Variável para calcular o tempo e gerar valor
        tempo = saida_min - entrada_min

        # Atualiza os dados após a saída
        r['saida'] = saida
        r['tempo'] = tempo
        r['valor'] = calcular_valor(tempo)
        r['ativo'] = False

        # limpa a tela para ficar mais limpo o programa para imprimir resultado final
        limpar_tela()

        print('\nSAÍDA FINALIZADA:')
        print('-' * 30)
        print(f"{'Placa':<8}: {r['id']}")
        print(f"{'Tipo':<8}: {r['veiculo']}")
        print(f"{'Tempo':<8}: {r['tempo']:.0f} min")
        print(f"{'Valor':<8}: R$ {r['valor']:.2f}")
        print('-' * 30)

        input('\nPressione ENTER para continuar...')
