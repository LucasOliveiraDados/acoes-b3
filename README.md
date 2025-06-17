# ACOES_BRASILEIRAS

Projeto para extração, análise e armazenamento de dados de ações da B3 com foco em liquidez mínima e valorização recente.

## Estrutura do Projeto

```plaintext
ACOES_BRASILEIRAS/
├── codigos/
│   ├── extrair_tickers.py         # Filtra ações com liquidez diária ≥ R$ 5 milhões (API brapi.dev)
│   ├── acoes_dados.py             # Extrai dados diários de cotações com yfinance
│   ├── valorizacao_acoes.py       # Calcula valorização diária e acumulada
│   ├── salvar_dados_acoes.py      # Armazena os dados em PostgreSQL e exporta CSV
│   └── conexao_banco.py           # Estabelece conexão via variáveis de ambiente (.env)
├── tickers_validos.txt            # Lista de ações válidas extraídas da API
├── .env                           # Variáveis de ambiente para conexão com o banco (não versionado)
├── requirements.txt               # Dependências do projeto
```

## Pré-requisitos

- Python 3.10+
- PostgreSQL
- Conta no GitHub (para clonar o projeto)

---

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/LucasOliveiraDados/ACOES_BRASILEIRAS.git
cd ACOES_BRASILEIRAS
```

2. (Opcional) Crie o ambiente virtual:
```bash
python -m venv .venv
.venv\Scripts\activate  # no Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o `.env` com os dados de conexão ao PostgreSQL:
```ini
DB_HOST=localhost
DB_NAME=seu_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_PORT=5432
```

---

## Execução

Forma rápida (pipeline completo):
```bash
python main.py
```


---

## Saídas

- **Banco de dados**: tabela `dados_acoes` no PostgreSQL.
- **Arquivo local**: `dados_acoes.csv` com os dados completos e variações.

---

## Autor

Lucas Oliveira  
[github.com/LucasOliveiraDados](https://github.com/LucasOliveiraDados)
