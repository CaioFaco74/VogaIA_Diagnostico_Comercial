#!/bin/bash

echo "🚀 TESTANDO DIAGNÓSTICO COMERCIAL - VERSÃO SIMPLES"
echo "=" 

# Navegar para o diretório
cd /Users/caiofaco/Desktop/crewaivogaia/diagnostico_comercial_voga_ia

echo "📂 Diretório atual: $(pwd)"

# Testar Python
echo "🐍 Testando Python..."
python3 --version

# Criar outputs directory
mkdir -p src/diagnostico_comercial_voga_ia/outputs

# Executar versão simples
echo "⚡ Executando diagnóstico simples..."
python3 src/diagnostico_comercial_voga_ia/main_simples.py

echo "✅ Teste concluído!"
