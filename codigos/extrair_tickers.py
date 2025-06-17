import requests
import yfinance as yf
import time

def obter_tickers_b3_validos(volume_minimo=5_000_000):
    url = "https://brapi.dev/api/quote/list?range=10000"
    response = requests.get(url)
    data = response.json()

    tickers_validos = []

    print("Verificando tickers de ações da B3 com liquidez mínima de R$", f"{volume_minimo:,}".replace(",", "."))

    for acao in data["stocks"]:
        ticker_base = acao.get("stock", "")
        tipo = acao.get("type", "")
        volume = acao.get("volume", 0)

        if tipo != "stock":
            continue 

        ticker = ticker_base + ".SA"

        if volume and volume >= volume_minimo:
            try:
                dados = yf.download(ticker, period="5d", progress=False)
                if not dados.empty:
                    tickers_validos.append(ticker)
                    print(f"{ticker} - OK")
                else:
                    print(f"{ticker} - sem dados no yfinance")
            except Exception as e:
                print(f"{ticker} - erro: {e}")

            time.sleep(0.2)

    print(f"\nTotal de tickers válidos: {len(tickers_validos)}")
    return tickers_validos

if __name__ == "__main__":
    tickers = obter_tickers_b3_validos()

    with open("tickers_validos.txt", "w") as f:
        for ticker in tickers:
            f.write(f"{ticker}\n")

    print("\nTickers salvos em 'tickers_validos.txt'")
