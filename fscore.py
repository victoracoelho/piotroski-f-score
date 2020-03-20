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
    listafco = ['01/01/2019 a 31/12/2019 (R$ mil)', '01/01/2019 a 30/09/2019 (R$ mil)']
    for pos in listafco:
        if pos in fco:
            fco = fco[pos][1].replace('.', '')
    return float(fco)


### FUNÇÃO PARA TRANSFORMAR AS VARIÁVEIS PARA FLOAT E FAZER O CÁLCULO DA VARIAÇÃO DO ROA
def roa_var(df3, df4):
    dre = df3[1]
    bp = df4[1]
    listadre = list(dre['Descrição'])
    for c, v in enumerate(listadre):
        if v == 'Lucro/Prejuízo Consolidado do Período':
            if '01/01/2019 a 31/12/2019 (R$ mil)' in dre:
                dre1 = float(dre['01/01/2019 a 31/12/2019 (R$ mil)'][c].replace('.', ''))
            elif '01/01/2019 a 30/09/2019 (R$ mil)' in dre:
                dre1 = float(dre['01/01/2019 a 30/09/2019 (R$ mil)'][c].replace('.', ''))
            if '01/01/2018 a 31/12/2018 (R$ mil)' in dre:
                dre2 = float(dre['01/01/2018 a 31/12/2018 (R$ mil)'][c].replace('.', ''))
            elif '01/01/2018 a 30/09/2018 (R$ mil)' in dre:
                dre2 = float(dre['01/01/2018 a 30/09/2018 (R$ mil)'][c].replace('.', ''))
    if '31/12/2019 (R$ mil)' in bp:
        bp1 = float(bp['31/12/2019 (R$ mil)'][1].replace('.', ''))
    elif '30/09/2019 (R$ mil)' in bp:
        bp1 = float(bp['30/09/2019 (R$ mil)'][1].replace('.', ''))
    if '31/12/2018 (R$ mil)' in bp:
        bp2 = float(bp['31/12/2018 (R$ mil)'][1].replace('.', ''))
    elif '30/09/2018 (R$ mil)' in bp:
        bp2 = float(bp['30/09/2018 (R$ mil)'][1].replace('.', ''))
    roa_var = (dre1/bp1) - (dre2/bp2)
    return roa_var


def lucroliq(df):
    lucro = df[3][1][5].replace('R$', '')
    lucro = lucro.replace('B', '')
    lucro = lucro.replace(',', '.')
    lucro = lucro.replace('M', '')
    lucro = lucro.replace('-', '')
    return float(lucro.strip())


def alavancagem(df):
    divida = df[7]
    divida = divida[1][5]
    divida = divida.replace('R$', '')
    divida = divida.replace(',', '.')
    divida = divida.replace('B', '')
    divida = divida.replace('M', '')
    if '-' in divida:
        divida = float(divida.replace('-', ''))
        divida = 0 - divida
    else:
        divida = float(divida)
    ebitda = df[3]
    ebitda = ebitda[1][4]
    ebitda = ebitda.replace('R$', '')
    ebitda = ebitda.replace(',', '.')
    ebitda = ebitda.replace('B', '')
    ebitda = ebitda.replace('M', '')
    if '-' in ebitda:
        ebitda = float(ebitda.replace('-', ''))
        ebitda = 0 - ebitda
    else:
        ebitda = float(ebitda)
    alav = divida / ebitda
    return alav


def liqcorr(df4, df5):
    listaliq19 = ['30/09/2019 (R$ mil)', '31/12/2019 (R$ mil)']
    listaliq18 = ['30/09/2018 (R$ mil)', '31/12/2018 (R$ mil)']
    ativo = df4[1]
    passivo = df5[1]
    for pos in listaliq19:
        if pos in ativo:
            ativo1 = float(ativo[pos][2].replace('.', ''))
        if pos in passivo:
            passivo1 = float(passivo[pos][2].replace('.', ''))
    for pos in listaliq18:
        if pos in ativo:
            ativo2 = float(ativo[pos][2].replace('.', ''))
        if pos in passivo:
            passivo2 = float(passivo[pos][2].replace('.', ''))
    liqcorr = (ativo1 / passivo1) - (ativo2 / passivo2)
    return liqcorr


def acoes(df):
    acoes = df[7]
    lista_acoes = list(acoes[0])
    for c, v in enumerate(lista_acoes):
        if v == 'Quant. Ações Ordinárias':
            acoeson = float(acoes[1][c].replace('.', ''))
        if v == 'Quant. Ações Preferenciais':
            acoespn = float(acoes[1][c].replace('.', ''))
    acoes_var = acoeson - acoespn
    return acoes_var


def margem(df):
    margem = df[6]
    listamargem = list(margem[0])
    for c, v in enumerate(listamargem):
        if v == 'Margem Bruta':
            margembt = (margem[1][c].replace('%', ''))
            margembt = (margembt.replace(',', '.'))
    return float(margembt)


def giro(df3, df4):
    lista_receita19 = ['01/01/2019 a 31/12/2019 (R$ mil)', '01/01/2019 a 30/09/2019 (R$ mil)']
    lista_receita18 = ['01/01/2018 a 30/09/2018 (R$ mil)', '01/01/2018 a 31/12/2018 (R$ mil)']
    lista_ativo19 = ['30/09/2019 (R$ mil)', '31/12/2019 (R$ mil)']
    lista_ativo18 = ['30/09/2018 (R$ mil)', '31/12/2018 (R$ mil)']
    receita = df3[1]
    ativo = df4[1]
    for pos in lista_receita19:
        if pos in receita:
            receita19 = float(receita[pos][1].replace('.', ''))
    for pos in lista_receita18:
        if pos in receita:
            receita18 = float(receita[pos][1].replace('.', ''))
    for pos in lista_ativo19:
        if pos in ativo:
            ativo19 = float(ativo[pos][1].replace('.', ''))
    for pos in lista_ativo18:
        if pos in ativo:
            ativo18 = float(ativo[pos][1].replace('.', ''))
    giro = (receita19 / ativo19) - (receita18 / ativo18)
    return giro


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

if fco(df2) > (lucroliq(df) * 1000000):
    fscore += 1

if alavancagem(df) < 3:
    fscore += 1

if liqcorr(df4, df5) > 0:
    fscore += 1

if acoes(df) > 0:
    fscore += 1

if margem(df) > 15.0:
    fscore += 1

if giro(df3, df4) > 0:
    fscore += 1

print(f'F-Score de Piotroski para o ativo {tick} é igual a {fscore}')
