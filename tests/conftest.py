"""
Configuração do pytest - Diagnóstico Comercial Voga.IA

Este arquivo contém fixtures e configurações compartilhadas por todos os testes.
"""

import os
import sys
import pytest
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Adicionar diretório src ao path para imports
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))


@pytest.fixture(scope="session")
def project_root():
    """Retorna o diretório raiz do projeto"""
    return PROJECT_ROOT


@pytest.fixture(scope="session")
def data_dir(project_root):
    """Retorna o diretório de dados de entrada"""
    return project_root / "src" / "diagnostico_comercial_voga_ia" / "data"


@pytest.fixture(scope="session")
def output_dir(project_root):
    """Retorna o diretório de saída de relatórios"""
    return project_root / "src" / "diagnostico_comercial_voga_ia" / "outputs"


@pytest.fixture
def sample_input_data():
    """Dados de entrada de exemplo para testes"""
    return {
        'Receita_Total': 1250000,
        'Custo_Vendas_Marketing': 350000,
        'Novos_Clientes': 125,
        'Propostas_Enviadas': 425,
        'Leads_Gerados': 1850,
        'Negocios_Fechados': 95,
        'Ciclo_Vendas_Dias': 45,
        'Reps_Ativos': 8,
        'Custo_Ferramentas': 25000,
        'Custo_Treinamento': 15000,
        'Clientes_Iniciais': 450,
        'Clientes_Finais': 520,
        'Setor_Empresa': 'SaaS',
        'Porte_Empresa': 'Media',
        'Regiao_Atuacao': 'Sudeste',
        'Ano_Fundacao': 2018,
        'Custo_Produto_Vendido': 400000,
        'Meta_Receita_Periodo': 1500000,
        'Margem_Bruta_Esperada': 60,
        'MQL_Gerados': 800,
        'SQL_Gerados': 400,
        'Reunioes_Realizadas': 300,
        'Situacao_Atual': 'Crescimento_Acelerado',
        'Problema_Principal': 'CAC_Alto_Conversao_Baixa',
        'Impacto_Problema': 'Reducao_Margem_Crescimento_Lento',
        'Evento_Critico': 'Lancamento_Novo_Produto_Q4',
        'Decisao_Esperada': 'Otimizar_Marketing_Treinar_Vendas'
    }


@pytest.fixture
def expected_metrics():
    """Métricas esperadas para validação"""
    return {
        'CAC': 2800.0,  # 350000 / 125
        'LTV': 10000.0,  # 1250000 / 125
        'ROI': 257.14,  # ((1250000 - 350000) / 350000) * 100
        'Win_Rate': 22.35,  # (95 / 425) * 100
        'Ticket_Medio': 13157.89,  # 1250000 / 95
    }


@pytest.fixture
def crew_inputs(data_dir):
    """Inputs padrão para execução do crew"""
    return {
        'cliente': 'Empresa Teste',
        'periodo': '2025',
        'dados_csv_path': str(data_dir / 'dados_entrada.csv'),
        'metricas_csv_path': str(data_dir / 'metricas_calculadas.csv'),
        'output_path': 'outputs/',
        'gerar_excel': True,
        'gerar_dashboard': True
    }


@pytest.fixture(autouse=True)
def skip_if_no_api_key():
    """Pula testes que precisam de API key se ela não estiver configurada"""
    if not os.getenv('OPENAI_API_KEY'):
        pytest.skip("OPENAI_API_KEY não configurada - pulando teste que requer API")


@pytest.fixture
def mock_openai_response():
    """Mock de resposta da OpenAI para testes sem consumir API"""
    return {
        "choices": [{
            "message": {
                "content": "Análise de teste concluída com sucesso."
            }
        }],
        "usage": {
            "total_tokens": 100
        }
    }


def pytest_configure(config):
    """Configuração inicial do pytest"""
    config.addinivalue_line(
        "markers", "slow: marca testes lentos (desabilite com '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marca testes de integração"
    )
    config.addinivalue_line(
        "markers", "unit: marca testes unitários"
    )
    config.addinivalue_line(
        "markers", "requires_api: marca testes que precisam de API key"
    )
