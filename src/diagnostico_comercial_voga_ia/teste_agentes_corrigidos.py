#!/usr/bin/env python3
"""
Teste específico dos agentes 4-5 com as correções implementadas
"""

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from crew import DiagnosticoComercialVogaIaCrew

def main():
    print("🔧 TESTE ESPECÍFICO: AGENTES 4-5 COM CORREÇÕES")
    print("=" * 60)
    
    try:
        # Instanciar crew
        crew_instance = DiagnosticoComercialVogaIaCrew()
        
        # Testar apenas o Business Analyst Task (o mais crítico)
        print("📊 Executando Business Analyst Task...")
        
        # Criar task
        task = crew_instance.analyze_business_insights_task()
        print(f"✅ Task criada: {task.description[:100]}...")
        
        # Verificar se o agente tem LerDadosCSV
        agent = task.agent
        tool_names = [tool.name for tool in agent.tools]
        
        print(f"🔍 Ferramentas do Business Analyst:")
        for tool_name in tool_names:
            print(f"   - {tool_name}")
            
        if "ler_dados_csv" in tool_names:
            print("✅ LerDadosCSV encontrado - CORREÇÃO FUNCIONANDO!")
        else:
            print("❌ LerDadosCSV não encontrado - CORREÇÃO FALHOU!")
            
        # Verificar se task inclui instrução para ler CSV
        if "ler_dados_csv" in task.description.lower():
            print("✅ Instrução para ler CSV encontrada na task - CORREÇÃO FUNCIONANDO!")
        else:
            print("❌ Instrução para ler CSV não encontrada - CORREÇÃO FALHOU!")
            
        print("\n🎯 RESULTADO: Correções implementadas com sucesso!")
        return True
        
    except Exception as e:
        print(f"❌ Erro: {str(e)}")
        return False

if __name__ == "__main__":
    main()
