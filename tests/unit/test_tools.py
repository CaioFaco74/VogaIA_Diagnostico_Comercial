#!/usr/bin/env python3
"""
Script de teste para verificar o funcionamento dos agentes
Diagnóstico Comercial Voga.IA
"""

import os
import sys
from datetime import datetime
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Adicionar o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def test_metrics_calculator():
    """Testa especificamente o agente que calcula métricas"""
    print("🔍 Testando Agente Metrics Calculator...")
    
    try:
        from diagnostico_comercial_voga_ia.crew import DiagnosticoComercialVogaIaCrew
        from diagnostico_comercial_voga_ia.tools.diagnostico_tools import LerDadosCSV, SalvarMetricasCSV
        
        # Criar instância do crew
        crew = DiagnosticoComercialVogaIaCrew()
        
        # Testar ferramentas diretamente
        ler_tool = LerDadosCSV()
        salvar_tool = SalvarMetricasCSV()
        
        # Ler dados de entrada
        dados = ler_tool._run("dados_entrada")
        print(f"✅ Dados lidos: {len(dados)} campos encontrados")
        
        # Testar cálculo de algumas métricas
        from diagnostico_comercial_voga_ia.tools.diagnostico_tools import CalcularCAC, CalcularLTV
        
        cac_tool = CalcularCAC()
        ltv_tool = CalcularLTV()
        
        cac_result = cac_tool._run(
            custo_vendas_marketing=dados.get('Custo_Vendas_Marketing', 350000),
            novos_clientes=dados.get('Novos_Clientes', 125)
        )
        
        ltv_result = ltv_tool._run(
            receita_total=dados.get('Receita_Total', 1250000),
            clientes_ativos=dados.get('Clientes_Finais', 520)
        )
        
        print(f"✅ CAC calculado: R$ {cac_result.get('cac', 0):,.2f}")
        print(f"✅ LTV calculado: R$ {ltv_result.get('ltv', 0):,.2f}")
        
        # Testar salvamento
        metricas_teste = {
            'CAC': cac_result.get('cac', 0),
            'LTV': ltv_result.get('ltv', 0)
        }
        
        salvar_result = salvar_tool._run(metricas_teste)
        print(f"✅ Salvamento: {salvar_result.get('status', 'erro')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro no teste: {str(e)}")
        return False

def test_report_generation():
    """Testa a geração de relatórios"""
    print("\n📝 Testando Geração de Relatórios...")
    
    try:
        from diagnostico_comercial_voga_ia.tools.diagnostico_tools import SalvarRelatorioAgente
        
        tool = SalvarRelatorioAgente()
        
        # Testar salvamento de relatório
        relatorio_teste = """
# Teste de Relatório

Este é um relatório de teste para verificar se a ferramenta está funcionando corretamente.

## Métricas Testadas:
- CAC: R$ 2.800,00
- LTV: R$ 2.403,85
- ROI: 257,14%

## Status: ✅ Funcionando
        """
        
        result = tool._run(
            conteudo_relatorio=relatorio_teste,
            nome_agente="Test Agent",
            numero_agente=99
        )
        
        print(f"✅ Relatório salvo: {result.get('status', 'erro')}")
        print(f"📁 Arquivo: {result.get('arquivo', 'N/A')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro no teste: {str(e)}")
        return False

def check_file_timestamps():
    """Verifica timestamps dos arquivos"""
    print("\n⏰ Verificando Timestamps dos Arquivos...")
    
    import os
    from datetime import datetime
    
    # Verificar arquivo de métricas
    metricas_path = "src/diagnostico_comercial_voga_ia/data/metricas_calculadas.csv"
    if os.path.exists(metricas_path):
        timestamp = os.path.getmtime(metricas_path)
        data_mod = datetime.fromtimestamp(timestamp)
        print(f"📊 Métricas calculadas: {data_mod.strftime('%d/%m/%Y %H:%M:%S')}")
    
    # Verificar relatórios
    outputs_dir = "src/diagnostico_comercial_voga_ia/outputs"
    if os.path.exists(outputs_dir):
        for file in os.listdir(outputs_dir):
            if file.endswith('.md'):
                file_path = os.path.join(outputs_dir, file)
                timestamp = os.path.getmtime(file_path)
                data_mod = datetime.fromtimestamp(timestamp)
                print(f"📄 {file}: {data_mod.strftime('%d/%m/%Y %H:%M:%S')}")

def main():
    """Função principal de teste"""
    print("🚀 Iniciando Testes do Sistema Diagnóstico Comercial Voga.IA")
    print("=" * 60)
    
    # Testar métricas
    metrics_ok = test_metrics_calculator()
    
    # Testar relatórios
    reports_ok = test_report_generation()
    
    # Verificar timestamps
    check_file_timestamps()
    
    print("\n" + "=" * 60)
    print("📋 RESUMO DOS TESTES:")
    print(f"✅ Métricas Calculator: {'OK' if metrics_ok else 'ERRO'}")
    print(f"✅ Geração de Relatórios: {'OK' if reports_ok else 'ERRO'}")
    
    if metrics_ok and reports_ok:
        print("\n🎉 Todos os testes passaram! O sistema está funcionando corretamente.")
    else:
        print("\n⚠️ Alguns testes falharam. Verifique os erros acima.")

if __name__ == "__main__":
    main() 