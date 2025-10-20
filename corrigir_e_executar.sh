#!/bin/bash

echo "🔧 CORREÇÃO RÁPIDA - DIAGNÓSTICO COMERCIAL VOGA.IA"
echo "=" * 60

# Navegar para o diretório do projeto
cd /Users/caiofaco/Desktop/crewaivogaia/diagnostico_comercial_voga_ia

# Ativar ambiente virtual
echo "🐍 Ativando ambiente virtual..."
source venv-crewai/bin/activate

# Reinstalar o projeto em modo editável
echo "📦 Reinstalando projeto..."
pip install -e . --force-reinstall

# Executar o script simples
echo "🚀 Executando diagnóstico..."
python executar_simples.py

echo "✅ Execução concluída!"
