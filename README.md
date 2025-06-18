# ACOES_BRASILEIRAS

Este projeto realiza a extração, transformação, análise e armazenamento de dados de ações da B3, com foco nas mais líquidas e nas variações recentes de desempenho. Todo o pipeline foi desenvolvido em Python, orquestrado com **Apache Airflow**, containerizado com **Docker** e os dados finais analisados no **Power BI**.

---

## 📁 Estrutura do Projeto

```
ACOES_BRASILEIRAS/
├── codigos/
│   ├── extrair_tickers.py         # Seleciona ações com liquidez ≥ R$ 5 milhões (API brapi.dev)
│   ├── acoes_dados.py             # Coleta histórico de preços via yfinance
│   ├── valorizacao_acoes.py       # Calcula valorização diária e acumulada
│   ├── salvar_dados_acoes.py      # Armazena no PostgreSQL e exporta em CSV
│   └── conexao_banco.py           # Gerencia conexão com o banco (via .env)
├── main.py                        # Pipeline completo: extração + transformação + carga
├── tickers_validos.txt            # Lista dos tickers filtrados
├── .env                           # Variáveis de ambiente (não versionado)
├── requirements.txt               # Bibliotecas do projeto
├── airflow/                       # Estrutura do Airflow (Docker + dags)
```

---

## 🔄 ETL – Pipeline de Dados

A lógica de dados foi estruturada em três etapas principais:

### 🟢 Extração

Coleta automática de dados de ações com base em critérios mínimos de liquidez.

- `extrair_tickers.py`: Consulta a API pública brapi.dev e filtra ativos com volume médio diário ≥ R$ 5 milhões.
- `acoes_dados.py`: Consulta o histórico de preços e volumes diários via yfinance.

### 🟡 Transformação

Cálculo de métricas financeiras úteis à tomada de decisão.

- `valorizacao_acoes.py`: Calcula a valorização diária e valorização acumulada ao longo do período analisado, mantendo os valores com 2 casas decimais.

### 🟠 Carga

Persistência dos dados transformados:

- Armazenamento em banco PostgreSQL (tabela `dados_acoes`)
- Exportação em CSV local (`dados_acoes.csv`)

---

## ⚙️ Orquestração com Airflow

A automação das etapas foi feita com o Apache Airflow, permitindo agendamentos periódicos do pipeline.

- Estrutura completa com `docker-compose` e pastas `dags/`, `plugins/`, `logs/`
- DAG personalizada para executar o pipeline completo em ordem (extração → transformação → carga)
- Ambiente isolado com Docker, pronto para escalabilidade futura

---

## 🐳 Docker

Todo o ecossistema de execução foi encapsulado em containers Docker:

- Banco de dados PostgreSQL
- Webserver e Scheduler do Airflow
- Execução do pipeline via `main.py` e/ou agendamento

---

## 📊 Análise Visual com Power BI

A análise dos dados transformados foi feita com Power BI Desktop, utilizando o arquivo `dados_acoes.csv` como fonte principal.

Principais KPIs e visualizações:

- **Média da valorização acumulada** (comparada à meta da Selic)
- **Proporção de ações com desempenho positivo** (meta: ≥50%)
- **Média de volume diário negociado**
- **Gráfico comparativo entre ações selecionadas**
- **Ranking de ações com maior valorização acumulada**
- **Evolução de volume e preço por mês**

---

## 🔗 Links

- Código-fonte completo: [GitHub – LucasOliveiraDados](https://github.com/LucasOliveiraDados)
- Dashboard interativo no Power BI Service: _(inserir link ao publicar)_

---

## ✍️ Autor

**Lucas Oliveira**  
[GitHub](https://github.com/LucasOliveiraDados) · [LinkedIn](https://www.linkedin.com/)
