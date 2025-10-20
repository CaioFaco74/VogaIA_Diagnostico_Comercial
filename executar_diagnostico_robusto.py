#!/usr/bin/env python3
"""
🚀 EXECUTAR DIAGNÓSTICO COMERCIAL VOGA.IA - VERSÃO ROBUSTA
Script principal para executar o enxame de 8 agentes CrewAI
"""

import sys
import os
from pathlib import Path
from dotenv import load_dotenv
import time

# Configurar paths do projeto
project_root = Path(__file__).parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))

# Carregar variáveis de ambiente
load_dotenv()

def verificar_ambiente():
    """Verifica se o ambiente está configurado corretamente"""
    print("🔍 VERIFICANDO AMBIENTE...")
    
    # Verificar OpenAI API Key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("⚠️  ATENÇÃO: OPENAI_API_KEY não encontrada")
        print("📝 Configure sua chave API no arquivo .env")
        print("💡 Exemplo: OPENAI_API_KEY=sk-...")
        
        response = input("\n🤔 Continuar sem OpenAI? (s/N): ").lower()
        if response != 's':
            print("👋 Configure a API key e execute novamente!")
            return False
    else:
        print("✅ OpenAI API Key encontrada")
    
    # Verificar estrutura de diretórios
    required_dirs = [
        src_path / "diagnostico_comercial_voga_ia",
        src_path / "diagnostico_comercial_voga_ia" / "data",
        src_path / "diagnostico_comercial_voga_ia" / "outputs",
        src_path / "diagnostico_comercial_voga_ia" / "tools"
    ]
    
    for dir_path in required_dirs:
        if dir_path.exists():
            print(f"✅ Diretório encontrado: {dir_path.name}")
        else:
            print(f"❌ Diretório não encontrado: {dir_path}")
            return False
    
    return True

def importar_modulos():
    """Importa os módulos necessários"""
    print("\n📦 IMPORTANDO MÓDULOS...")
    
    try:
        from diagnostico_comercial_voga_ia.crew import DiagnosticoComercialVogaIaCrew
        print("✅ DiagnosticoComercialVogaIaCrew importado com sucesso!")
        return DiagnosticoComercialVogaIaCrew
        
    except ImportError as e:
        print(f"❌ Erro de importação: {e}")
        print("🔧 Tentando corrigir paths...")
        
        # Adicionar mais paths
        possible_paths = [
            project_root / "src",
            project_root / "src" / "diagnostico_comercial_voga_ia",
            project_root
        ]
        
        for path in possible_paths:
            if path not in sys.path:
                sys.path.insert(0, str(path))
                print(f"📁 Adicionado ao path: {path}")
        
        # Tentar importar novamente
        try:
            from diagnostico_comercial_voga_ia.crew import DiagnosticoComercialVogaIaCrew
            print("✅ Importação bem-sucedida após correção de paths!")
            return DiagnosticoComercialVogaIaCrew
        except ImportError as e2:
            print(f"❌ Falha na importação mesmo após correções: {e2}")
            return None

def verificar_dados():
    """Verifica se os dados de entrada existem"""
    print("\n📊 VERIFICANDO DADOS DE ENTRADA...")
    
    dados_path = src_path / "diagnostico_comercial_voga_ia" / "data" / "dados_entrada.csv"
    
    if dados_path.exists():
        print(f"✅ Arquivo de dados encontrado: {dados_path}")
        return True
    else:
        print(f"❌ Arquivo de dados não encontrado: {dados_path}")
        return False

def executar_diagnostico():
    """Executa o diagnóstico completo"""
    print("\n🚀 INICIANDO DIAGNÓSTICO COMERCIAL VOGA.IA")
    print("="*80)
    print("🤖 ENXAME DE 8 AGENTES ESPECIALIZADOS:")
    print("   1️⃣  Data Collector Agent     → Coleta e validação")
    print("   2️⃣  Data Governance Agent    → Governança de dados")  
    print("   3️⃣  Metrics Calculator Agent → Cálculo de métricas")
    print("   4️⃣  Business Analyst Agent   → Análise estratégica")
    print("   5️⃣  Alert Monitor Agent      → Sistema de alertas")
    print("   6️⃣  Visualization Agent      → Gráficos e tabelas")
    print("   7️⃣  Dashboard Creator Agent  → Especificações BI")
    print("   8️⃣  Report Generator Agent   → Relatório executivo")
    print("="*80)
    
    # Verificar ambiente
    if not verificar_ambiente():
        return False
    
    # Importar módulos
    DiagnosticoComercialVogaIaCrew = importar_modulos()
    if not DiagnosticoComercialVogaIaCrew:
        return False
    
    # Verificar dados
    if not verificar_dados():
        print("⚠️  Continuando sem verificação de dados...")
    
    # Configurar inputs
    inputs = {
        'cliente': 'Diagnóstico Comercial Voga.IA - Execução Completa',
        'periodo': '2025',
        'dados_csv_path': 'data/dados_entrada.csv',
        'metricas_csv_path': 'data/metricas_calculadas.csv',
        'output_path': 'outputs/',
        'gerar_excel': True,
        'gerar_dashboard': True,
        'gerar_relatorios_individuais': True,
        'data_execucao': time.strftime("%Y-%m-%d"),
        'hora_execucao': time.strftime("%H:%M:%S"),
        'executado_por': 'Sistema Voga.IA v1.0'
    }
    
    print(f"\n📋 CONFIGURAÇÕES DA EXECUÇÃO:")
    for key, value in inputs.items():
        print(f"   • {key}: {value}")
    
    print(f"\n⏰ Início: {time.strftime('%H:%M:%S')}")
    print("🕐 Tempo estimado: 5-8 minutos")
    print("📊 Aguarde... Os agentes estão trabalhando!")
    
    try:
        # Criar instância do crew
        crew_instance = DiagnosticoComercialVogaIaCrew()
        
        # Executar o kickoff
        resultado = crew_instance.crew().kickoff(inputs=inputs)
        
        print(f"\n⏰ Conclusão: {time.strftime('%H:%M:%S')}")
        print("\n🎉 DIAGNÓSTICO CONCLUÍDO COM SUCESSO!")
        print("📁 Resultados salvos em: src/diagnostico_comercial_voga_ia/outputs/")
        print("📊 Verifique os relatórios gerados pelos 8 agentes")
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERRO durante execução: {e}")
        print("🔍 Detalhes do erro:")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Função principal"""
    print("🎯 DIAGNÓSTICO COMERCIAL VOGA.IA")
    print("🤖 Sistema Automatizado com 8 Agentes CrewAI")
    print("📈 Análise Profunda de Performance Comercial")
    print()
    
    sucesso = executar_diagnostico()
    
    if sucesso:
        print("\n✅ EXECUÇÃO COMPLETADA COM SUCESSO!")
        print("🔗 Para visualizar os resultados:")
        print("   📁 cd src/diagnostico_comercial_voga_ia/outputs")
        print("   📄 ls -la")
        print("   📖 cat *.md")
    else:
        print("\n❌ EXECUÇÃO FALHOU!")
        print("🔧 Verifique os erros acima e tente novamente")

if __name__ == "__main__":
    main()
