# 🚀 Voga.IA - Plataforma de Diagnóstico Comercial Inteligente

## 📋 Visão Geral

A **Voga.IA** é uma plataforma completa de diagnóstico comercial que combina **8 agentes especializados em IA** com uma **interface web moderna** para análise de métricas comerciais em tempo real.

### ✨ Características Principais

- 🤖 **8 Agentes Especializados** em IA para análise completa
- 📊 **40+ Métricas Comerciais** calculadas automaticamente
- 🌐 **Interface Web Moderna** com dashboards interativos
- 🔐 **Sistema de Login** com diferentes níveis de acesso
- 📈 **Gráficos Interativos** com Plotly
- 📄 **Relatórios Automáticos** em Markdown
- 🔄 **Atualização em Tempo Real** dos dados

## 🏗️ Arquitetura do Sistema

```
Voga.IA/
├── 🔬 Diagnóstico Comercial (CrewAI)
│   ├── 8 Agentes Especializados
│   ├── 40+ Métricas Calculadas
│   └── Relatórios Automáticos
├── 🌐 Plataforma Web (Flask)
│   ├── Sistema de Login
│   ├── Dashboards Interativos
│   └── Visualização de Dados
└── 📊 Dados e Relatórios
    ├── Métricas Calculadas (CSV)
    └── Relatórios Gerados (Markdown)
```

## 🚀 Como Usar

### 1. **Inicialização Rápida**

```bash
# Ativar ambiente virtual
source venv-python312/bin/activate

# Executar plataforma completa
python3 start_platform.py
```

### 2. **Acesso à Plataforma**

- **URL:** http://localhost:5000
- **Admin:** admin@vogaia.com / admin123
- **Usuário:** user@vogaia.com / user123

### 3. **Funcionalidades Disponíveis**

#### 📊 Dashboard Principal
- Visão geral das métricas
- Gráficos interativos
- Cards de status
- Atualização automática

#### 📈 Métricas Detalhadas
- Tabela completa de 40+ métricas
- Filtros por categoria
- Comparação com benchmarks

#### 📄 Relatórios
- Visualização de relatórios gerados
- Formato Markdown formatado
- Download disponível

#### 🔬 Execução de Diagnóstico
- Botão para executar diagnóstico completo
- 8 agentes especializados
- Relatórios automáticos

## 🤖 Agentes Especializados

### 1. **Data Collector Agent**
- Coleta e validação de dados
- Verificação de completude
- Padronização de informações

### 2. **Data Governance Agent**
- Governança e limpeza de dados
- Detecção de outliers
- Aplicação de regras de negócio

### 3. **Metrics Calculator Agent**
- Cálculo de 40+ métricas
- Fórmulas financeiras precisas
- Categorização automática

### 4. **Business Analyst Agent**
- Análise estratégica
- Identificação de gargalos
- Comparação com benchmarks

### 5. **Alert Monitor Agent**
- Monitoramento de métricas
- Configuração de alertas
- Detecção de desvios

### 6. **Visualization Agent**
- Criação de visualizações
- Gráficos e tabelas
- Relatórios visuais

### 7. **Dashboard Creator Agent**
- Especificações de dashboards
- Protótipos interativos
- Recomendações técnicas

### 8. **Report Generator Agent**
- Relatórios executivos
- Consolidação de análises
- Recomendações estratégicas

## 📊 Métricas Calculadas

### 💰 Métricas Financeiras (8)
- CAC (Custo de Aquisição de Cliente)
- LTV (Lifetime Value)
- ROI (Return on Investment)
- ROS (Return on Sales)
- Ticket Médio
- Magic Number
- Payback Period
- Meta Achievement

### 📈 Métricas de Performance (5)
- Win Rate
- Pipeline Velocity
- Produtividade por Rep
- Custo por Lead
- Eficiência Operacional

### 🎯 Métricas de Funil (6)
- Lead → MQL
- MQL → SQL
- SQL → Reunião
- Reunião → Proposta
- Proposta → Fechamento
- Lead → Fechamento

### 👥 Métricas de Produtividade (7)
- Leads por Rep
- MQL por Rep
- SQL por Rep
- Reuniões por Rep
- Propostas por Rep
- Fechamentos por Rep
- Receita por Rep

### 📈 Métricas de Crescimento (4)
- Growth Rate
- Net New Clients
- Churn Rate
- Client Acquisition Rate

### ⚡ Métricas de Eficiência (4)
- Investimento em Ferramentas
- Investimento em Treinamento
- Eficiência SQL
- Total Investment per Client

### 🎯 Métricas Contextuais SPICED (2)
- Idade da Empresa
- Urgência SPICED

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.12** - Linguagem principal
- **CrewAI 0.126.0** - Framework de agentes IA
- **Flask** - Framework web
- **Pandas** - Manipulação de dados
- **Plotly** - Gráficos interativos

