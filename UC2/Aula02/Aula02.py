#LDC
#ILOC
#QUERY  

import pandas as pd # alias "pd"
import numpy as np # alais "np"
# import openpyxl

filmes = {
    'titulo': ["lagoa azul", "Agente Secreto", "Gênio Indomavel", "A Freira", "Brinquedo Assassino", "Top Gun"],
    'categoria': ["romance", "ação", "Drama", "Terror", "Comedia", "Aventura"],
    'ano': ["1980", "2025", "1997", "2022", "1995", "1986"],
    'faturamento':[6, 5, 4, 5, 5, 3] 
}

indice = ["A", "B", "C", "D", "E", "F"]
tabela_filmes = pd.DataFrame(filmes, index=indice)

# print(tabela_filmes)
# print(type(tabela_filmes))
# print(tabela_filmes)
# print(type(tabela_filmes))

# print(tabela_filmes.iloc[-3])
#print("-"*20)
#print(tabela_filmes.loc['B':'F'])
#print(tabela_filmes.iloc[1:3])
consulta1 = tabela_filmes.query("faturamento == 5")
print(consulta1)
#print("-"*20)

# < > <= => == != and or not in