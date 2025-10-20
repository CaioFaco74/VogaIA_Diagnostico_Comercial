#!/usr/bin/env python3
"""
Script para re-executar apenas o Agente 8 (Report Generator)
que não foi executado em 03/10/2025
"""

import sys
import os
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Adicionar o diretório src ao path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from diagnostico_comercial_voga_ia.crew import DiagnosticoComercialVogaIaCrew

def reexecutar_agente_8():
    """
    Re-executa apenas o agente 8 (Report Generator) usando os dados já calculados
    """
    print("🔄 RE-EXECUTANDO AGENTE 8 (REPORT GENERATOR)")
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

    try:
        print("\n📊 Carregando métricas já calculadas...")
        print("🎯 Executando agente 8 (Report Generator)...")

        crew_instance = DiagnosticoComercialVogaIaCrew()

        # Executar apenas a task do agente 8
        report_task = crew_instance.generate_executive_report_task()

        # Criar um crew simplificado apenas com o agente 8
        from crewai import Crew, Process

        simple_crew = Crew(
            agents=[crew_instance.report_generator_agent()],
            tasks=[report_task],
            process=Process.sequential,
            verbose=True
        )

        resultado = simple_crew.kickoff(inputs=inputs)

        print("\n✅ AGENTE 8 EXECUTADO COM SUCESSO!")
        print("📁 Verifique: outputs/08_report_generator_report.md")

        return resultado

    except Exception as e:
        print(f"\n❌ ERRO durante execução: {e}")
        import traceback
        traceback.print_exc()
        raise e

if __name__ == "__main__":
    print("🎯 RE-EXECUÇÃO DO AGENTE 8 - REPORT GENERATOR")
    print("📈 Usando métricas já calculadas em 03/10/2025")
    print()

    reexecutar_agente_8()
