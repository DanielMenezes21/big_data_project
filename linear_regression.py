import geopandas as gpd
import pandas as pd
import datetime as dt
import os
import re
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

if not os.path.exists("dados_imoveis.csv"):
    gdf = gpd.read_file("AREA_IMOVEL_1.shp")

    # Converter para DataFrame e salvar como CSV
    gdf.drop(columns='geometry').to_csv("dados_imoveis.csv", index=False)

# Carregar dados
df = pd.read_csv("dados_imoveis.csv")

# Preparar dados
df_reg = df[['mod_fiscal', 'num_area', 'ind_tipo']].dropna()
df_reg = pd.get_dummies(df_reg, columns=['ind_tipo'], drop_first=True)

# Definir variáveis
X = df_reg.drop(columns='num_area')
y = df_reg['num_area']

# Dividir treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Criar modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Prever e avaliar
y_pred = modelo.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
coeficientes = pd.Series(modelo.coef_, index=X.columns)

print("MSE:", mse)
print("R²:", r2)
print("\nCoeficientes:")
print(coeficientes)

