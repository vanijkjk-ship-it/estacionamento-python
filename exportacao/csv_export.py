# Módulo do sistema operacional (usado para abrir o arquivo automaticamente)
import os

# Exportação de Relatório
def exportar_csv(registros):
    # Nome do arquivo que será gerado
    nome_arquivo = 'relatorio.csv'

    # Abre (ou cria) o arquivo em modo escrita
    # encoding='utf-8' garante compatibilidade com acentos
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        # Escreve o cabeçalho da planilha
        f.write('Placa;Tipo;Entrada;Saida;Tempo;Valor\n')
        # Percorre apenas registros finalizados (não ativos)
        for r in registros:
            if not r['ativo']:
                # Escreve os dados separados por ponto e vírgula (formato CSV)
                f.write(f"{r['id']};{r['veiculo']};{r['entrada']};{r['saida']};{r['tempo']};{r['valor']}\n")

    print('\nRelatório exportado com sucesso!')

    # Abre automático para visualização
    try:
        os.startfile(nome_arquivo)
    except Exception as e:
        # Caso o sistema não suporte (Linux/Mac ou erro), informa ao usuário
        print(f'Não foi possível abrir automaticamente: {e}')
