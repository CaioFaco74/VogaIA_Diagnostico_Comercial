# Guia de Segurança - Voga.IA Diagnóstico Comercial

## Configuração Segura de API Keys

### 1. NUNCA Commite Credenciais no Git

**IMPORTANTE:** Chaves de API, senhas e tokens NUNCA devem ser commitados no Git, nem mesmo em arquivos de exemplo.

### 2. Como Configurar sua OpenAI API Key

#### Passo 1: Obter sua API Key

1. Acesse [OpenAI Platform](https://platform.openai.com/api-keys)
2. Faça login na sua conta OpenAI
3. Navegue até "API Keys"
4. Clique em "Create new secret key"
5. Copie a chave gerada (você só verá ela uma vez!)

#### Passo 2: Criar arquivo .env local

```bash
# Na raiz do projeto, crie o arquivo .env
cp .env.example .env
```

#### Passo 3: Adicionar sua chave no arquivo .env

Edite o arquivo `.env` e substitua o placeholder pela sua chave real:

```bash
# Antes (arquivo .env.example)
OPENAI_API_KEY=sk-sua-chave-aqui-substitua-por-chave-real

# Depois (arquivo .env - NUNCA commitar este arquivo!)
OPENAI_API_KEY=sk-proj-abc123xyz789...sua-chave-real-aqui
```

#### Passo 4: Verificar se .env está no .gitignore

O arquivo `.env` deve estar listado no `.gitignore` para evitar commits acidentais:

```bash
# Verificar se .env está sendo ignorado pelo Git
git check-ignore .env
# Deve retornar: .env
```

### 3. Modelos OpenAI Disponíveis

Configure o modelo no arquivo `.env`:

```bash
# Modelo padrão (recomendado - mais econômico)
OPENAI_MODEL_NAME=gpt-4o-mini

# Outros modelos disponíveis:
# OPENAI_MODEL_NAME=gpt-4o
# OPENAI_MODEL_NAME=gpt-4-turbo
# OPENAI_MODEL_NAME=gpt-3.5-turbo
```

### 4. Custo Estimado de Uso

Para cada execução completa do diagnóstico (8 agentes):

| Modelo | Custo Estimado | Tempo |
|--------|----------------|-------|
| gpt-4o-mini | ~$0.10 - $0.50 | 5-10 min |
| gpt-4o | ~$2.00 - $5.00 | 5-10 min |
| gpt-4-turbo | ~$3.00 - $8.00 | 5-10 min |

### 5. Boas Práticas de Segurança

#### ✅ FAÇA:

- Use variáveis de ambiente (`.env`) para credenciais
- Mantenha `.env` no `.gitignore`
- Use chaves diferentes para desenvolvimento e produção
- Rotacione suas chaves periodicamente (a cada 90 dias)
- Configure limites de uso na OpenAI Platform
- Monitore o uso de API no dashboard da OpenAI

#### ❌ NÃO FAÇA:

- Commitar arquivos `.env` no Git
- Colocar chaves reais em `.env.example`
- Compartilhar chaves por email ou chat
- Usar a mesma chave em múltiplos projetos
- Deixar chaves hardcoded no código
- Compartilhar screenshots com chaves visíveis

### 6. Configuração para Ambientes Diferentes

#### Desenvolvimento Local

```bash
# .env.development
OPENAI_API_KEY=sk-proj-dev-123...
OPENAI_MODEL_NAME=gpt-4o-mini
DEBUG_MODE=true
```

#### Produção

```bash
# .env.production
OPENAI_API_KEY=sk-proj-prod-456...
OPENAI_MODEL_NAME=gpt-4o
DEBUG_MODE=false
ENABLE_ALERTS=true
```

### 7. Verificação de Segurança

Execute este checklist antes de commitar:

```bash
# 1. Verificar se há chaves expostas
grep -r "sk-proj-" . --exclude-dir=venv* --exclude-dir=.git

# 2. Verificar se .env está sendo ignorado
git status | grep .env
# Não deve aparecer nada

# 3. Verificar arquivos que serão commitados
git diff --cached

# 4. Verificar histórico Git
git log -p | grep -i "api.key\|openai\|sk-"
```

### 8. O que fazer se expor uma chave acidentalmente

Se você commitou uma chave de API no Git:

1. **Revogar imediatamente:**
   - Acesse [OpenAI API Keys](https://platform.openai.com/api-keys)
   - Encontre a chave exposta
   - Clique em "Delete" ou "Revoke"

2. **Criar nova chave:**
   - Gere uma nova chave na plataforma
   - Atualize seu arquivo `.env` local

3. **Limpar histórico Git:**
   ```bash
   # CUIDADO: Isso reescreve o histórico Git
   # Use apenas se absolutamente necessário
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch .env" \
     --prune-empty --tag-name-filter cat -- --all

   # Force push (se já enviou para remoto)
   git push origin --force --all
   ```

4. **Usar BFG Repo-Cleaner (alternativa mais rápida):**
   ```bash
   # Instalar BFG
   brew install bfg  # macOS

   # Remover chaves do histórico
   bfg --replace-text sensitive-data.txt
   ```

### 9. Ferramentas de Segurança Recomendadas

#### Git Secrets

Previne commits com credenciais:

```bash
# Instalar git-secrets
brew install git-secrets  # macOS
apt-get install git-secrets  # Linux

# Configurar no repositório
cd /path/to/projeto
git secrets --install
git secrets --register-aws
git secrets --add 'sk-[a-zA-Z0-9]{20,}'
```

#### Pre-commit Hooks

Adicionar ao `.git/hooks/pre-commit`:

```bash
#!/bin/bash
if git diff --cached | grep -E "sk-[a-zA-Z0-9]{20,}"; then
    echo "❌ ERRO: Possível API key detectada!"
    echo "🔍 Revise suas alterações antes de commitar"
    exit 1
fi
```

### 10. Alternativas para Gerenciamento de Credenciais

#### Opção 1: Variáveis de Ambiente do Sistema

```bash
# Adicionar ao ~/.bashrc ou ~/.zshrc
export OPENAI_API_KEY="sk-proj-..."

# Usar no projeto (sem .env)
python3 web_app.py
```

#### Opção 2: Gerenciadores de Senha

- **1Password**: Armazene e sincronize credenciais
- **AWS Secrets Manager**: Para produção em AWS
- **HashiCorp Vault**: Para empresas
- **Azure Key Vault**: Para produção em Azure

#### Opção 3: Docker Secrets

```yaml
# docker-compose.yml
services:
  web:
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    env_file:
      - .env
```

### 11. Checklist de Configuração Inicial

- [ ] Copiar `.env.example` para `.env`
- [ ] Adicionar sua OpenAI API Key em `.env`
- [ ] Verificar que `.env` está no `.gitignore`
- [ ] Testar a aplicação com `python3 start_platform.py`
- [ ] Configurar limites de uso na OpenAI Platform
- [ ] Ativar alertas de cobrança na OpenAI
- [ ] Documentar onde a chave está armazenada (cofre de senhas)

### 12. Contato e Suporte

Se você acidentalmente expôs credenciais:

1. Revoque imediatamente a chave
2. Notifique o time de segurança (se aplicável)
3. Gere nova chave
4. Documente o incidente

### 13. Recursos Adicionais

- [OpenAI API Best Practices](https://platform.openai.com/docs/guides/safety-best-practices)
- [Git Secrets Documentation](https://github.com/awslabs/git-secrets)
- [OWASP Credential Management](https://cheatsheetseries.owasp.org/cheatsheets/Credential_Storage_Cheat_Sheet.html)

---

**Última atualização:** 2025-10-20
**Mantenha este documento atualizado com as melhores práticas de segurança.**
