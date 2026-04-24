from utilidades import limpar_tela
from cadastro import cadastrar_veiculo
from saida import registrar_saida
from relatorio import mostrar_relatorio
from ativos import mostrar_ativos

# LISTA DE REGISTROS

registros = []

# LOOP PRINCIPAL
while True:

    limpar_tela()

    print('-=-' * 20)
    print('Estacionamento UniCesumar Parking'.center(60))
    print('-=-' * 20)
    print()

    print('MENU\n')
    print('[1] Cadastro')
    print('[2] Saída de Veículo')
    print('[3] Relatório')
    print('[4] Ativos')
    print('[5] Sair')
    print()

    opcao = input('Opção: ').strip()

    # CADASTRO
    if opcao == '1':

        while True:
            limpar_tela()

            registro = cadastrar_veiculo()

            # 🔒 bloqueio de duplicado ativo
            if any(r['id'] == registro['id'] and r['ativo'] for r in registros):
                print('\nERRO: Veículo já está no estacionamento!')
                input('\nENTER...')
                continue

            registros.append(registro)

            print('\nVEÍCULO CADASTRADO COM SUCESSO!')
            print(f"Placa  : {registro['id']}")
            print(f"Tipo   : {registro['veiculo']}")
            print(f"Entrada: {registro['entrada']}")

            continuar = input('\nCadastrar outro? (S/N): ').strip().upper()

            if continuar != 'S':
                break

    # SAÍDA
    elif opcao == '2':

        if not any(r['ativo'] for r in registros):
            print('Nenhum veículo no estacionamento!')
            input('\nENTER...')
            continue

        registrar_saida(registros)

    # RELATÓRIO
    elif opcao == '3':
        mostrar_relatorio(registros)

    # ATIVOS
    elif opcao == '4':
        mostrar_ativos(registros)
        input('\nENTER...')

    # SAIR
    elif opcao == '5':
        limpar_tela()
        print('\nEncerrando o sistema...')
        break

    # OPÇÃO INVÁLIDA
    else:
        print('Opção inválida!')
        input('\nENTER...')
