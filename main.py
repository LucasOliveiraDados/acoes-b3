import subprocess

def executar_comando(comando):
    print(f"\n[EXECUTANDO] {comando}")
    resultado = subprocess.run(comando, shell=True, text=True)
    if resultado.returncode == 0:
        print(f"[OK] Comando finalizado com sucesso.")
    else:
        print(f"[ERRO] Comando '{comando}' falhou.")

if __name__ == "__main__":
    # Etapa 1 – Extrair tickers válidos
    executar_comando("python codigos/extrair_tickers.py")
    
    # Etapa 2 – Executar pipeline completo (extrai dados, calcula valorização e salva no banco/CSV)
    executar_comando("python codigos/salvar_dados_acoes.py")
