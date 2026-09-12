import pandas as pd

df_transacoes = pd.read_excel('base_invest.xlsx', sheet_name= 'Transacoes')
df_ativos = pd.read_excel('base_invest.xlsx', sheet_name= 'Ativo')


df_compra = df_transacoes[df_transacoes['operacao'] == 'compra']
df_venda = df_transacoes[df_transacoes['operacao'] == 'venda']


max_compra_preco = df_compra['preco'].max()
min_compra_preco = df_compra['preco'].min()
max_venda_preco = df_venda['preco'].max()
min_venda_preco = df_venda['preco'].min()

#print(max_compra_preco)
df_transacoes['valor_total'] = df_transacoes['quantidade'] * df_transacoes['preco']
print(df_transacoes)
valor_por_ativo = df_transacoes.groupby('id_ativo')['valor_total'].sum()
id_ativo_maior_valor = valor_por_ativo.idxmax()
print(valor_por_ativo)

cnpj_maior_valor = df_ativos[df_ativos['id_ativo'] == id_ativo_maior_valor]['cnpj'].iloc[0]

print(f"O CNPJ para o ativo com maior valor é: {cnpj_maior_valor}")

valor_por_participante = df_transacoes.groupby('id_participantes')
