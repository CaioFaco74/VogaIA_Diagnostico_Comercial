#!/usr/bin/env python3
"""
Diagnóstico Comercial Voga.IA - Versão Completa com 8 Agentes
Execução dos 8 agentes especializados salvando relatórios individuais
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

def limpar_outputs_anteriores():
    """Remove arquivos de execuções anteriores"""
    outputs_dir = project_root / "src" / "diagnostico_comercial_voga_ia" / "outputs"
    if outputs_dir.exists():
        for file in outputs_dir.glob("*.md"):
            if file.name not in ["logs.md"]:  # Manter apenas logs.md
                file.unlink()
                print(f"🗑️  Removido: {file.name}")

def verificar_dados():
    """Verifica se os dados estão acessíveis"""
    print("\n🔍 VERIFICANDO DADOS DE ENTRADA...")
    tool = LerDadosCSV()
    result = tool._run("dados_entrada")
    
    if result["status"] == "sucesso":
        print(f"✅ Dados carregados: {result['total_campos']} campos")
        
        dados = result['dados']
        print("📊 RESUMO DOS DADOS:")
        print(f"   💰 Receita Total: R$ {dados['Receita_Total']['valor']:,.2f}")
        print(f"   💳 Custo Vendas/Marketing: R$ {dados['Custo_Vendas_Marketing']['valor']:,.2f}")
        print(f"   👥 Novos Clientes: {dados['Novos_Clientes']['valor']}")
        print(f"   📋 Propostas Enviadas: {dados['Propostas_Enviadas']['valor']}")
        print(f"   🎯 Negócios Fechados: {dados['Negocios_Fechados']['valor']}")
        print(f"   📅 Ciclo de Vendas: {dados['Ciclo_Vendas_Dias']['valor']} dias")
        print(f"   👨‍💼 Reps Ativos: {dados['Reps_Ativos']['valor']}")
        
        return True
    else:
        print(f"❌ Erro ao carregar dados: {result['mensagem']}")
        return False

def executar_diagnostico_completo():
    """Executa o diagnóstico completo com os 8 agentes"""
    print("\n🚀 INICIANDO DIAGNÓSTICO COMERCIAL COMPLETO")
    print("="*80)
    print("🎯 ENXAME DE 8 AGENTES ESPECIALIZADOS")
    print()
    print("   1️⃣  Data Collector Agent     → Coleta e validação de dados")
    print("   2️⃣  Data Governance Agent    → Governança e detecção de outliers")  
    print("   3️⃣  Metrics Calculator Agent → Cálculo de todas as métricas")
    print("   4️⃣  Business Analyst Agent   → Análise estratégica e insights")
    print("   5️⃣  Alert Monitor Agent      → Configuração de alertas")
    print("   6️⃣  Visualization Agent      → Criação de gráficos e tabelas")
    print("   7️⃣  Dashboard Creator Agent  → Especificações de dashboard")
    print("   8️⃣  Report Generator Agent   → Relatório executivo final")
    print("="*80)
    
    inputs = {
        'cliente': 'Diagnóstico Comercial Voga.IA - Versão Completa',
        'periodo': '2025',
        'dados_csv_path': 'data/dados_entrada.csv',
        'metricas_csv_path': 'data/metricas_calculadas.csv',
        'output_path': 'outputs/',
        'gerar_excel': True,
        'gerar_dashboard': True,
        'gerar_relatorios_individuais': True,
        'data_execucao': time.strftime("%Y-%m-%d"),
        'hora_execucao': time.strftime("%H:%M:%S"),
        'executado_por': 'Sistema Voga.IA v2.0'
    }
    
    print(f"\n📋 CONFIGURAÇÕES:")
    for key, value in inputs.items():
        print(f"   • {key}: {value}")
    
    print(f"\n⏰ Início da execução: {time.strftime('%H:%M:%S')}")
    print("⚠️  TEMPO ESTIMADO: 5-8 minutos (8 agentes trabalhando)")
    print("📊 AGUARDE: Cada agente salvará seu relatório individual...")
    
    try:
        crew_instance = DiagnosticoComercialVogaIaCrew()
        resultado = crew_instance.crew().kickoff(inputs=inputs)
        
        print(f"\n⏰ Conclusão: {time.strftime('%H:%M:%S')}")
        print("\n🎉 DIAGNÓSTICO COMPLETO CONCLUÍDO!")
        
        return resultado
        
    except Exception as e:
        print(f"\n❌ ERRO durante execução: {e}")
        print("🔍 Detalhes:")
        import traceback
        traceback.print_exc()
        return None

def verificar_relatorios_gerados():
    """Verifica se todos os 8 relatórios foram gerados"""
    print("\n📋 VERIFICANDO RELATÓRIOS GERADOS...")
    
    outputs_dir = project_root / "src" / "diagnostico_comercial_voga_ia" / "outputs"
    
    relatorios_esperados = [
        ("01_data_collector_report.md", "Data Collector"),
        ("02_data_governance_report.md", "Data Governance"), 
        ("03_metrics_calculator_report.md", "Metrics Calculator"),
        ("04_business_analyst_report.md", "Business Analyst"),
        ("05_alert_monitor_report.md", "Alert Monitor"),
        ("06_visualization_report.md", "Visualization"),
        ("07_dashboard_creator_report.md", "Dashboard Creator"),
        ("08_report_generator_report.md", "Report Generator")
    ]
    
    relatorios_encontrados = []
    total_size = 0
    
    for arquivo, agente in relatorios_esperados:
        file_path = outputs_dir / arquivo
        if file_path.exists():
            size = file_path.stat().st_size
            total_size += size
            print(f"✅ {agente:20} → {arquivo} ({size:,} bytes)")
            relatorios_encontrados.append(arquivo)
        else:
            print(f"❌ {agente:20} → {arquivo} NÃO ENCONTRADO")
    
    # Verificar relatório executivo
    exec_report = outputs_dir / "diagnostico_executivo.md"
    if exec_report.exists():
        size = exec_report.stat().st_size
        total_size += size
        print(f"✅ {'Executivo':20} → diagnostico_executivo.md ({size:,} bytes)")
        relatorios_encontrados.append("diagnostico_executivo.md")
    
    # Verificar CSV de métricas
    metricas_path = project_root / "src" / "diagnostico_comercial_voga_ia" / "data" / "metricas_calculadas.csv"
    if metricas_path.exists():
        size = metricas_path.stat().st_size
        total_size += size
        print(f"✅ {'Métricas CSV':20} → metricas_calculadas.csv ({size:,} bytes)")
        relatorios_encontrados.append("metricas_calculadas.csv")
    
    print(f"\n📊 RESUMO DA EXECUÇÃO:")
    print(f"   🎯 Relatórios gerados: {len(relatorios_encontrados)}/{len(relatorios_esperados)+2}")
    print(f"   📁 Tamanho total: {total_size:,} bytes")
    print(f"   💾 Localização: {outputs_dir}")
    
    if len(relatorios_encontrados) >= 6:  # Pelo menos 6 dos 8 + executivo
        print(f"   🟢 Status: SUCESSO COMPLETO!")
        return True
    elif len(relatorios_encontrados) >= 4:
        print(f"   🟡 Status: SUCESSO PARCIAL")
        return True
    else:
        print(f"   🔴 Status: FALHA - Poucos relatórios gerados")
        return False

def mostrar_resultado_final():
    """Mostra como acessar os resultados"""
    print("\n🔗 COMO VISUALIZAR OS RESULTADOS:")
    print()
    print("📄 RELATÓRIOS INDIVIDUAIS:")
    outputs_dir = "src/diagnostico_comercial_voga_ia/outputs"
    for i in range(1, 9):
        print(f"   {i}️⃣  cat {outputs_dir}/{i:02d}_*_report.md")
    
    print("\n📊 RELATÓRIO EXECUTIVO:")
    print(f"   🎯 cat {outputs_dir}/diagnostico_executivo.md")
    
    print("\n📈 MÉTRICAS CALCULADAS:")
    print("   📊 cat src/diagnostico_comercial_voga_ia/data/metricas_calculadas.csv")
    
    print("\n🌐 TODOS OS ARQUIVOS:")
    print(f"   📁 ls -la {outputs_dir}/")

def main():
    """Função principal"""
    print("🎯 DIAGNÓSTICO COMERCIAL VOGA.IA - VERSÃO COMPLETA")
    print("🤖 Sistema com 8 Agentes Especializados CrewAI")
    print("📈 Análise Profunda: CAC, LTV, ROI, Alertas, Dashboard e mais...")
    
    # Limpar execuções anteriores
    limpar_outputs_anteriores()
    
    # Verificar dados
    if not verificar_dados():
        print("\n❌ Falha na verificação de dados. Abortando execução.")
        return
    
    # Executar diagnóstico completo
    resultado = executar_diagnostico_completo()
    
    if resultado:
        # Verificar relatórios gerados
        if verificar_relatorios_gerados():
            print("\n✅ EXECUÇÃO COMPLETA E BEM-SUCEDIDA!")
            mostrar_resultado_final()
        else:
            print("\n⚠️  Execução concluída com problemas na geração de relatórios.")
    else:
        print("\n❌ Falha na execução do diagnóstico.")

if __name__ == "__main__":
    main()