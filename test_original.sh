#!/bin/bash

echo "🎯 TESTANDO PROJETO ORIGINAL - 8 AGENTES CREWAI"
echo "================================================================"

# Navegar para o diretório do projeto
cd /Users/caiofaco/Desktop/crewaivogaia/diagnostico_comercial_voga_ia

echo "📂 Diretório: $(pwd)"

# Verificar se temos .env
if [ ! -f ".env" ]; then
    echo "⚠️  Arquivo .env não encontrado!"
    echo "📝 Criando .env básico..."
    cp .env.example .env
fi

# Verificar Python
echo "🐍 Python version:"
python3 --version

# Criar virtual environment se não existir
if [ ! -d ".venv" ]; then
    echo "📦 Criando virtual environment..."
    python3 -m venv .venv
fi

# Ativar virtual environment
echo "🔧 Ativando virtual environment..."
source .venv/bin/activate

# Instalar projeto em modo desenvolvimento
echo "📥 Instalando projeto..."
pip install -e .

# Criar diretório de outputs
mkdir -p src/diagnostico_comercial_voga_ia/outputs

# Executar o projeto ORIGINAL
echo ""
echo "🚀 EXECUTANDO ENXAME DE 8 AGENTES CREWAI..."
echo "================================================================"
python src/diagnostico_comercial_voga_ia/main.py

echo ""
echo "✅ Execução finalizada!"
echo "📁 Verifique os arquivos em: src/diagnostico_comercial_voga_ia/outputs/"
