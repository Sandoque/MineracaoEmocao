import nltk

# nltk.download()

base = [('eu sou admirada por muitos','alegria'),
        ('me sinto completamente amado','alegria'),
        ('amar e maravilhoso','alegria'),
        ('estou me sentindo muito animado novamente','alegria'),
        ('eu estou muito bem hoje','alegria'),
        ('que belo dia para dirigir um carro novo','alegria'),
        ('o dia está muito bonito','alegria'),
        ('estou contente com o resultado do teste que fiz no dia de ontem','alegria'),
        ('o amor e lindo','alegria'),
        ('nossa amizade e amor vai durar para sempre', 'alegria'),
        ('estou amedrontado', 'medo'),
        ('ele esta me ameacando a dias', 'medo'),
        ('isso me deixa apavorada', 'medo'),
        ('este lugar e apavorante', 'medo'),
        ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'medo'),
        ('tome cuidado com o lobisomem', 'medo'),
        ('se eles descobrirem estamos encrencados', 'medo'),
        ('estou tremendo de medo', 'medo'),
        ('eu tenho muito medo dele', 'medo'),
        ('estou com medo do resultado dos meus testes', 'medo')]

stopwords = nltk.corpus.stopwords.words('portuguese')

# def removestopwords(texto):
#     frases = []
#     for (palavras, emocao) in texto:
#             semstop = [p for p in palavras.split() if p not in stopwords]
#             frases.append((semstop, emocao))
#     return frases


def aplica_stemmer(texto):
  stemmer = nltk.stem.RSLPStemmer()
  frases_stemming = []
  for (palavras, emocao) in texto:
    com_stemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stopwords]
    frases_stemming.append((com_stemming, emocao))
  return frases_stemming

frases_com_stemming = aplica_stemmer(base)

print(frases_com_stemming)