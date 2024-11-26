import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("ecommerce_preparados.csv")
print(df.head(20).to_string())

df.drop_duplicates(subset="Título", inplace=True)
print(df.head(20).to_string())


#df_corr = df["Nota_MinMax", "N_Avaliações_MinMax", "Desconto_MinMax", "Preço_MinMax", "Marca_Cod", "Material_Cod", "Temporada_Cod", "Qtd_Vendidos_Cod", "Marca_Freq", "Material_Freq"]].corr()
# Primeiro fiz uma analise com os dados Normalizado e tratados, logo depois olhei quais deles tinham correlações altas, tanto negativas quanto possitivas

# Logo abaixo fiz uma analise apenas com as Variantes que tem correlações altas para ter certeza.
df_corr = df[["N_Avaliações_MinMax", "Qtd_Vendidos_Cod", "Temporada_Cod", "Material_Cod",]].corr()
# Heatmap de correção
plt.figure(figsize=(9, 4))
sns.heatmap(df_corr, annot=True, fmt=".2f")
plt.title("Mapa de Calor Apenas com as Variáveis Normalizadas")
plt.xticks(rotation=0)
plt.show()

# Gráfico de Dispersão
sns.pairplot(df[["N_Avaliações_MinMax", "Qtd_Vendidos_Cod", "Temporada_Cod", "Material_Cod",]])
plt.show()

# Mapa de Calor
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
corr = df[["Temporada_Cod", "Material_Cod"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlação de Temporada e Material")

plt.subplot(1,2,2)
corr = df[["N_Avaliações_MinMax", "Qtd_Vendidos_Cod"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.xticks(rotation=0)
plt.title("Correlação de Avaliações e QTD de Vendas")
plt.tight_layout() # Ajustar espaçamentos
plt.show()


# Gráfico de Barras
plt.figure(figsize=(9, 4))
sns.countplot(y="Gênero", hue="Gênero", data=df)
plt.title("Gêneros que mais vendem")
plt.ylabel("Gênero")
plt.xlabel("Nivel de cada gênero")
plt.legend(title="Cor dos Gêneros")
plt.show()

# Gráfico em pizza
x = df["Gênero"].value_counts().index
y = df["Gênero"].value_counts().values
plt.figure(figsize=(10, 10))
plt.pie(y, labels=x, autopct="%.1f%%", startangle=90)
plt.title("Distribuição de Nível dos Gêneros")
plt.tight_layout()
plt.show()

# Gráficos de Densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df["Qtd_Vendidos_Cod"], fill=True, color="#863e9c")
plt.title("Densidade de Qtd de Vendas")
plt.xlabel("Qtd vendidas")
plt.xticks(ticks=range(0, int(df["Qtd_Vendidos_Cod"].max())+10000, 10000))
plt.show()
