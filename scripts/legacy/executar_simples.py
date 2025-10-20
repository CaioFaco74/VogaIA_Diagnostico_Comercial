#!/usr/bin/env python3
"""
🎯 EXECUTAR DIAGNÓSTICO - VERSÃO SIMPLIFICADA
Script direto para executar o diagnóstico sem complicações
"""

import sys
import os
from pathlib import Path

# Configurar paths ANTES de qualquer import
project_root = Path(__file__).parent
src_path = project_root / "src"

# Adicionar ao Python path
sys.path.insert(0, str(src_path))
sys.path.insert(0, str(project_root))

print("🎯 DIAGNÓSTICO COMERCIAL VOGA.IA")
print("🚀 Iniciando execução direta...")

# Carregar variáveis de ambiente
from dotenv import load_dotenv
load_dotenv()

# Verificar se temos OpenAI API Key
if not os.getenv('OPENAI_API_KEY'):
    print("⚠️  Executando sem OpenAI API Key")

try:
    print("📦 Importando módulos...")
    
    # Import direto do crew
    from diagnostico_comercial_voga_ia.crew import DiagnosticoComercialVogaIaCrew
    
    print("✅ Módulos importados com sucesso!")
    
    # Configurar inputs
    inputs = {
        'cliente': 'Empresa Teste Voga.IA',
        'periodo': '2025',
        'dados_csv_path': 'data/dados_entrada.csv',
        'metricas_csv_path': 'data/metricas_calculadas.csv',
        'output_path': 'outputs/',
        'gerar_excel': True,
        'gerar_dashboard': True
    }
    
    print("\n🤖 Iniciando enxame de 8 agentes...")
    
    # Criar e executar crew
    crew_instance = DiagnosticoComercialVogaIaCrew()
    resultado = crew_instance.crew().kickoff(inputs=inputs)
    
    print("\n🎉 DIAGNÓSTICO CONCLUÍDO!")
    print("📁 Verifique: src/diagnostico_comercial_voga_ia/outputs/")
    
except Exception as e:
    print(f"❌ ERRO: {e}")
    
    # Diagnóstico detalhado
    print("\n🔍 DIAGNÓSTICO DO ERRO:")
    print(f"Python path atual: {sys.path[:3]}")
    print(f"Diretório atual: {os.getcwd()}")
    print(f"Arquivo src existe? {src_path.exists()}")
    
    # Tentar listar o que está no src
    if src_path.exists():
        print(f"Conteúdo do src: {list(src_path.iterdir())}")
    
    import traceback
    traceback.print_exc()
