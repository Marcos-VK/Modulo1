import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.width', None)

df = pd.read_csv("D:\marcos_vk\ebac\ecommerce_preparados.csv")
print(df.head())
# Tratamento Dados
df['Gênero'] = df['Gênero'].apply(lambda x: 'Infantil' if x == 'Sem gênero infantil' else x)
df['Gênero'] = df['Gênero'].apply(lambda x: 'Unissex' if x == 'Sem gênero' else x)
df['Desconto'] = df['Desconto'].fillna(0.0)
# Filtrar apenas gêneros desejados
df_filtrado = df[df['Gênero'].isin(['Masculino', 'Feminino', 'Bebês', 'Infantil', 'Unissex'])]
print(df['Gênero'])
#Grafico de Barras
top_marcas = df_filtrado['Marca'].value_counts().head(10).index
df_top = df_filtrado[df_filtrado['Marca'].isin(top_marcas)]
ordem_marcas = df_top['Marca'].value_counts().index
plt.figure(figsize=(10, 6))
grafico1= sns.countplot(x='Marca', hue='Gênero', data=df_top, order=ordem_marcas)
    # Adiciona contagem em cima de cada barra
for container in grafico1.containers:
    grafico1.bar_label(container, label_type='edge', fontsize=9, padding=2)
plt.title('Distribuição das Top10 Marcas por Gênero')
plt.xlabel('Marca')
plt.xticks(rotation=45)
plt.tight_layout()
plt.ylabel('Quantidade')
plt.show()

# Contar notas nas top 10 marcas
notas_counts = df_top['Nota'].value_counts().sort_index()
x = notas_counts.index     # Labels: as notas (ex: 1, 2, 3, ...)
y = notas_counts.values    # Valores: quantidade de cada nota
    # Calcular média das notas por marca
media_notas_por_marca = df_top.groupby('Marca')['Nota'].mean().sort_values(ascending=False)
    # Separar dados para o gráfico
labels = media_notas_por_marca.index
sizes = media_notas_por_marca.values
    # Criar gráfico de pizza
plt.figure(figsize=(10, 6))
plt.pie(sizes, labels=None, autopct='%1.1f%%', startangle=90)
    # Adicionar legenda com nomes das marcas
plt.legend(labels, title='Marcas', loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('Participação das Marcas por Nota Média (Top 10)')
plt.tight_layout()
plt.show()

#Grafico de Dispersão
sns.jointplot(x='Preço',y='Qtd_Vendidos_Cod', data=df, kind='scatter')
plt.tight_layout()
plt.show()

#Histograma - Parâmetros
plt.figure(figsize = (10,6))
plt.hist(df['Preço'], bins = 40, color = 'green', alpha = 0.8) # alpha(transparência)
plt.title('Histograma - Distribuição de Preços')
plt.xlabel('Preço')
plt.xticks(ticks = range(0, int(df['Preço'].max())+30, 30))
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

#Gráfico Densidade
plt.figure(figsize = (10,6))
sns.kdeplot(df['Preço'], fill=True, color='#863e9c')
plt.title('Densidade Preço')
plt.xlabel('Preço')
plt.show()

#Mapa de Calor
corr = df[['Desconto', 'Qtd_Vendidos_Cod']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correção Desconto e Vendas')
plt.tight_layout()
plt.show()

#Gráfico de Regressão
sns.regplot(x='Nota',y='Qtd_Vendidos_Cod', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color':'#34c289'})
plt.title('Regressão de Nota por Vendas')
plt.xlabel('Nota')
plt.ylabel('Vendas')
plt.show()