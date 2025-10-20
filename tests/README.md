# Testes - Diagnóstico Comercial Voga.IA

Esta pasta contém todos os testes automatizados do projeto.

## Estrutura de Testes

```
tests/
├── unit/              # Testes unitários de componentes individuais
├── integration/       # Testes de integração do fluxo completo
├── conftest.py        # Configurações e fixtures do pytest
└── README.md          # Este arquivo
```

## Como Executar os Testes

### Todos os testes

```bash
# Ativar ambiente virtual
source venv-python312/bin/activate

# Executar todos os testes
pytest tests/

# Com output detalhado
pytest tests/ -v

# Com cobertura de código
pytest tests/ --cov=src/diagnostico_comercial_voga_ia
```

### Testes específicos

```bash
# Apenas testes unitários
pytest tests/unit/

# Apenas testes de integração
pytest tests/integration/

# Teste específico
pytest tests/unit/test_tools.py

# Teste específico de uma função
pytest tests/unit/test_tools.py::test_calcular_cac
```

### Filtrar por marcadores

```bash
# Pular testes lentos
pytest tests/ -m "not slow"

# Apenas testes que não precisam de API
pytest tests/ -m "not requires_api"

# Apenas testes unitários (marcador)
pytest tests/ -m unit

# Apenas testes de integração (marcador)
pytest tests/ -m integration
```

## Tipos de Testes

### Unit Tests (`tests/unit/`)

Testes de componentes individuais e funções isoladas:

| Arquivo | Descrição |
|---------|-----------|
| `test_tools.py` | Testa ferramentas de cálculo de métricas (CAC, LTV, ROI, etc.) |
| `test_imports.py` | Valida imports do CrewAI e dependências |
| `test_simple_tools.py` | Testes simples sem dependências externas |

**Características:**
- Rápidos (< 1 segundo por teste)
- Sem dependências externas
- Sem chamadas de API
- Executam em isolamento

### Integration Tests (`tests/integration/`)

Testes do fluxo completo dos agentes:

| Arquivo | Descrição |
|---------|-----------|
| `test_execution.py` | Testa execução do fluxo completo de agentes |
| `test_corrections.py` | Testa correções e melhorias implementadas |

**Características:**
- Mais lentos (vários minutos)
- Podem fazer chamadas de API
- Testam integração entre componentes
- Marcados com `@pytest.mark.slow`

## Configuração (conftest.py)

O arquivo `conftest.py` fornece fixtures compartilhadas:

### Fixtures de Diretórios

```python
def test_exemplo(project_root, data_dir, output_dir):
    # project_root: /path/to/VogaIA_Diagnostico_Comercial
    # data_dir: .../src/diagnostico_comercial_voga_ia/data
    # output_dir: .../src/diagnostico_comercial_voga_ia/outputs
```

### Fixtures de Dados

```python
def test_metricas(sample_input_data, expected_metrics):
    # sample_input_data: dict com dados de entrada
    # expected_metrics: dict com métricas esperadas
```

### Fixtures de Configuração

```python
def test_crew(crew_inputs):
    # crew_inputs: dict com parâmetros para inicializar o crew
```

## Escrevendo Novos Testes

### Exemplo de Teste Unitário

```python
# tests/unit/test_new_feature.py
import pytest
from diagnostico_comercial_voga_ia.tools.diagnostico_tools import MinhaNovaFerramenta

@pytest.mark.unit
def test_minha_nova_ferramenta(sample_input_data):
    """Testa se MinhaNovaFerramenta calcula corretamente"""
    tool = MinhaNovaFerramenta()
    resultado = tool._run(
        parametro1=sample_input_data['Receita_Total'],
        parametro2=sample_input_data['Custo_Vendas_Marketing']
    )

    assert resultado > 0
    assert isinstance(resultado, (int, float))
```

### Exemplo de Teste de Integração

```python
# tests/integration/test_new_flow.py
import pytest

@pytest.mark.integration
@pytest.mark.slow
@pytest.mark.requires_api
def test_novo_fluxo_completo(crew_inputs):
    """Testa fluxo completo com novo agente"""
    from diagnostico_comercial_voga_ia.crew import DiagnosticoComercialVogaIaCrew

    crew = DiagnosticoComercialVogaIaCrew()
    resultado = crew.crew().kickoff(inputs=crew_inputs)

    assert resultado is not None
    # Validar saídas esperadas
```

## Marcadores Disponíveis

Marcadores configurados em `conftest.py`:

| Marcador | Uso | Comando para pular |
|----------|-----|-------------------|
| `@pytest.mark.unit` | Testes unitários | - |
| `@pytest.mark.integration` | Testes de integração | `pytest -m "not integration"` |
| `@pytest.mark.slow` | Testes lentos (>30s) | `pytest -m "not slow"` |
| `@pytest.mark.requires_api` | Precisa de API key | Automático se sem API key |

## Boas Práticas

### ✅ FAÇA:

- Use fixtures do `conftest.py` para dados de teste
- Marque testes lentos com `@pytest.mark.slow`
- Marque testes que precisam de API com `@pytest.mark.requires_api`
- Escreva docstrings descrevendo o que o teste valida
- Use `assert` com mensagens claras
- Organize testes por funcionalidade
- Execute testes antes de commitar

### ❌ NÃO FAÇA:

- Hardcode paths absolutos (use fixtures `project_root`, `data_dir`)
- Commite testes que dependem de dados locais específicos
- Escreva testes que modificam arquivos de produção
- Use `sleep()` em testes (use mocks)
- Ignore warnings e erros nos testes

## Cobertura de Código

Para verificar a cobertura de código:

```bash
# Instalar pytest-cov (se ainda não instalado)
pip install pytest-cov

# Executar com cobertura
pytest tests/ --cov=src/diagnostico_comercial_voga_ia --cov-report=html

# Ver relatório HTML
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
```

**Meta de cobertura:** > 80% para código crítico (ferramentas de cálculo)

## CI/CD

Os testes são (ou deverão ser) executados automaticamente em:

- **Pull Requests:** Todos os testes unitários
- **Merge para main:** Todos os testes (incluindo integração)
- **Release:** Suite completa + testes de performance

## Troubleshooting

### Erro: "OPENAI_API_KEY não configurada"

```bash
# Criar arquivo .env com sua chave
echo "OPENAI_API_KEY=sk-sua-chave-aqui" > .env

# Ou pular testes que precisam de API
pytest -m "not requires_api"
```

### Erro: "ModuleNotFoundError"

```bash
# Verificar se está no ambiente virtual
source venv-python312/bin/activate

# Instalar dependências
poetry install
# ou
pip install -e .
```

### Testes muito lentos

```bash
# Executar apenas testes rápidos
pytest tests/ -m "not slow"

# Executar em paralelo (requer pytest-xdist)
pip install pytest-xdist
pytest tests/ -n auto
```

## Recursos Adicionais

- [Documentação do pytest](https://docs.pytest.org/)
- [pytest fixtures](https://docs.pytest.org/en/stable/fixture.html)
- [pytest markers](https://docs.pytest.org/en/stable/mark.html)
- [pytest-cov](https://pytest-cov.readthedocs.io/)

---

**Última atualização:** 2025-10-20
**Mantenha os testes atualizados conforme o código evolui!**
