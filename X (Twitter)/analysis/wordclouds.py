import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Carregar os dados do CSV
df = pd.read_csv('seuarquivo.csv')

# Definir uma lista de palavras para exclusão
exclusion_list = ['the', 'and', 'to', 'of', 'a', 'in', 'is', 'that', 'it']

# Concatenar todos os textos em uma única string
text = ' '.join(df['text'].astype(str))

# Criar a nuvem de palavras com as palavras mais frequentes
wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=exclusion_list).generate(text)

# Plotar a nuvem de palavras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
