import psycopg2
import os
from dotenv import load_dotenv
from valorizacao_acoes import calcular_valorizacoes, obter_dados_acoes
import pandas as pd

def salvar_dados(df):
    load_dotenv()

    conexao = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT", "5432")
    )
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dados_acoes (
            ticker TEXT NOT NULL,
            data DATE NOT NULL,
            open NUMERIC,
            high NUMERIC,
            low NUMERIC,
            close NUMERIC,
            volume BIGINT,
            valorizacao_dia NUMERIC,
            valorizacao_acumulada NUMERIC,
            PRIMARY KEY (ticker, data)
        );
    """)

    insert_query = """
        INSERT INTO dados_acoes (
            ticker, data, open, high, low, close, volume,
            valorizacao_dia, valorizacao_acumulada
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (ticker, data) DO NOTHING;
    """

    dados = [
        (
            row['ticker'], row['data'], row['open'], row['high'], row['low'],
            row['close'], row['volume'], row['valorizacao_dia'], row['valorizacao_acumulada']
        )
        for _, row in df.iterrows()
    ]

    cursor.executemany(insert_query, dados)
    conexao.commit()
    cursor.close()
    conexao.close()
    print(f"{len(dados)} registros inseridos na tabela dados_acoes.")

    # Salvar como CSV
    df.to_csv("dados_acoes.csv", index=False)
    print("Arquivo 'dados_acoes.csv' salvo com sucesso.")


if __name__ == "__main__":
    with open("tickers_validos.txt", "r") as f:
        tickers = [linha.strip() for linha in f if linha.strip()]

    dados = obter_dados_acoes(tickers)
    df = calcular_valorizacoes(dados)
    salvar_dados(df)
