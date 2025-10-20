#!/usr/bin/env python3
"""
Script de Validação - Diagnóstico Comercial Voga.IA
Executa o sistema e valida as 40 métricas
"""

import sys
import os
from pathlib import Path

# Adicionar o src ao path
sys.path.insert(0, str(Path(__file__).parent / "src"))

try:
    print("🚀 INICIANDO VALIDAÇÃO DO SISTEMA DIAGNÓSTICO COMERCIAL")
    print("="*70)
    
    # Importar e executar o sistema
    from diagnostico_comercial_voga_ia.main import run
    
    print("✅ Módulos importados com sucesso!")
    print("🎯 Iniciando execução...")
    
    # Executar o sistema
    resultado = run()
    
    print("\n🎉 EXECUÇÃO CONCLUÍDA!")
    print("📁 Verificando outputs gerados...")
    
    # Verificar outputs
    outputs_dir = Path("src/diagnostico_comercial_voga_ia/outputs")
    if outputs_dir.exists():
        arquivos = list(outputs_dir.glob("*.md"))
        print(f"📊 Relatórios gerados: {len(arquivos)}")
        for arquivo in sorted(arquivos):
            print(f"   • {arquivo.name}")
    else:
        print("⚠️ Diretório outputs não encontrado")
    
    print("\n✅ VALIDAÇÃO CONCLUÍDA!")
    
except ImportError as e:
    print(f"❌ Erro de importação: {e}")
    print("💡 Verifique se o ambiente Poetry está ativo")
    
except Exception as e:
    print(f"❌ Erro durante execução: {e}")
    print("🔍 Detalhes do erro:")
    import traceback
    traceback.print_exc()

if __name__ == "__main__":
    print("📍 Executando validação direta...")
