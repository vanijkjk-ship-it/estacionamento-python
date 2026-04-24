# Módulo utilizado para manipulação de dados do sistema
from utilidades import validar_horario, validar_placa, agora

def cadastrar_veiculo():
    # Loop garante que o usuário só sai com uma opção válida
    while True:
        print('Tipo de veículo:')
        print('[1] Motocicleta')
        print('[2] Carro de Passeio')
        print('[3] Caminhonete')

        opcao = input('Escolha: ').strip()

        if opcao == '1':
            veiculo = 'Motocicleta'
            break
        elif opcao == '2':
            veiculo = 'Carro de Passeio'
            break
        elif opcao == '3':
            veiculo = 'Caminhonete'
            break
        else:
            print('Opção inválida!')

    # Identificação
    # Aqui você trata dois cenários diferentes de entrada
    while True:
        tem_placa = input('Possui placa? (S/N): ').strip().upper()
        # CASO TENHA PLACA
        if tem_placa == 'S':

            while True:
                identificador = input('Digite a placa: ').strip().upper()

                if not identificador:
                    print('Placa não pode ser vazia!')
                    continue

                if validar_placa(identificador):
                    break
                else:
                    print('Placa inválida! Use ABC1234 ou ABC1D23')

            break
        # CASO NÃO TENHA PLACA (CHASSI)
        elif tem_placa == 'N':

            while True:
                identificador = input('Digite os 6 primeiros números do chassi: ').strip()

                if not identificador:
                    print('Chassi não pode ser vazio!')
                    continue

                if identificador.isdigit() and len(identificador) == 6:
                    break
                else:
                    print('Digite exatamente 6 números.')

            break

        else:
            print('Digite S ou N.')

    # Definição do horário de entrada
    # Permite automático (sistema) ou manual (usuário)
    while True:
        print('\n[1] Digitar horário')
        print('[2] Usar horário atual')

        escolha = input('Escolha: ').strip()
        # HORÁRIO AUTOMÁTICO
        if escolha == '2':
            entrada = agora()

            if not validar_horario(entrada):
                print('Horário atual fora do funcionamento (08h às 18h).')
                input('\nENTER para tentar novamente...')
                continue

            print(f'Entrada automática: {entrada}')
            break
        # HORÁRIO MANUAL
        elif escolha == '1':
            entrada = input('Hora de entrada (HH:MM:SS): ').strip()

            if validar_horario(entrada):
                break
            else:
                print('Formato inválido ou fora do horário permitido (08h às 18h).')
                input('\nENTER para tentar novamente...')

        else:
            print('Opção inválida!')

    # RETORNO DO REGISTRO
    # Estrutura padrão usada
    return {
        'veiculo': veiculo,
        'id': identificador,
        'entrada': entrada,
        'saida': None,
        'tempo': 0,
        'valor': 0,
        'ativo': True
    }
