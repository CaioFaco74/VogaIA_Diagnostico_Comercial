#!/usr/bin/env python3
"""
Teste rápido para verificar se as importações do CrewAI estão funcionando
"""

import sys
import os

print("🔍 TESTE DE IMPORTAÇÕES DO CREWAI")
print("=" * 50)

# Adicionar paths necessários
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src', 'diagnostico_comercial_voga_ia'))

try:
    print("✅ Testando import do crewai...")
    import crewai
    print(f"   Versão CrewAI: {getattr(crewai, '__version__', 'Desconhecida')}")
except Exception as e:
    print(f"❌ Erro ao importar crewai: {e}")
    sys.exit(1)

try:
    print("✅ Testando import crewai.tools...")
    from crewai.tools import BaseTool
    print(f"   BaseTool importada com sucesso: {BaseTool}")
except Exception as e:
    print(f"❌ Erro ao importar BaseTool: {e}")
    
    # Tentar imports alternativos
    try:
        print("🔄 Tentando import alternativo de crewai_tools...")
        from crewai_tools import BaseTool
        print(f"   BaseTool importada de crewai_tools: {BaseTool}")
    except Exception as e2:
        print(f"❌ Erro no import alternativo: {e2}")
        
        try:
            print("🔄 Tentando import diretamente de crewai...")
            from crewai import BaseTool
            print(f"   BaseTool importada de crewai: {BaseTool}")
        except Exception as e3:
            print(f"❌ Erro no import direto: {e3}")
            sys.exit(1)

try:
    print("✅ Testando imports das ferramentas customizadas...")
    from diagnostico_comercial_voga_ia.tools.diagnostico_tools import (
        CalcularCAC,
        CalcularLTV,
        CalcularROISimples
    )
    print("   Ferramentas customizadas importadas com sucesso")
    
    # Teste rápido de instanciação
    cac_tool = CalcularCAC()
    print(f"   Ferramenta CAC instanciada: {cac_tool.name}")
    
except Exception as e:
    print(f"❌ Erro ao importar ferramentas customizadas: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n🎉 TODOS OS IMPORTS FORAM EXECUTADOS COM SUCESSO!")
print("✅ O problema de importação foi resolvido")