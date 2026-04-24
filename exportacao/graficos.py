# Biblioteca para criação de gráficos (visualização de dados)
# Esse é um bonus para ter outras formas de ver os dados
import matplotlib.pyplot as plt

#Prepara os dados
def preparar_dados(registros):
    # Contagem de veículos por tipo
    tipos = {
        'Motocicleta': 0,
        'Carro de Passeio': 0,
        'Caminhonete': 0
    }
    # Soma de valores arrecadados por tipo
    valores = {
        'Motocicleta': 0,
        'Carro de Passeio': 0,
        'Caminhonete': 0
    }
    # Percorre os registros finalizados (não ativos)
    for r in registros:
        if not r['ativo']:
            tipos[r['veiculo']] += 1
            valores[r['veiculo']] += r['valor']

    return tipos, valores

# Gráfico de Pizza
def grafico_pizza(registros):
    tipos, _ = preparar_dados(registros)

    labels = []
    dados = []
    # Filtra apenas tipos com valores > 0
    for k, v in tipos.items():
        if v > 0:
            labels.append(k)
            dados.append(v)
    # Evita gráfico vazio
    if not dados:
        print('Sem dados.')
        return
    # Gera gráfico de distribuição
    plt.pie(dados, labels=labels, autopct='%1.1f%%')
    plt.title('Tipos de veículos')
    plt.show()

# Gráfico de Barras
def grafico_barras(registros):
    _, valores = preparar_dados(registros)

    labels = list(valores.keys())
    dados = list(valores.values())
    # Evita gráfico vazio
    if sum(dados) == 0:
        print('Sem dados.')
        return
    # Gera gráfico de arrecadação
    plt.bar(labels, dados)
    plt.title('Arrecadação por tipo de veículo')
    plt.xlabel('Tipo de veículo')
    plt.ylabel('Valor (R$)')
    plt.show()
