import pandas as pd
from acoes_dados import obter_dados_acoes

def calcular_valorizacoes(dados):
    df = pd.DataFrame(dados)
    df = df.sort_values(by=['ticker', 'data'])

    df['valorizacao_dia'] = df.groupby('ticker')['close'].pct_change().round(2)
    df['valorizacao_acumulada'] = df.groupby('ticker')['close'].transform(lambda x: (x / x.iloc[0] - 1)).round(2)

    return df

if __name__ == "__main__":
    with open("tickers_validos.txt", "r") as f:
        tickers = [linha.strip() for linha in f if linha.strip()]

    dados = obter_dados_acoes(tickers)
    df_valorizacoes = calcular_valorizacoes(dados)

    print(df_valorizacoes.head())
