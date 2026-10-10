import pandas as pd

# Ler arquivo
df = pd.read_csv(
    "C:/Users/lucas.llima/Documents/BIGDATA/AnalistadeDadosNI2026BigDataSenac/titles_netflix.csv",
    encoding="utf-8"
)

# Remover espaços dos nomes das colunas
df.columns = df.columns.str.strip()

# Remover linhas totalmente vazias
df = df.dropna(how="all")

# Remover registros duplicados
df = df.drop_duplicates()

# Substituir valores nulos
df["imdb_score"] = df["imdb_score"].fillna(0)
df["tmdb_score"] = df["tmdb_score"].fillna(0)
df["imdb_votes"] = df["imdb_votes"].fillna(0)

# Salvar novo CSV
df.to_csv(
    "titles_netflix_limpo.csv",
    index=False,
    encoding="utf-8"
)

print("Arquivo corrigido criado com sucesso!")
print(df.shape)