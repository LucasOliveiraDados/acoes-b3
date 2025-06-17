from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
sys.path.append("/opt/airflow/codigos")

from extrair_tickers import extrair_tickers
from salvar_dados_acoes import salvar_dados_acoes

default_args = {
    "owner": "lucas",
    "start_date": datetime(2025, 6, 1),
}

with DAG(
    dag_id="pipeline_acoes_brasileiras",
    default_args=default_args,
    schedule_interval="@daily",  # ou "0 9 * * 1-5" para dias úteis às 9h
    catchup=False,
    tags=["b3", "acoes"],
) as dag:

    tarefa_extrair = PythonOperator(
        task_id="extrair_tickers",
        python_callable=extrair_tickers,
    )

    tarefa_pipeline = PythonOperator(
        task_id="executar_pipeline",
        python_callable=salvar_dados_acoes,
    )

    tarefa_extrair >> tarefa_pipeline
