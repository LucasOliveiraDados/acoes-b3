
# ACOES_BRASILEIRAS

Projeto para extração, análise e armazenamento de dados de ações da B3 com foco em liquidez mínima e valorização recente.

## 📁 Estrutura do Projeto

```plaintext
ACOES_BRASILEIRAS/
├── codigos/
│   ├── extrair_tickers.py         # Filtra ações com liquidez diária ≥ R$ 5 milhões (API brapi.dev)
│   ├── acoes_dados.py             # Extrai dados diários de cotações com yfinance
│   ├── valorizacao_acoes.py       # Calcula valorização diária e acumulada
│   ├── salvar_dados_acoes.py      # Armazena os dados em PostgreSQL e exporta CSV
│   └── conexao_banco.py           # Estabelece conexão via variáveis de ambiente (.env)
├── main.py                        # Executa o pipeline completo (tickers + dados + banco + CSV)
├── tickers_validos.txt            # Lista de ações válidas extraídas da API
├── .env                           # Variáveis de ambiente para conexão com o banco (não versionado)
├── requirements.txt               # Dependências do projeto
```


## 🔄 ETL – Extração, Transformação e Carga dos Dados

O pipeline do projeto ACOES_BRASILEIRAS segue a arquitetura ETL, sendo dividido em três etapas principais:

### 🟢 Etapa 1 – Extração

**Objetivo:** Coletar os dados brutos das ações brasileiras com base em critérios mínimos de liquidez.

- `extrair_tickers.py`: usa API brapi.dev para selecionar ações com liquidez ≥ R$ 5 milhões
- `acoes_dados.py`: extrai dados de cotações via yfinance dos tickers válidos

### 🟡 Etapa 2 – Transformação

**Objetivo:** Enriquecer os dados com métricas analíticas para avaliação do desempenho das ações.

- `valorizacao_acoes.py`: calcula valorização diária e acumulada com arredondamento de 2 casas

### 🟠 Etapa 3 – Carga

**Objetivo:** Armazenar os dados transformados.

- `salvar_dados_acoes.py` grava:
  - No PostgreSQL: tabela `dados_acoes`
  - Em CSV local: `dados_acoes.csv`

Execução manual:

```bash
python codigos/extrair_tickers.py
python codigos/salvar_dados_acoes.py
```

Ou execução total via:

```bash
python main.py
```

---

## 📊 Dashboard Power BI

O arquivo `dados_acoes.csv` é utilizado como fonte para análises no Power BI, incluindo:
- Média de valorização acumulada (vs. meta da Selic)
- % de ações com variação positiva (vs. meta de 50%)
- Média de volume diário
- Evolução comparativa por ticker
- Rankings de valorização e volume

---

## 👨‍💻 Autor

Lucas Oliveira  
[github.com/LucasOliveiraDados](https://github.com/LucasOliveiraDados)
