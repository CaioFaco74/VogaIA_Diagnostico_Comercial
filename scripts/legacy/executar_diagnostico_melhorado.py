#!/usr/bin/env python3
"""
Diagnóstico Comercial Voga.IA - Versão Melhorada
Execução controlada do enxame de 8 agentes com verificações
"""

import sys
import os
from pathlib import Path
from dotenv import load_dotenv
import time

# Carregar variáveis de ambiente
load_dotenv()

# Adicionar path do projeto
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / "src"))

try:
    from diagnostico_comercial_voga_ia.crew import DiagnosticoComercialVogaIaCrew
    from diagnostico_comercial_voga_ia.tools.diagnostico_tools import LerDadosCSV
    print("✅ Módulos importados com sucesso!")
except ImportError as e:
    print(f"❌ Erro ao importar módulos: {e}")
    sys.exit(1)

def verificar_dados():
    """Verifica se os dados estão acessíveis"""
    print("\n🔍 VERIFICANDO DADOS...")
    tool = LerDadosCSV()
    result = tool._run("dados_entrada")
    
    if result["status"] == "sucesso":
        print(f"✅ Dados carregados: {result['total_campos']} campos")
        print(f"📊 Receita Total: R$ {result['dados']['Receita_Total']['valor']:,.2f}")
        print(f"💰 Custo Vendas: R$ {result['dados']['Custo_Vendas_Marketing']['valor']:,.2f}")
        print(f"👥 Novos Clientes: {result['dados']['Novos_Clientes']['valor']}")
        return True
    else:
        print(f"❌ Erro ao carregar dados: {result['mensagem']}")
        return False

def executar_diagnostico():
    """Executa o diagnóstico com 8 agentes"""
    print("\n🚀 INICIANDO DIAGNÓSTICO COMERCIAL COMPLETO")
    print("="*70)
    print("🤖 8 Agentes Especializados em Ação:")
    print("   1️⃣ Data Collector - Coleta e validação")
    print("   2️⃣ Data Governance - Governança e limpeza")  
    print("   3️⃣ Metrics Calculator - Cálculo de métricas")
    print("   4️⃣ Business Analyst - Análise estratégica")
    print("   5️⃣ Alert Monitor - Configuração de alertas")
    print("   6️⃣ Visualization - Criação de gráficos")
    print("   7️⃣ Dashboard Creator - Protótipo dashboard")
    print("   8️⃣ Report Generator - Relatório executivo")
    print("="*70)
    
    inputs = {
        'cliente': 'Empresa Diagnóstico Voga.IA',
        'periodo': '2025',
        'dados_csv_path': 'data/dados_entrada.csv',
        'metricas_csv_path': 'data/metricas_calculadas.csv',
        'output_path': 'outputs/',
        'gerar_excel': True,
        'gerar_dashboard': True,
        'data_atual': time.strftime("%Y-%m-%d"),
        'executado_por': 'Sistema Voga.IA'
    }
    
    print(f"\n📋 Configurações do diagnóstico:")
    for key, value in inputs.items():
        print(f"   • {key}: {value}")
    
    print(f"\n⏰ Início da execução: {time.strftime('%H:%M:%S')}")
    print("⚠️  AGUARDE: O processamento pode levar 3-5 minutos...")
    
    try:
        crew_instance = DiagnosticoComercialVogaIaCrew()
        resultado = crew_instance.crew().kickoff(inputs=inputs)
        
        print(f"\n⏰ Conclusão: {time.strftime('%H:%M:%S')}")
        print("\n🎉 DIAGNÓSTICO CONCLUÍDO COM SUCESSO!")
        print("📁 Verifique os resultados em:")
        print("   • src/diagnostico_comercial_voga_ia/outputs/")
        print("   • src/diagnostico_comercial_voga_ia/data/metricas_calculadas.csv")
        
        return resultado
        
    except Exception as e:
        print(f"\n❌ ERRO durante execução: {e}")
        print("🔍 Detalhes:")
        import traceback
        traceback.print_exc()
        return None

def verificar_resultados():
    """Verifica se os arquivos foram gerados"""
    print("\n📋 VERIFICANDO RESULTADOS GERADOS...")
    
    outputs_dir = project_root / "src" / "diagnostico_comercial_voga_ia" / "outputs"
    
    arquivos_esperados = [
        "diagnostico_executivo.md",
        "logs.md"
    ]
    
    arquivos_encontrados = []
    for arquivo in arquivos_esperados:
        file_path = outputs_dir / arquivo
        if file_path.exists():
            size = file_path.stat().st_size
            print(f"✅ {arquivo} ({size} bytes)")
            arquivos_encontrados.append(arquivo)
        else:
            print(f"❌ {arquivo} não encontrado")
    
    # Verificar CSV de métricas
    metricas_path = project_root / "src" / "diagnostico_comercial_voga_ia" / "data" / "metricas_calculadas.csv"
    if metricas_path.exists():
        print(f"✅ metricas_calculadas.csv ({metricas_path.stat().st_size} bytes)")
        arquivos_encontrados.append("metricas_calculadas.csv")
    else:
        print("❌ metricas_calculadas.csv não encontrado")
    
    print(f"\n📊 Resumo: {len(arquivos_encontrados)}/{len(arquivos_esperados)+1} arquivos gerados")
    
    return len(arquivos_encontrados) > 0

def main():
    """Função principal"""
    print("🎯 DIAGNÓSTICO COMERCIAL VOGA.IA - VERSÃO MELHORADA")
    print("🤖 Sistema Inteligente de Análise Comercial com 8 Agentes")
    print("📈 Análise Completa: CAC, LTV, ROI, Win Rate e mais...")
    
    # Verificar dados
    if not verificar_dados():
        print("\n❌ Falha na verificação de dados. Abortando execução.")
        return
    
    # Executar diagnóstico
    resultado = executar_diagnostico()
    
    if resultado:
        # Verificar resultados
        if verificar_resultados():
            print("\n✅ EXECUÇÃO COMPLETA E BEM-SUCEDIDA!")
            print("🔗 Para ver os resultados:")
            print("   📄 cat src/diagnostico_comercial_voga_ia/outputs/diagnostico_executivo.md")
            print("   📊 cat src/diagnostico_comercial_voga_ia/data/metricas_calculadas.csv")
        else:
            print("\n⚠️  Execução concluída, mas alguns arquivos podem não ter sido gerados.")
    else:
        print("\n❌ Falha na execução do diagnóstico.")

if __name__ == "__main__":
    main()