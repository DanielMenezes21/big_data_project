import pandas as pd

# Carrega os dados
df = pd.read_csv("dados_imoveis.csv")

# Agrupar por município e calcular estatísticas
agrupado = df.groupby('municipio').agg({
    'num_area': ['count', 'mean', 'sum'],
    'mod_fiscal': 'mean',
    'ind_tipo': lambda x: x.value_counts().index[0],   # tipo mais comum
    'ind_status': lambda x: x.value_counts().index[0]  # status mais comum
})

# Renomear colunas
agrupado.columns = [
    'qtde_imoveis',
    'area_media',
    'area_total',
    'mod_fiscal_medio',
    'tipo_mais_comum',
    'status_mais_comum'
]

# Ordenar por área total decrescente
agrupado = agrupado.sort_values(by='area_total', ascending=False)

# Exibir os primeiros resultados
print(agrupado.head(50))

import matplotlib.pyplot as plt

agrupado['area_total'].head(10).plot(kind='barh', figsize=(10, 6))
plt.title("Top 10 Municípios com Maior Área Total de Imóveis")
plt.xlabel("Área Total (ha)")
plt.ylabel("Município")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
