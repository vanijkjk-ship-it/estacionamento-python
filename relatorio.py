# Importação de funções de outros módulos do sistema
from utilidades import limpar_tela
from exportacao.csv_export import exportar_csv
from exportacao.graficos import grafico_pizza, grafico_barras

# Função Auxiliar
# Responsável por padronizar a exibição dos dados de um veículo
def mostrar_relatorio(registros):

    def mostrar_detalhes(r):
        print('-' * 30)
        print(f"{'Placa':<8}: {r['id']}")
        print(f"{'Tipo':<8}: {r['veiculo']}")
        print(f"{'Entrada':<8}: {r['entrada']}")
        print(f"{'Saída':<8}: {r['saida']}")
        print(f"{'Tempo':<8}: {r['tempo']:.0f} min")
        print(f"{'Valor':<8}: R$ {r['valor']:.2f}")
        print('-' * 30)

    # Loop principal do relatório
    # Mantém o usuário dentro do menu até escolher sair
    while True:
        limpar_tela()

        print('\nRELATÓRIO')
        print('[1] Motocicletas')
        print('[2] Carros')
        print('[3] Caminhonetes')
        print('[4] Isentos')
        print('[5] Relatório Diário')
        print('[6] Voltar')

        opcao = input('Escolha: ').strip()
        # Filtra as motocicletas
        if opcao == '1':
            limpar_tela()
            total = 0
            encontrou = False

            print('\nMOTOCICLETAS\n')
            # Percorre registros finalizados (não ativos)
            for r in registros:
                if r['veiculo'] == 'Motocicleta' and not r['ativo']:
                    mostrar_detalhes(r)
                    total += r['valor']
                    encontrou = True

            if not encontrou:
                print('Nenhum registro encontrado.')

            print(f'\nTotal arrecadado: R$ {total:.2f}')
            input('\nENTER...')
        # Filtra os carros
        elif opcao == '2':
            limpar_tela()
            total = 0
            encontrou = False

            print('\nCARROS\n')
            # Percorre registros finalizados (não ativos)
            for r in registros:
                if r['veiculo'] == 'Carro de Passeio' and not r['ativo']:
                    mostrar_detalhes(r)
                    total += r['valor']
                    encontrou = True

            if not encontrou:
                print('Nenhum registro encontrado.')

            print(f'\nTotal arrecadado: R$ {total:.2f}')
            input('\nENTER...')
        # Filtra as caminhonetes
        elif opcao == '3':
            limpar_tela()
            total = 0
            encontrou = False

            print('\nCAMINHONETES\n')
            # Percorre registros finalizados (não ativos)
            for r in registros:
                if r['veiculo'] == 'Caminhonete' and not r['ativo']:
                    mostrar_detalhes(r)
                    total += r['valor']
                    encontrou = True

            if not encontrou:
                print('Nenhum registro encontrado.')

            print(f'\nTotal arrecadado: R$ {total:.2f}')
            input('\nENTER...')
        # Filtra veículos isentos
        elif opcao == '4':
            limpar_tela()
            total_isentos = 0
            encontrou = False

            print('\nISENTOS\n')
            # Mostra veículos que não geraram cobrança
            for r in registros:
                if r['valor'] == 0 and not r['ativo']:
                    print('-' * 30)
                    print(f"{'Placa':<8}: {r['id']}")
                    print(f"{'Tempo':<8}: {r['tempo']:.0f} min")
                    print(f"{'Status':<8}: ISENTO")
                    print('-' * 30)
                    total_isentos += 1
                    encontrou = True

            if not encontrou:
                print('Nenhum registro encontrado.')

            print(f'\nTotal de isentos: {total_isentos}')
            input('\nENTER...')

        # Relatório completo
        elif opcao == '5':
            limpar_tela()

            total = 0
            total_valor = 0
            total_isentos = 0
            # Exibe TODOS os veículos finalizados
            for r in registros:
                if not r['ativo']:
                    mostrar_detalhes(r)
                    total += 1
                    total_valor += r['valor']

                    if r['valor'] == 0:
                        total_isentos += 1

            # Consolida os dados do dia para análise rápida
            print('\nRESUMO DO DIA')
            print('-' * 30)
            print(f"Total de veículos : {total}")
            print(f"Pagantes          : {total - total_isentos}")
            print(f"Isentos           : {total_isentos}")
            print(f"Arrecadação       : R$ {total_valor:.2f}")
            print('-' * 30)
            # -----------------------------
            # MENU EXTRA (EXPORTAÇÃO E GRÁFICOS)
            # -----------------------------
            # Permite gerar arquivos e visualizações dos dados
            while True:
                print('\n[1] Exportar CSV')
                print('[2] Gráfico Pizza')
                print('[3] Gráfico Barras')
                print('[4] Voltar')

                escolha = input('Escolha: ').strip()

                if escolha == '1':
                    exportar_csv(registros)

                elif escolha == '2':
                    grafico_pizza(registros)

                elif escolha == '3':
                    grafico_barras(registros)

                elif escolha == '4':
                    break

                else:
                    print('Opção inválida!')

                input('\nENTER...')

        # Saí do relatório
        elif opcao == '6':
            break

        # Tratamento de erro
        else:
            print('Opção inválida!')
            input('\nENTER...')
