#!/usr/bin/env python3
"""
Script de inicialização da aplicação web
Verifica se já está rodando antes de iniciar nova instância
"""

import os
import sys
import subprocess
import time
import signal
from pathlib import Path

def check_port_in_use(port):
    """Verifica se a porta está em uso"""
    try:
        import socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('localhost', port))
            return False
    except OSError:
        return True

def kill_process_on_port(port):
    """Mata processo rodando na porta especificada"""
    try:
        result = subprocess.run(['lsof', '-ti', f':{port}'], 
                              capture_output=True, text=True)
        if result.stdout.strip():
            pids = result.stdout.strip().split('\n')
            for pid in pids:
                if pid:
                    print(f"Matando processo {pid} na porta {port}")
                    os.kill(int(pid), signal.SIGTERM)
                    time.sleep(1)
    except Exception as e:
        print(f"Erro ao matar processo: {e}")

def main():
    """Função principal"""
    port = 8080
    
    print("🚀 Iniciando aplicação web do Diagnóstico Comercial Voga.IA")
    print(f"📡 Porta: {port}")
    
    # Verificar se a porta está em uso
    if check_port_in_use(port):
        print(f"⚠️  Porta {port} já está em uso!")
        response = input("Deseja matar o processo existente? (s/n): ")
        if response.lower() in ['s', 'sim', 'y', 'yes']:
            kill_process_on_port(port)
            time.sleep(2)
        else:
            print("❌ Cancelando inicialização")
            return
    
    # Verificar se o ambiente virtual está ativo
    if not os.environ.get('VIRTUAL_ENV'):
        print("⚠️  Ambiente virtual não detectado!")
        print("Ativando ambiente virtual...")
        
        venv_path = Path("venv-python312/bin/activate")
        if venv_path.exists():
            # Ativar ambiente virtual
            activate_script = f"source {venv_path} && "
        else:
            print("❌ Ambiente virtual não encontrado!")
            return
    else:
        activate_script = ""
    
    # Comando para executar a aplicação
    cmd = f"{activate_script}python web_app.py"
    
    print("✅ Iniciando aplicação...")
    print(f"🌐 Acesse: http://localhost:{port}")
    print("🛑 Para parar: Ctrl+C")
    print("-" * 50)
    
    try:
        # Executar a aplicação
        subprocess.run(cmd, shell=True, check=True)
    except KeyboardInterrupt:
        print("\n🛑 Aplicação interrompida pelo usuário")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar aplicação: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main() 