#!/usr/bin/env python3
"""
Diagnóstico Comercial Voga.IA - Versão Simples para Teste
"""

import sys
import os
from pathlib import Path

# Adicionar o caminho do projeto ao Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

try:
    from tools.diagnostico_tools import (
        CalcularCAC,
        CalcularLTV,
        CalcularROISimples,
        CalcularWinRate,
        LerDadosCSV,
        SalvarMetricasCSV,
        ExportarRelatorioMD
    )
    print("✅ Ferramentas importadas com sucesso!")
except ImportError as e:
    print(f"❌ Erro ao importar ferramentas: {e}")
    sys.exit(1)

def executar_diagnostico_simples():
    """Executa um diagnóstico simplificado sem CrewAI"""
    print("🎯 DIAGNÓSTICO COMERCIAL SIMPLIFICADO")
    print("=" * 50)
    
    # 1. Ler dados
    print("📊 1. Lendo dados de entrada...")
    csv_reader = LerDadosCSV()
    resultado_dados = csv_reader._run("dados_entrada")
    
    if resultado_dados["status"] != "sucesso":
        print(f"❌ Erro ao ler dados: {resultado_dados}")
        return
    
    dados = resultado_dados["dados"]
    print("✅ Dados lidos com sucesso!")
    
    # 2. Extrair valores
    print("\n🔢 2. Extraindo valores...")
    receita = dados["Receita_Total"]["valor"]
    custo_vendas = dados["Custo_Vendas_Marketing"]["valor"] 
    novos_clientes = dados["Novos_Clientes"]["valor"]
    propostas = dados["Propostas_Enviadas"]["valor"]
    fechados = dados["Negocios_Fechados"]["valor"]
    
    print(f"Receita: R$ {receita:,.2f}")
    print(f"Custo Vendas: R$ {custo_vendas:,.2f}")
    print(f"Novos Clientes: {novos_clientes}")
    
    # 3. Calcular métricas
    print("\n🧮 3. Calculando métricas...")
    
    # CAC
    cac_tool = CalcularCAC()
    cac_resultado = cac_tool._run(custo_vendas, novos_clientes)
    print(f"CAC: {cac_resultado}")
    
    # LTV
    ltv_tool = CalcularLTV()
    ltv_resultado = ltv_tool._run(receita, novos_clientes)
    print(f"LTV: {ltv_resultado}")
    
    # ROI
    roi_tool = CalcularROISimples()
    roi_resultado = roi_tool._run(receita, custo_vendas)
    print(f"ROI: {roi_resultado}")
    
    # Win Rate
    winrate_tool = CalcularWinRate()
    winrate_resultado = winrate_tool._run(fechados, propostas)
    print(f"Win Rate: {winrate_resultado}")
    
    # 4. Criar relatório
    print("\n📄 4. Gerando relatório...")
    
    insights = [
        f"CAC de R$ {cac_resultado['cac']} está {cac_resultado['status']}",
        f"LTV de R$ {ltv_resultado['ltv']} mostra potencial {ltv_resultado['status']}",
        f"ROI de {roi_resultado['roi']}% indica performance {roi_resultado['status']}",
        f"Win Rate de {winrate_resultado['win_rate']}% está {winrate_resultado['status']}"
    ]
    
    recomendacoes = [
        "Focar em otimização do CAC se necessário",
        "Aumentar estratégias de retenção para maximizar LTV",
        "Melhorar processo de vendas para aumentar Win Rate",
        "Monitorar ROI por canal de aquisição"
    ]
    
    relatorio_tool = ExportarRelatorioMD()
    dados_analise = {
        "receita_total": receita,
        "roi": roi_resultado["roi"],
        "cac": cac_resultado["cac"],
        "ltv": ltv_resultado["ltv"],
        "win_rate": winrate_resultado["win_rate"]
    }
    
    relatorio = relatorio_tool._run(dados_analise, insights, recomendacoes)
    
    # 5. Salvar relatório
    output_path = project_root / "outputs"
    output_path.mkdir(exist_ok=True)
    
    relatorio_file = output_path / "diagnostico_executivo.md"
    with open(relatorio_file, "w", encoding="utf-8") as f:
        f.write(relatorio)
    
    print(f"📁 Relatório salvo em: {relatorio_file}")
    
    # 6. Salvar métricas no CSV
    print("\n💾 5. Salvando métricas...")
    metricas_calculadas = {
        "CAC": cac_resultado["cac"],
        "LTV": ltv_resultado["ltv"], 
        "ROI": roi_resultado["roi"],
        "Win_Rate": winrate_resultado["win_rate"]
    }
    
    csv_saver = SalvarMetricasCSV()
    save_result = csv_saver._run(metricas_calculadas)
    print(f"Resultado salvamento: {save_result}")
    
    print("\n🎉 DIAGNÓSTICO CONCLUÍDO!")
    print(f"📊 Métricas principais:")
    print(f"   • CAC: R$ {cac_resultado['cac']}")
    print(f"   • LTV: R$ {ltv_resultado['ltv']}")
    print(f"   • ROI: {roi_resultado['roi']}%")
    print(f"   • Win Rate: {winrate_resultado['win_rate']}%")
    print(f"📄 Relatório completo em: outputs/diagnostico_executivo.md")

if __name__ == "__main__":
    executar_diagnostico_simples()
