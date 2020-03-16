import pandas as pd
import numpy as np

def roa(df):
    df = df[6][1][3].replace('%', '')
    df = df.replace(',', '.')
    return float(df)


fscore = 0

tick = str(input('Digite o ticker do ativo: ')).upper()

link = 'https://www.investsite.com.br/principais_indicadores.php?cod_negociacao=' + tick
df = pd.read_html(link)
 
if roa(df) > 0:
    fscore += 1

print(f'F-Score de Piotroski para o ativo {tick} é igual a {fscore}')
