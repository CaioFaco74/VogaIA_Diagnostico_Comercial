#!/usr/bin/env python3
"""
Teste das correções implementadas
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from tools.diagnostico_tools import LerDadosCSV, CriarGraficosPerformance, GerarPlanilhaDiagnostico

def test_ler_dados_csv():
    """Testa se a ferramenta LerDadosCSV está funcionando"""
    print("🔧 Testando LerDadosCSV...")
    
    # Teste leitura de métricas
    tool = LerDadosCSV()
    resultado = tool._run("metricas")
    
    if resultado.get("status") == "sucesso":
        metricas = resultado.get("metricas", [])
        print(f"✅ Métricas lidas: {len(metricas)} registros")
        
        # Mostrar algumas métricas principais
        metricas_dict = {m.get('metrica', ''): m.get('valor', 0) for m in metricas}
        print(f"   - CAC: {metricas_dict.get('CAC', 'N/A')}")
        print(f"   - LTV: {metricas_dict.get('LTV', 'N/A')}")
        print(f"   - ROI: {metricas_dict.get('ROI', 'N/A')}")
        print(f"   - Win Rate: {metricas_dict.get('Win_Rate', 'N/A')}")
        return True
    else:
        print(f"❌ Erro: {resultado.get('mensagem', 'Erro desconhecido')}")
        return False

def test_criar_graficos():
    """Testa se a ferramenta CriarGraficosPerformance está funcionando"""
    print("\n🔧 Testando CriarGraficosPerformance...")
    
    tool = CriarGraficosPerformance()
    resultado = tool._run()  # Sem parâmetros - deve ler do CSV
    
    if "erro" not in resultado:
        print("✅ Gráficos gerados com sucesso!")
        for nome, grafico in resultado.items():
            print(f"   - {nome}: {len(grafico)} caracteres")
        return True
    else:
        print(f"❌ Erro: {resultado.get('erro', 'Erro desconhecido')}")
        return False

def test_gerar_planilha():
    """Testa se a ferramenta GerarPlanilhaDiagnostico está funcionando"""
    print("\n🔧 Testando GerarPlanilhaDiagnostico...")
    
    tool = GerarPlanilhaDiagnostico()
    resultado = tool._run()  # Sem parâmetros - deve ler do CSV
    
    if resultado.get("status") == "sucesso":
        estrutura = resultado.get("estrutura_planilha", {})
        print("✅ Estrutura de planilha gerada!")
        
        resumo = estrutura.get("resumo_executivo", {})
        print(f"   - Empresa: {resumo.get('empresa', 'N/A')}")
        print(f"   - Porte: {resumo.get('porte', 'N/A')}")
        
        metricas = resumo.get("metricas_principais", {})
        print(f"   - ROI: {metricas.get('roi', 'N/A')}")
        print(f"   - CAC: {metricas.get('cac', 'N/A')}")
        return True
    else:
        print(f"❌ Erro: {resultado.get('mensagem', 'Erro desconhecido')}")
        return False

def main():
    print("🚀 TESTANDO CORREÇÕES IMPLEMENTADAS")
    print("=" * 50)
    
    sucessos = 0
    total = 3
    
    if test_ler_dados_csv():
        sucessos += 1
    
    if test_criar_graficos():
        sucessos += 1
        
    if test_gerar_planilha():
        sucessos += 1
    
    print("\n" + "=" * 50)
    print(f"📊 RESULTADO: {sucessos}/{total} testes passaram")
    
    if sucessos == total:
        print("🎉 TODAS AS CORREÇÕES FUNCIONANDO!")
        return True
    else:
        print("⚠️  Algumas correções precisam de ajustes")
        return False

if __name__ == "__main__":
    main()
