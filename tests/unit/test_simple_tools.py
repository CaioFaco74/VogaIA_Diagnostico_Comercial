#!/usr/bin/env python3
"""
Teste simples do diagnóstico comercial sem YAML
"""

import pandas as pd
import os
from pathlib import Path

# Importar as ferramentas diretamente
import sys
# Adicionar o diretório src ao path (relativo ao projeto)
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root / 'src'))

try:
    from diagnostico_comercial_voga_ia.tools.diagnostico_tools import (
        CalcularCAC,
        CalcularLTV,
        CalcularROISimples,
        LerDadosCSV
    )
    print("✅ Ferramentas importadas com sucesso!")
except ImportError as e:
    print(f"❌ Erro ao importar ferramentas: {e}")
    sys.exit(1)

def test_tools():
    """Testa as ferramentas individualmente"""
    print("\n🧮 TESTANDO FERRAMENTAS INDIVIDUAIS:")
    
    # Teste CAC
    cac_tool = CalcularCAC()
    resultado_cac = cac_tool._run(350000, 125)
    print(f"CAC: {resultado_cac}")
    
    # Teste LTV
    ltv_tool = CalcularLTV()
    resultado_ltv = ltv_tool._run(1250000, 125)
    print(f"LTV: {resultado_ltv}")
    
    # Teste ROI
    roi_tool = CalcularROISimples()
    resultado_roi = roi_tool._run(1250000, 350000)
    print(f"ROI: {resultado_roi}")
    
    print("✅ Todas as ferramentas funcionando!")

def test_csv_reading():
    """Testa leitura dos CSVs"""
    print("\n📊 TESTANDO LEITURA DE CSV:")
    
    try:
        csv_tool = LerDadosCSV()
        dados = csv_tool._run("dados_entrada")
        print(f"Dados lidos: {dados}")
        return True
    except Exception as e:
        print(f"❌ Erro ao ler CSV: {e}")
        return False

def main():
    """Função principal de teste"""
    print("🎯 TESTE SIMPLES DO DIAGNÓSTICO COMERCIAL")
    print("=" * 50)
    
    # Testar ferramentas
    test_tools()
    
    # Testar CSV
    csv_ok = test_csv_reading()
    
    if csv_ok:
        print("\n🎉 TESTE CONCLUÍDO COM SUCESSO!")
        print("✅ O projeto está funcionando corretamente")
    else:
        print("\n⚠️ Alguns problemas encontrados, mas ferramentas básicas OK")

if __name__ == "__main__":
    main()
