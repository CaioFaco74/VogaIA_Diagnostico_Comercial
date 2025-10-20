#!/usr/bin/env python3
"""
Teste das Correções da Fase 1 - Diagnóstico Comercial Voga.IA
Valida as correções críticas aplicadas antes de prosseguir.
"""

import os
import sys
import pandas as pd

def test_memory_and_context():
    """Testa se memory e share_crew foram adicionados ao crew.py"""
    crew_path = "src/diagnostico_comercial_voga_ia/crew.py"
    
    print("🔍 Testando correções no crew.py...")
    
    if not os.path.exists(crew_path):
        print("❌ Arquivo crew.py não encontrado!")
        return False
    
    with open(crew_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    corrections_found = {
        "memory=True": "memory=True" in content,
        "share_crew=True": "share_crew=True" in content,
        "max_iter=1": "max_iter=1" in content
    }
    
    print("📋 Verificações:")
    for correction, found in corrections_found.items():
        status = "✅" if found else "❌"
        print(f"   {status} {correction}")
    
    return all(corrections_found.values())

def test_encoding_fix():
    """Testa se o fix de encoding foi aplicado nas tools"""
    tools_path = "src/diagnostico_comercial_voga_ia/tools/diagnostico_tools.py"
    
    print("\n🔍 Testando correção de encoding...")
    
    if not os.path.exists(tools_path):
        print("❌ Arquivo diagnostico_tools.py não encontrado!")
        return False
    
    with open(tools_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    encoding_fixes = {
        "errors='replace'": "errors='replace'" in content,
        "UnicodeEncodeError": "UnicodeEncodeError" in content,
        "encoding='utf-8', errors='ignore'": "encoding='utf-8', errors='ignore'" in content
    }
    
    print("📋 Verificações de encoding:")
    for fix, found in encoding_fixes.items():
        status = "✅" if found else "❌"
        print(f"   {status} {fix}")
    
    return all(encoding_fixes.values())

def test_task_improvements():
    """Testa se as melhorias nas tasks foram aplicadas"""
    tasks_path = "src/diagnostico_comercial_voga_ia/config/tasks.yaml"
    
    print("\n🔍 Testando melhorias nas tasks...")
    
    if not os.path.exists(tasks_path):
        print("❌ Arquivo tasks.yaml não encontrado!")
        return False
    
    with open(tasks_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    task_improvements = {
        "DADOS REAIS DOS CSVs": "DADOS REAIS DOS CSVs" in content,
        "PASSO 1 OBRIGATÓRIO": "PASSO 1 OBRIGATÓRIO" in content,
        "valores REAIS": "valores REAIS" in content,
        "não valores fictícios": "não valores fictícios" in content
    }
    
    print("📋 Verificações das tasks:")
    for improvement, found in task_improvements.items():
        status = "✅" if found else "❌"
        print(f"   {status} {improvement}")
    
    return all(task_improvements.values())

def test_data_files():
    """Verifica se os arquivos de dados estão presentes"""
    data_files = [
        "src/diagnostico_comercial_voga_ia/data/dados_entrada.csv",
        "src/diagnostico_comercial_voga_ia/data/metricas_calculadas.csv"
    ]
    
    print("\n🔍 Testando presença dos arquivos de dados...")
    
    all_present = True
    for file_path in data_files:
        exists = os.path.exists(file_path)
        status = "✅" if exists else "❌"
        print(f"   {status} {file_path}")
        if not exists:
            all_present = False
    
    return all_present

def test_csv_data_integrity():
    """Testa se os dados nos CSVs estão íntegros"""
    dados_path = "src/diagnostico_comercial_voga_ia/data/dados_entrada.csv"
    
    print("\n🔍 Testando integridade dos dados...")
    
    if not os.path.exists(dados_path):
        print("❌ Arquivo dados_entrada.csv não encontrado!")
        return False
    
    try:
        df = pd.read_csv(dados_path)
        
        # Verificar colunas essenciais
        required_columns = ['campo', 'valor', 'unidade', 'descricao']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            print(f"❌ Colunas faltando: {missing_columns}")
            return False
        
        # Verificar se há dados
        if len(df) == 0:
            print("❌ CSV está vazio!")
            return False
        
        # Verificar alguns campos essenciais
        essential_fields = ['Receita_Total', 'Custo_Vendas_Marketing', 'Novos_Clientes']
        missing_fields = [field for field in essential_fields if field not in df['campo'].values]
        
        if missing_fields:
            print(f"⚠️  Campos essenciais faltando: {missing_fields}")
        
        print(f"✅ CSV com {len(df)} registros encontrados")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao ler CSV: {str(e)}")
        return False

def main():
    """Executa todos os testes da Fase 1"""
    print("🚀 TESTE DAS CORREÇÕES DA FASE 1 - DIAGNÓSTICO COMERCIAL VOGA.IA")
    print("=" * 70)
    
    tests = [
        ("Context & Memory", test_memory_and_context),
        ("Encoding Fix", test_encoding_fix),
        ("Task Improvements", test_task_improvements),
        ("Data Files", test_data_files),
        ("CSV Integrity", test_csv_data_integrity)
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        print(f"\n🧪 {test_name.upper()}")
        print("-" * 40)
        results[test_name] = test_func()
    
    # Resumo final
    print("\n" + "=" * 70)
    print("📊 RESUMO DOS TESTES")
    print("=" * 70)
    
    passed = 0
    total = len(tests)
    
    for test_name, result in results.items():
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n🎯 RESULTADO: {passed}/{total} testes passaram")
    
    if passed == total:
        print("🎉 FASE 1 CONCLUÍDA COM SUCESSO!")
        print("✅ Todas as correções críticas foram aplicadas")
        print("🚀 Pronto para executar o sistema corrigido")
    else:
        print("⚠️  ALGUMAS CORREÇÕES PRECISAM DE ATENÇÃO")
        print("🔧 Revisar os itens que falharam antes de prosseguir")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
