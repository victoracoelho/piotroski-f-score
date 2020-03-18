import pandas as pd
import numpy as np


### FUNÇÃO PARA TRANSFORMAR O ROA DE STRING PARA FLOAT
def roa(df):
    df = df[6][1][3].replace('%', '')
    df = df.replace(',', '.')
    return float(df)


### FUNÇÃO PARA TRANSFORMAR O FCO DE STRING PARA FLOAT
def fco(df2):
    fco = df2[1]
    fco = fco['01/01/2019 a 31/12/2019 (R$ mil)'][1]
    fco = fco.replace('.', '')
    return float(fco)


### FUNÇÃO PARA TRANSFORMAR AS VARIÁVEIS PARA FLOAT E FAZER O CÁLCULO DA VARIAÇÃO DO ROA
def roa_var(df3, df4):
    dre = df3[1]
    bp = df4[1]
    dre1 = float(dre['01/01/2019 a 31/12/2019 (R$ mil)'][34].replace('.', ''))
    dre2 = float(dre['01/01/2018 a 31/12/2018 (R$ mil)'][34].replace('.', ''))
    bp1 = float(bp['31/12/2019 (R$ mil)'][1].replace('.', ''))
    bp2 = float(bp['31/12/2018 (R$ mil)'][1].replace('.', ''))
    roa_var = (dre1/bp1) - (dre2/bp2)
    return roa_var

################## CONSERTAR FUNÇÕES ABAIXO ##################
def lucroliq(df):
    lucro = df[3][1][5].replace('R$', '')
    lucro = lucro.replace('B', '')
    lucro = lucro.replace(',', '.')
    lucro = lucro.replace('M', '')
    if '-' in lucro:
        lucro = lucro.replace('-', '')
        float(lucro)
        lucro = 0 - lucro
        return lucro
    else:
        return float(lucro)


def alavancagem(df4, df5):
    divida = df5[1]
    ativos = df4[1]
    divida1 = float(divida['31/12/2019 (R$ mil)'][47].replace('.', ''))
    divida2 = float(divida['31/12/2018 (R$ mil)'][47].replace('.', ''))
    ativos1 = float(ativos['31/12/2019 (R$ mil)'][1].replace('.', ''))
    ativos2 = float(ativos['31/12/2018 (R$ mil)'][1].replace('.', ''))
    alav = (ativos1 / divida1) - (ativos2 / divida2)
    return alav
################################################### PROGRAMA PRINCIPAL ###################################################

fscore = 0

tick = str(input('Digite o ticker do ativo: ')).upper()

link = 'https://www.investsite.com.br/principais_indicadores.php?cod_negociacao=' + tick
df = pd.read_html(link)

link2 = 'https://www.investsite.com.br/fluxo_caixa.php?cod_negociacao=' + tick
df2 = pd.read_html(link2)

link3 = 'https://www.investsite.com.br/demonstracao_resultado.php?cod_negociacao=' + tick
df3 = pd.read_html(link3)

link4 = 'https://www.investsite.com.br/balanco_patrimonial_ativo.php?cod_negociacao=' + tick
df4 = pd.read_html(link4)
 
link5 = 'https://www.investsite.com.br/balanco_patrimonial_passivo.php?cod_negociacao=' + tick
df5 = pd.read_html(link5)

if roa(df) > 0:
    fscore += 1

if fco(df2) > 0:
    fscore += 1

if roa_var(df3, df4) > 0:
    fscore += 1

if (fco(df2) / 1000000) > lucroliq(df):
    fscore += 1


print(f'F-Score de Piotroski para o ativo {tick} é igual a {fscore}')

print(alavancagem(df4, df5))
