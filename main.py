import pandas as pd


def buscar_coluna_por_nome(planilha, nome):
    df = pd.read_excel(planilha, header=None)  # Lê a planilha sem considerar a primeira linha como cabeçalho

    # Busca o nome na primeira linha

    for coluna in df.columns:
        if df[coluna][0] == nome:
            return coluna + 1  # Retorna o número da coluna (começando em 1)
        return None  # Retorna None caso o nome não seja encontrado

# Exemplo de uso

planilha = 'C:\ws-intellij\Python\Consumindo planilhas\Teste.ods'  # Substitua pelo caminho correto da sua planilha
nome_buscado = 'Placa'
coluna = buscar_coluna_por_nome(planilha, nome_buscado)

if coluna is not None:
    print(f'O nome "{nome_buscado}" está na coluna {coluna}.')
else:
    print(f'O nome "{nome_buscado}" não foi encontrado na planilha.')


class veiculo:
    def __init__(self, placa, renavam, chassi, uf):
        self.placa = placa
        self.renavam = renavam
        self.chassi = chassi
        self.uf = uf

