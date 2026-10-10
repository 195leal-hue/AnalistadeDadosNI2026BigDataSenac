import pandas as pd

# Dataset 1
df1 = pd.read_csv("C:/Users/lucas.llima/Documents/BIGDATA/AnalistadeDadosNI2026BigDataSenac/netflix_titles.csv")

# Renomear colunas
df1 = df1.rename(columns={
    "show_id": "id",
    "country": "country"
})

# Dataset 2
df2 = pd.read_csv("C:/Users/lucas.llima/Documents/BIGDATA/AnalistadeDadosNI2026BigDataSenac/titles_netflix_limpo.csv")

# Renomear colunas
df2 = df2.rename(columns={
    "production_countries": "country"
})

# Salvar versões corrigidas
df1.to_csv(
    "netflix_titles01_corrigido.csv",
    index=False,
    encoding="utf-8"
)

df2.to_csv(
    "titles_netflix_02corrigido.csv",
    index=False,
    encoding="utf-8"
)

print("Arquivos corrigidos criados!")