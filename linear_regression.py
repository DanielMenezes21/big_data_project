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

    gdf.drop(columns='geometry').to_csv("dados_imoveis.csv", index=False)

df = pd.read_csv("dados_imoveis.csv")

df_reg = df[['mod_fiscal', 'num_area', 'ind_tipo']].dropna()
df_reg = pd.get_dummies(df_reg, columns=['ind_tipo'], drop_first=True)

X = df_reg.drop(columns='num_area')
y = df_reg['num_area']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
coeficientes = pd.Series(modelo.coef_, index=X.columns)

print("MSE:", mse)
print("R²:", r2)
print("\nCoeficientes:")
print(coeficientes)

import seaborn as sns
import matplotlib.pyplot as plt

corr_matrix = df_reg.copy()
corr_matrix['num_area'] = y

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Matriz de Correlação entre Variáveis")
plt.show()

