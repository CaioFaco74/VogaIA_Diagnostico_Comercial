#!/usr/bin/env python3
"""
Script de Inicialização da Plataforma Voga.IA
Executa o diagnóstico e inicia a aplicação web
"""

import os
import sys
import subprocess
import time
import webbrowser
from datetime import datetime

def print_banner():
    """Imprime o banner da aplicação"""
    print("=" * 60)
    print("🚀 Voga.IA - Diagnóstico Comercial Inteligente")
    print("=" * 60)
    print(f"📅 Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 60)

def check_environment():
    """Verifica se o ambiente está configurado"""
    print("🔍 Verificando ambiente...")
    
    # Verificar se o ambiente virtual está ativo
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("❌ Ambiente virtual não detectado!")
        print("💡 Execute: source venv-python312/bin/activate")
        return False
    
    # Verificar dependências
    try:
        import flask
        import plotly
        import crewai
        print("✅ Dependências verificadas")
        return True
    except ImportError as e:
        print(f"❌ Dependência faltando: {e}")
        return False

def run_diagnosis():
    """Executa o diagnóstico completo"""
    print("\n🔬 Executando diagnóstico comercial...")
    
    try:
        # Adicionar src ao path
        sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
        
        # Importar e executar o diagnóstico
        from diagnostico_comercial_voga_ia.main import main
        main()
        
        print("✅ Diagnóstico executado com sucesso!")
        return True
    except Exception as e:
        print(f"❌ Erro ao executar diagnóstico: {e}")
        return False

def start_web_app():
    """Inicia a aplicação web"""
    print("\n🌐 Iniciando aplicação web...")
    
    try:
        # Verificar se a porta 8080 está livre
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 8080))
        sock.close()
        
        if result == 0:
            print("⚠️ Porta 8080 já está em uso")
            print("💡 A aplicação pode já estar rodando")
        else:
            print("✅ Porta 8080 disponível")
        
        # Iniciar aplicação web
        print("🚀 Iniciando servidor web...")
        print("📱 Acesse: http://localhost:8080")
        print("👤 Login: admin@vogaia.com / admin123")
        print("👤 Login: user@vogaia.com / user123")
        
        # Abrir navegador automaticamente
        time.sleep(2)
        webbrowser.open('http://localhost:8080')
        
        # Executar aplicação web
        subprocess.run([sys.executable, 'web_app.py'])
        
    except Exception as e:
        print(f"❌ Erro ao iniciar aplicação web: {e}")
        return False

def main():
    """Função principal"""
    print_banner()
    
    # Verificar ambiente
    if not check_environment():
        print("\n❌ Ambiente não configurado corretamente")
        return
    
    # Perguntar se quer executar diagnóstico
    print("\n🤔 Deseja executar o diagnóstico antes de iniciar a plataforma?")
    print("1. Sim - Executar diagnóstico + Plataforma web")
    print("2. Não - Apenas iniciar plataforma web")
    print("3. Sair")
    
    choice = input("\nEscolha uma opção (1-3): ").strip()
    
    if choice == "1":
        # Executar diagnóstico
        if run_diagnosis():
            print("\n✅ Diagnóstico concluído! Iniciando plataforma web...")
            start_web_app()
        else:
            print("\n❌ Falha no diagnóstico. Tentando iniciar plataforma web...")
            start_web_app()
    
    elif choice == "2":
        # Apenas iniciar plataforma web
        start_web_app()
    
    elif choice == "3":
        print("\n👋 Até logo!")
        return
    
    else:
        print("\n❌ Opção inválida!")

if __name__ == "__main__":
    main() 