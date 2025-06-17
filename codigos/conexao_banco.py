import psycopg2  
from psycopg2 import OperationalError  
import os  
from dotenv import load_dotenv  

def conexao_bd():  
    
    load_dotenv()  # Carrega variáveis do arquivo .env  

    try:  
        conexao = psycopg2.connect(  
            host=os.getenv("DB_HOST"),  
            database=os.getenv("DB_NAME"),  
            user=os.getenv("DB_USER"),  
            password=os.getenv("DB_PASSWORD"),  
            port=os.getenv("DB_PORT", "5432")  
        )  
        print("[SUCESSO] Conexão com PostgreSQL estabelecida.")  
        conexao.close()  
        return True  

    except OperationalError as erro:  
        print(f"[ERRO] Falha na conexão: {erro}")  
        return False  

if __name__ == "__main__":  
    conexao_bd()  