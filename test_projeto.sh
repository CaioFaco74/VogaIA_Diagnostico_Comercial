#!/bin/bash

echo "🚀 Testando Diagnóstico Comercial Voga.IA"
echo "=" * 50

# Navegar para o diretório do projeto
cd /Users/caiofaco/Desktop/crewaivogaia/diagnostico_comercial_voga_ia

# Verificar se temos Python
echo "🐍 Verificando Python..."
python3 --version

# Criar virtual environment se não existir
if [ ! -d ".venv" ]; then
    echo "📦 Criando virtual environment..."
    python3 -m venv .venv
fi

# Ativar virtual environment
echo "🔧 Ativando virtual environment..."
source .venv/bin/activate

# Instalar dependências
echo "📥 Instalando dependências..."
pip install -e .

# Executar o projeto
echo "🎯 Executando diagnóstico..."
python src/diagnostico_comercial_voga_ia/main.py

echo "✅ Teste concluído!"
