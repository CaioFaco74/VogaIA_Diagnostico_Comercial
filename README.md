# 🎯 Diagnóstico Comercial Voga.IA

Sistema inteligente de diagnóstico comercial que utiliza múltiplos agentes de IA para analisar métricas comerciais, gerar relatórios detalhados e criar dashboards interativos.

## 🚀 Funcionalidades

- **Análise Inteligente**: Múltiplos agentes de IA especializados
- **Métricas Comerciais**: Cálculo automático de KPIs importantes
- **Relatórios Detalhados**: Geração de relatórios em Markdown
- **Dashboard Web**: Interface web interativa com gráficos
- **Sistema de Login**: Autenticação segura de usuários
- **Visualizações**: Gráficos interativos com Plotly

## 📋 Pré-requisitos

- Python 3.12 (recomendado)
- macOS, Linux ou Windows
- 4GB RAM mínimo
- Conexão com internet para APIs de IA

## 🛠️ Instalação

1. **Clone o repositório**:
```bash
git clone <url-do-repositorio>
cd diagnostico_comercial_voga_ia
```

2. **Crie o ambiente virtual**:
```bash
python3 -m venv venv-python312
```

3. **Ative o ambiente virtual**:
```bash
# macOS/Linux
source venv-python312/bin/activate

# Windows
venv-python312\Scripts\activate
```

4. **Instale as dependências**:
```bash
pip install -e .
```

## 🎯 Como Usar

### 1. Configurar API Key

Antes de começar, configure sua API key da OpenAI:

```bash
# Copiar arquivo de exemplo
cp .env.example .env

# Editar .env e adicionar sua chave real
# OPENAI_API_KEY=sk-sua-chave-aqui
```

📖 **Consulte o arquivo [SECURITY.md](SECURITY.md) para instruções detalhadas de segurança**

### 2. Executar Plataforma Completa (Recomendado)

```bash
# Ativar ambiente virtual
source venv-python312/bin/activate

# Executar diagnóstico + web app
python3 start_platform.py
```

Isso irá:
1. Executar os 8 agentes de IA
2. Gerar relatórios completos
3. Calcular todas as métricas
4. Iniciar a aplicação web

### 3. Usar a Plataforma Web

#### Opção A: Script de Gerenciamento (Recomendado)
```bash
# Verificar status
./manage_web_app.sh status

# Iniciar aplicação
./manage_web_app.sh start

# Parar aplicação
./manage_web_app.sh stop

# Reiniciar aplicação
./manage_web_app.sh restart

# Ver logs
./manage_web_app.sh logs

# Ver ajuda
./manage_web_app.sh help
```

#### Opção B: Execução Manual
```bash
# Ativar ambiente virtual
source venv-python312/bin/activate

# Iniciar aplicação
python web_app.py
```

### 3. Acessar a Plataforma

- **URL**: http://localhost:8080
- **Login**: admin@vogaia.com / admin123
- **Usuário**: user@vogaia.com / user123

## 📊 Estrutura do Projeto

```
VogaIA_Diagnostico_Comercial/
├── src/
│   └── diagnostico_comercial_voga_ia/
│       ├── config/           # Configurações dos agentes (YAML)
│       ├── data/             # Dados de entrada e métricas calculadas
│       ├── outputs/          # Relatórios gerados pelos agentes
│       ├── tools/            # Ferramentas de cálculo de métricas
│       ├── crew.py           # Definição dos 8 agentes CrewAI
│       └── main.py           # Execução principal do diagnóstico
├── tests/                    # 🆕 Testes automatizados
│   ├── unit/                 # Testes unitários de componentes
│   ├── integration/          # Testes de integração do fluxo
│   ├── conftest.py           # Configurações do pytest
│   └── README.md             # Documentação de testes
├── scripts/                  # 🆕 Scripts auxiliares
│   ├── legacy/               # Scripts antigos (referência)
│   └── README.md             # Documentação de scripts
├── templates/                # Templates HTML (Jinja2)
├── static/                   # CSS, JS e assets web
├── start_platform.py         # 🚀 Script principal (diagnóstico + web)
├── web_app.py               # Aplicação web Flask
├── SECURITY.md              # 🆕 Guia de segurança (API keys)
├── .env.example             # Template de variáveis de ambiente
├── .gitignore               # Arquivos ignorados pelo Git
└── README.md                # Este arquivo
```