### Frontend
- **Bootstrap 5** - Framework CSS
- **Font Awesome** - Ícones
- **Plotly.js** - Gráficos interativos
- **HTML5/CSS3/JavaScript** - Interface

### Dados
- **CSV** - Armazenamento de métricas
- **Markdown** - Relatórios
- **YAML** - Configurações

## 📁 Estrutura de Arquivos

```
diagnostico_comercial_voga_ia/
├── 📄 web_app.py              # Aplicação web Flask
├── 📄 start_platform.py       # Script de inicialização
├── 📄 test_agents.py          # Testes dos agentes
├── 📁 templates/              # Templates HTML
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── dashboard.html
│   ├── metrics.html
│   ├── reports.html
│   └── view_report.html
├── 📁 src/                    # Código fonte do diagnóstico
│   └── diagnostico_comercial_voga_ia/
│       ├── crew.py            # Configuração dos agentes
│       ├── main.py            # Execução principal
│       ├── tools/             # Ferramentas dos agentes
│       ├── config/            # Configurações
│       ├── data/              # Dados e métricas
│       └── outputs/           # Relatórios gerados
└── 📁 venv-python312/         # Ambiente virtual
```

## 🔧 Configuração e Instalação

### Pré-requisitos
- Python 3.12+
- Ambiente virtual ativo
- Dependências instaladas

### Instalação
```bash
# 1. Clonar repositório
git clone <repository-url>
cd diagnostico_comercial_voga_ia

# 2. Criar ambiente virtual
python3.12 -m venv venv-python312

# 3. Ativar ambiente
source venv-python312/bin/activate

# 4. Instalar dependências
pip install -e .

# 5. Instalar dependências web
pip install flask flask-login plotly

# 6. Configurar variáveis de ambiente
cp .env.example .env
# Editar .env com suas configurações
```

### Variáveis de Ambiente
```bash
# .env
OPENAI_API_KEY=sua_chave_api_aqui
OPENAI_MODEL_NAME=gpt-4o-mini
SECRET_KEY=voga-ia-secret-key-2025
```

## 🚀 Execução

### Opção 1: Script de Inicialização (Recomendado)
```bash
python3 start_platform.py
```

### Opção 2: Execução Manual
```bash
# 1. Executar diagnóstico
python3 src/diagnostico_comercial_voga_ia/main.py

# 2. Iniciar aplicação web
python3 web_app.py
```

### Opção 3: Apenas Diagnóstico
```bash
python3 src/diagnostico_comercial_voga_ia/main.py
```

## 📊 Dashboards Disponíveis

### 1. **Dashboard Principal**
- Visão geral das métricas
- Cards de status coloridos
- Gráficos interativos
- Tabela de métricas principais

### 2. **Métricas Detalhadas**
- Tabela completa de todas as métricas
- Filtros por categoria
- Comparação com benchmarks
- Status visual

### 3. **Relatórios**
- Lista de relatórios gerados
- Visualização em Markdown
- Download de arquivos
- Navegação entre relatórios

## 🔍 Troubleshooting

### Problemas Comuns

#### 1. **Erro de Importação**
```bash
# Verificar ambiente virtual
source venv-python312/bin/activate

# Verificar dependências
pip list | grep crewai
```

#### 2. **Porta 5000 em Uso**
```bash
# Verificar processos
lsof -i :5000

# Matar processo se necessário
kill -9 <PID>
```

#### 3. **Erro de API Key**
```bash
# Verificar arquivo .env
cat .env

# Configurar API key
echo "OPENAI_API_KEY=sua_chave_aqui" >> .env
```

#### 4. **Dados Não Atualizados**
```bash
# Executar diagnóstico manualmente
python3 src/diagnostico_comercial_voga_ia/main.py

# Verificar arquivos de dados
ls -la src/diagnostico_comercial_voga_ia/data/
```

## 📈 Próximos Passos

### Melhorias Planejadas
- [ ] Banco de dados PostgreSQL
- [ ] Autenticação OAuth
- [ ] API REST completa
- [ ] Notificações em tempo real
- [ ] Exportação para Excel/PDF
- [ ] Múltiplos usuários/empresas
- [ ] Histórico de execuções
- [ ] Alertas por email
- [ ] Integração com CRMs

### Funcionalidades Avançadas
- [ ] Machine Learning para predições
- [ ] Análise de tendências
- [ ] Comparação entre períodos
- [ ] Análise de concorrência
- [ ] Otimização automática
- [ ] Recomendações personalizadas

## 🤝 Contribuição

Para contribuir com o projeto:

1. Fork o repositório
2. Crie uma branch para sua feature
3. Faça commit das mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 📞 Suporte

Para suporte e dúvidas:
- 📧 Email: suporte@vogaia.com
- 📱 WhatsApp: (11) 99999-9999
- 🌐 Website: https://vogaia.com

---

**Voga.IA** - Transformando dados em insights acionáveis! 🚀 