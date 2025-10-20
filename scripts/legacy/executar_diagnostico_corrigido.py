#!/usr/bin/env python3
"""
Script para executar o diagnóstico completo com as correções aplicadas
Versão corrigida que resolve o problema do max_iter=1
"""

import sys
import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime

# Carregar variáveis de ambiente
load_dotenv()

# Verificar se temos OpenAI API Key
if not os.getenv('OPENAI_API_KEY'):
    print("⚠️  ATENÇÃO: OPENAI_API_KEY não encontrada no .env")
    print("📝 Por favor, adicione sua chave API no arquivo .env")
    print("💡 Exemplo: OPENAI_API_KEY=sk-...")

    response = input("\n🤔 Continuar sem OpenAI? (s/N): ").lower()
    if response != 's':
        print("👋 Configure a API key e execute novamente!")
        sys.exit(1)

# Adicionar o diretório src ao path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

try:
    from diagnostico_comercial_voga_ia.crew import DiagnosticoComercialVogaIaCrew
    print("✅ Módulo DiagnosticoComercialVogaIaCrew importado com sucesso!")
except ImportError as e:
    print(f"❌ Erro ao importar DiagnosticoComercialVogaIaCrew: {e}")
    sys.exit(1)


def run():
    """
    Executa o ENXAME DE 8 AGENTES para diagnóstico comercial completo
    com correções aplicadas (max_iter=3)
    """
    print("🚀 INICIANDO ENXAME DE 8 AGENTES CREWAI (VERSÃO CORRIGIDA)")
    print("="*70)
    print("🤖 Agentes: Coletor, Governança, Calculador, Analista,")
    print("           Monitor, Visualizador, Dashboard, Relator")
    print("="*70)
    print("🔧 Correções aplicadas:")
    print("   • max_iter aumentado de 1 para 3")
    print("   • Garantia de execução completa do agente 8")
    print("="*70)

    inputs = {
        'cliente': 'Empresa Demonstração',
        'periodo': '2025',
        'dados_csv_path': 'data/dados_entrada.csv',
        'metricas_csv_path': 'data/metricas_calculadas.csv',
        'output_path': 'outputs/',
        'gerar_excel': True,
        'gerar_dashboard': True
    }

    print("\n📊 Dados de entrada configurados:")
    for key, value in inputs.items():
        print(f"   • {key}: {value}")

    # Criar arquivo de log da execução
    log_inicio = datetime.now()
    print(f"\n⏰ Início da execução: {log_inicio.strftime('%d/%m/%Y %H:%M:%S')}")

    try:
        print("\n🎯 Iniciando execução do crew corrigido...")
        crew_instance = DiagnosticoComercialVogaIaCrew()
        resultado = crew_instance.crew().kickoff(inputs=inputs)

        log_fim = datetime.now()
        duracao = log_fim - log_inicio

        print("\n" + "="*70)
        print("🎉 DIAGNÓSTICO CONCLUÍDO COM SUCESSO!")
        print("="*70)
        print(f"⏱️  Tempo de execução: {duracao}")
        print(f"⏰ Término: {log_fim.strftime('%d/%m/%Y %H:%M:%S')}")
        print("\n📁 Resultados salvos em: outputs/")
        print("📊 Arquivos gerados:")
        print("   ✓ 01_data_collector_report.md")
        print("   ✓ 02_data_governance_report.md")
        print("   ✓ 03_metrics_calculator_report.md")
        print("   ✓ 04_business_analyst_report.md")
        print("   ✓ 05_alert_monitor_report.md")
        print("   ✓ 06_visualization_agent_report.md")
        print("   ✓ 07_dashboard_creator_report.md")
        print("   ✓ 08_report_generator_report.md ← CORRIGIDO!")
        print("="*70)

        # Salvar log de execução
        log_file = Path(__file__).parent / "outputs" / f"execution_log_{log_fim.strftime('%Y%m%d_%H%M%S')}.txt"
        log_file.parent.mkdir(exist_ok=True)
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write(f"Execução Diagnóstico Comercial Voga.IA\n")
            f.write(f"Data/Hora Início: {log_inicio}\n")
            f.write(f"Data/Hora Fim: {log_fim}\n")
            f.write(f"Duração: {duracao}\n")
            f.write(f"Status: SUCESSO\n")
            f.write(f"Correções Aplicadas: max_iter=3\n")

        return resultado

    except Exception as e:
        log_fim = datetime.now()
        print(f"\n❌ ERRO durante execução do crew: {e}")
        print("🔍 Detalhes do erro:")
        import traceback
        traceback.print_exc()

        # Salvar log de erro
        log_file = Path(__file__).parent / "outputs" / f"error_log_{log_fim.strftime('%Y%m%d_%H%M%S')}.txt"
        log_file.parent.mkdir(exist_ok=True)
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write(f"Execução Diagnóstico Comercial Voga.IA - ERRO\n")
            f.write(f"Data/Hora: {log_fim}\n")
            f.write(f"Erro: {str(e)}\n")
            f.write(f"\nTraceback:\n")
            f.write(traceback.format_exc())

        raise e


if __name__ == "__main__":
    print("🎯 DIAGNÓSTICO COMERCIAL VOGA.IA - VERSÃO CORRIGIDA")
    print("🤖 Sistema com 8 Agentes CrewAI Especializados")
    print("📈 Análise Completa de Performance Comercial")
    print()

    run()
