import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0

    for i in range(1, 6):
        soma += abs(as_a[i] - as_b[i])
    grau = soma / 6
    if grau < 0:
        grau = grau * (-1)

    return grau


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []

    for sentenca in sentencas:
        fs = separa_frases(sentenca)
        frases.extend(fs)
        for frase in fs:
            palavras.extend(separa_palavras(frase))

    total_caracteres_palavras = sum(len(p) for p in palavras)
    total_palavras = len(palavras)
    total_palavras_diferentes = n_palavras_diferentes(palavras)
    total_palavras_unicas = n_palavras_unicas(palavras)

    total_caracteres_sentencas = sum(len(s) for s in sentencas)
    total_frases = len(frases)
    total_caracteres_frases = sum(len(f) for f in frases)

    wal = total_caracteres_palavras / total_palavras if total_palavras else 0
    ttr = total_palavras_diferentes / total_palavras if total_palavras else 0
    hlr = total_palavras_unicas / total_palavras if total_palavras else 0
    sal = total_caracteres_sentencas / len(sentencas) if sentencas else 0
    sac = total_frases / len(sentencas) if sentencas else 0
    pal = total_caracteres_frases / total_frases if total_frases else 0

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    similaridades = []
    for texto in textos:
        assinatura = calcula_assinatura(texto)
        similaridade = compara_assinatura(assinatura, ass_cp)
        similaridades.append(similaridade)

    return similaridades.index(min(similaridades)) + 1