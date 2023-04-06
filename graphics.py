import matplotlib.pyplot as plt
from textblob import TextBlob
import seaborn as sns

def barGraphic(sentimentos):
    sentimento_medio = sum(sentimentos) / len(sentimentos)
    plt.bar(["Sentimento Médio"], [sentimento_medio])
    plt.title("Sentimento Médio dos Comentários")
    plt.show()

def dipersionGraphic(sentimentos, textos):
    # Gerar um gráfico de dispersão do sentimento dos comentários em relação ao comprimento do texto
    tamanhos_textos = [len(texto) for texto in textos]
    plt.scatter(tamanhos_textos, sentimentos)
    plt.title("Sentimento em relação ao Comprimento do Texto")
    plt.xlabel("Comprimento do Texto")
    plt.ylabel("Sentimento")
    plt.show()

def pizzaGraphic(sentimentos):
    # Gerar um gráfico de pizza da proporção de textos com cada valor de sentimento
    num_positivos = len([sentimento for sentimento in sentimentos if sentimento > 0])
    num_negativos = len([sentimento for sentimento in sentimentos if sentimento < 0])
    num_neutros = len([sentimento for sentimento in sentimentos if sentimento == 0])
    labels = ["Positivos", "Negativos", "Neutros"]
    sizes = [num_positivos, num_negativos, num_neutros]
    colors = ["green", "red", "gray"]
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.title("Distribuição de Sentimentos")
    plt.show()

def warmthGraphic(palavras_chave, textos):
    # Gerar um mapa de calor de valores de sentimento em relação a palavras-chave específicas
    #palavras_chave = ["python", "data", "analysis", "machine", "learning"]
    matriz_sentimentos = []
    for palavra in palavras_chave:
        matriz_linha = []
        for texto in textos:
            if palavra in texto.lower():
                blob = TextBlob(texto)
                sentimento = blob.sentiment.polarity
                matriz_linha.append(sentimento)
            else:
                matriz_linha.append(None)
        matriz_sentimentos.append(matriz_linha)
        
    sns.heatmap(matriz_sentimentos, annot=True, xticklabels=False, yticklabels=palavras_chave)
    plt.title("Sentimento em relação a Palavras-Chave")
    plt.show()
    
def histogram(sentimentos):
    # Gerar um histograma dos valores de sentimento dos comentários
    plt.hist(sentimentos, bins=10)
    plt.title("Distribuição do Sentimento dos Comentários")
    plt.xlabel("Sentimento")
    plt.ylabel("Número de Comentários")
    plt.show()
    
def lineGraphic(sentimentos):
    # Gerar um gráfico de linha dos valores de sentimento dos comentários
    plt.plot(sentimentos)
    plt.title("Variação do Sentimento dos Comentários")
    plt.xlabel("Número de Comentários")
    plt.ylabel("Sentimento")
    plt.show()