### 📁 Descrição dos Diretórios Principais

- **src/**: Código-fonte do sistema de diagnóstico
- **tests/**: Testes automatizados (pytest) - [Ver documentação](tests/README.md)
- **scripts/**: Scripts auxiliares e versões legacy - [Ver documentação](scripts/README.md)
- **templates/**: Interface web (HTML + Jinja2)
- **static/**: Recursos estáticos (CSS, JavaScript, imagens)

## 🔧 Configuração

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sua_chave_api_aqui
SECRET_KEY=sua_chave_secreta_aqui
```

### Dados de Entrada

Coloque seus dados comerciais em `src/diagnostico_comercial_voga_ia/data/dados_entrada.csv`

## 📈 Métricas Calculadas

- **Financeiras**: Receita, Margem, ROI
- **Funil de Vendas**: Conversões, Taxa de fechamento
- **Performance**: Produtividade, Eficiência
- **Cliente**: Satisfação, Retenção, LTV

## 🧪 Testes

O projeto agora inclui testes automatizados organizados:

```bash
# Executar todos os testes
pytest tests/

# Apenas testes unitários
pytest tests/unit/

# Apenas testes de integração
pytest tests/integration/

# Com cobertura de código
pytest tests/ --cov=src/diagnostico_comercial_voga_ia
```

📖 **Ver documentação completa em [tests/README.md](tests/README.md)**

### Estrutura de Testes

- **tests/unit/**: Testes unitários de ferramentas e funções
- **tests/integration/**: Testes do fluxo completo dos agentes
- **tests/conftest.py**: Configurações e fixtures compartilhadas

## 🎨 Interface Web

### Dashboard Principal
- Visão geral das métricas
- Gráficos interativos
- Status em tempo real

### Páginas Disponíveis
- **Dashboard**: Visão geral
- **Métricas**: Detalhamento das métricas
- **Relatórios**: Visualização dos relatórios
- **Executar**: Rodar novo diagnóstico

## 🚨 Solução de Problemas

### Problema: Porta 8080 em uso
```bash
# Verificar o que está usando a porta
lsof -i :8080

# Parar processo específico
./manage_web_app.sh stop
```

### Problema: Ambiente virtual não encontrado
```bash
# Recriar ambiente virtual
python3 -m venv venv-python312
source venv-python312/bin/activate
pip install -e .
```

### Problema: Múltiplas instâncias rodando
```bash
# Parar todas as instâncias
./manage_web_app.sh stop

# Verificar status
./manage_web_app.sh status
```

### Problema: Reloads infinitos (modo debug)
- A aplicação foi configurada para rodar sem modo debug
- Use o script de gerenciamento para evitar problemas

## 📝 Logs

- **Aplicação Web**: `/tmp/voga_ia_web.log`
- **Diagnóstico**: Console de saída
- **Ver logs**: `./manage_web_app.sh logs`

## 🔒 Segurança

- Sistema de login implementado
- Senhas criptografadas
- Sessões seguras
- Proteção contra CSRF

## 📞 Suporte

Para problemas ou dúvidas:
1. Verifique os logs: `./manage_web_app.sh logs`
2. Consulte a seção de solução de problemas
3. Verifique se todas as dependências estão instaladas

## 🎯 Próximos Passos

- [ ] Integração com mais fontes de dados
- [ ] Relatórios em PDF
- [ ] API REST completa
- [ ] Notificações em tempo real
- [ ] Backup automático de dados

---

**Desenvolvido com ❤️ pela equipe Voga.IA**
