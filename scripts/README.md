# Scripts - Diagnóstico Comercial Voga.IA

Esta pasta contém scripts auxiliares e versões antigas de execução do sistema.

## Estrutura

```
scripts/
├── legacy/           # Scripts antigos mantidos para referência
│   ├── executar_diagnostico_completo.py
│   ├── executar_diagnostico_corrigido.py
│   ├── executar_diagnostico_melhorado.py
│   ├── executar_diagnostico_robusto.py
│   ├── executar_simples.py
│   ├── executar_validacao.py
│   └── reexecutar_agente_8.py
└── README.md         # Este arquivo
```

## Scripts Recomendados (na raiz do projeto)

Para usar o sistema, utilize os scripts principais na raiz do projeto:

### 🚀 start_platform.py (RECOMENDADO)

Executa diagnóstico completo + web app em uma única execução:

```bash
python3 start_platform.py
```

**Faz:**
1. Executa os 8 agentes do diagnóstico
2. Gera relatórios em `outputs/`
3. Calcula métricas e salva em `data/metricas_calculadas.csv`
4. Inicia aplicação web em http://localhost:5000

### 🌐 web_app.py

Apenas a aplicação web (se já tiver executado o diagnóstico):

```bash
python3 web_app.py
```

**Acesso:**
- URL: http://localhost:5000
- Login: `admin@vogaia.com` / `admin123`
- Ou: `user@vogaia.com` / `user123`

### 📊 src/diagnostico_comercial_voga_ia/main.py

Apenas o diagnóstico (sem web app):

```bash
cd src/diagnostico_comercial_voga_ia
python3 main.py
```

## Scripts Legacy (não recomendados)

Os scripts na pasta `legacy/` são versões antigas mantidas apenas para referência histórica.

### ⚠️ NÃO RECOMENDADO - Use apenas se necessário

| Script | Descrição | Status |
|--------|-----------|--------|
| `executar_diagnostico_completo.py` | Versão completa antiga | Substituído por `start_platform.py` |
| `executar_diagnostico_corrigido.py` | Versão com correções antigas | Substituído por `start_platform.py` |
| `executar_diagnostico_melhorado.py` | Versão melhorada antiga | Substituído por `start_platform.py` |
| `executar_diagnostico_robusto.py` | Versão robusta antiga | Substituído por `start_platform.py` |
| `executar_simples.py` | Versão simplificada | Use `main.py` |
| `executar_validacao.py` | Validação antiga | Use testes em `tests/` |
| `reexecutar_agente_8.py` | Re-execução do agente 8 | Funcionalidade removida |

### Por que foram movidos?

1. **Redundância:** Múltiplos scripts fazendo a mesma coisa
2. **Manutenção:** Difícil manter várias versões sincronizadas
3. **Confusão:** Usuários não sabiam qual script usar
4. **Organização:** Poluíam o diretório raiz do projeto

### Posso deletar os scripts legacy?

**Sim**, se você:
- Confirmou que `start_platform.py` atende suas necessidades
- Não tem customizações específicas nos scripts antigos
- Fez backup do repositório

**Não**, se você:
- Ainda não testou o `start_platform.py`
- Tem scripts customizados baseados nos antigos
- Quer manter histórico de evolução do projeto

## Executando Scripts Legacy (se necessário)

Se precisar executar algum script legacy:

```bash
# Da raiz do projeto
python3 scripts/legacy/nome_do_script.py
```

**Nota:** Alguns scripts podem ter paths hardcoded que precisam ser ajustados.

## Migração Recomendada

Se você estava usando algum script legacy:

| Antes | Agora |
|-------|-------|
| `python3 executar_diagnostico_completo.py` | `python3 start_platform.py` |
| `python3 executar_diagnostico_corrigido.py` | `python3 start_platform.py` |
| `python3 executar_simples.py` | `python3 src/diagnostico_comercial_voga_ia/main.py` |
| `python3 executar_validacao.py` | `pytest tests/` |

## Adicionando Novos Scripts

Se precisar criar scripts auxiliares, siga estas diretrizes:

### Estrutura Recomendada

```python
#!/usr/bin/env python3
"""
Descrição clara do que o script faz
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Adicionar src ao path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

# Carregar variáveis de ambiente
load_dotenv()

def main():
    """Função principal"""
    # Seu código aqui
    pass

if __name__ == "__main__":
    main()
```

### Boas Práticas

✅ **FAÇA:**
- Use paths relativos ao projeto
- Documente o propósito do script
- Use variáveis de ambiente para configurações
- Adicione tratamento de erros
- Use logging ao invés de prints
- Siga PEP 8

❌ **NÃO FAÇA:**
- Hardcode paths absolutos
- Commite credenciais
- Duplique funcionalidades existentes
- Modifique arquivos de produção sem backup

## Limpeza de Scripts Legacy

Para remover os scripts legacy quando estiver pronto:

```bash
# Backup (opcional)
git tag backup-legacy-scripts

# Remover pasta legacy
git rm -r scripts/legacy/

# Commit
git commit -m "Remove legacy scripts - migrated to start_platform.py"
```

## Suporte

Se você tem dúvidas sobre qual script usar:

1. **Para uso normal:** Use `start_platform.py`
2. **Para testes:** Use `pytest tests/`
3. **Para desenvolvimento:** Use `src/diagnostico_comercial_voga_ia/main.py`
4. **Para dúvidas:** Consulte o `README.md` principal

---

**Última atualização:** 2025-10-20
**Recomendação:** Use os scripts principais na raiz do projeto.
