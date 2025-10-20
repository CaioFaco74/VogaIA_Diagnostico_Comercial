#!/usr/bin/env python3
"""
Diagnóstico Comercial Voga.IA
Sistema de Diagnóstico Comercial Automatizado com CrewAI - 8 AGENTES
"""

import sys
import os
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Verificar se temos OpenAI API Key
if not os.getenv('OPENAI_API_KEY'):
    print("⚠️  ATENÇÃO: OPENAI_API_KEY não encontrada no .env")
    print("📝 Por favor, adicione sua chave API no arquivo .env")
    print("💡 Exemplo: OPENAI_API_KEY=sk-...")
    
    # Perguntar se quer continuar sem API key (usando modelo local)
    response = input("\n🤔 Continuar sem OpenAI? (s/N): ").lower()
    if response != 's':
        print("👋 Configure a API key e execute novamente!")
        sys.exit(1)

try:
    # Import absoluto
    from diagnostico_comercial_voga_ia.crew import DiagnosticoComercialVogaIaCrew
    print("✅ Módulo DiagnosticoComercialVogaIaCrew importado com sucesso!")
except ImportError as e:
    print(f"❌ Erro ao importar DiagnosticoComercialVogaIaCrew: {e}")
    sys.exit(1)


def run():
    """
    Executa o ENXAME DE 8 AGENTES para diagnóstico comercial completo.
    """
    print("🚀 INICIANDO ENXAME DE 8 AGENTES CREWAI")
    print("="*60)
    print("🤖 Agentes: Coletor, Governança, Calculador, Analista,")
    print("           Monitor, Visualizador, Dashboard, Relator")
    print("="*60)
    
    inputs = {
        'cliente': 'Empresa Demonstração',
        'periodo': '2025',
        'dados_csv_path': 'data/dados_entrada.csv',
        'metricas_csv_path': 'data/metricas_calculadas.csv',
        'output_path': 'outputs/',
        'gerar_excel': True,
        'gerar_dashboard': True
    }
    
    print("📊 Dados de entrada configurados:")
    for key, value in inputs.items():
        print(f"   • {key}: {value}")
    
    try:
        print("\n🎯 Iniciando execução do crew...")
        crew_instance = DiagnosticoComercialVogaIaCrew()
        resultado = crew_instance.crew().kickoff(inputs=inputs)
        
        print("\n🎉 DIAGNÓSTICO CONCLUÍDO COM SUCESSO!")
        print("📁 Resultados salvos em: outputs/")
        print("📊 Verifique os arquivos gerados pelos agentes")
        
        return resultado
        
    except Exception as e:
        print(f"\n❌ ERRO durante execução do crew: {e}")
        print("🔍 Detalhes do erro:")
        import traceback
        traceback.print_exc()
        raise e


if __name__ == "__main__":
    print("🎯 DIAGNÓSTICO COMERCIAL VOGA.IA")
    print("🤖 Sistema com 8 Agentes CrewAI Especializados")
    print("📈 Análise Completa de Performance Comercial")
    print()
    
    run()
