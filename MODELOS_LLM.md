# 🎯 CONFIGURAÇÃO DE MODELOS LLM

## Como mudar o modelo OpenAI:

### 1. No arquivo .env:
```
OPENAI_MODEL_NAME=gpt-4o-mini    # Mais barato para testes
# OPENAI_MODEL_NAME=gpt-4o       # Mais inteligente, mais caro
# OPENAI_MODEL_NAME=gpt-4        # Modelo clássico
```

### 2. Modelos disponíveis e custos (aproximados):

| Modelo | Input/1K tokens | Output/1K tokens | Uso recomendado |
|--------|----------------|------------------|-----------------|
| **gpt-4o-mini** | $0.000150 | $0.000600 | ✅ **TESTES** - Mais barato |
| **gpt-4o** | $0.005000 | $0.015000 | 🚀 **PRODUÇÃO** - Mais inteligente |
| **gpt-4** | $0.030000 | $0.060000 | 📈 **PREMIUM** - Máxima qualidade |

### 3. Configuração atual:
- ✅ Configurado para usar: **gpt-4o-mini**
- ✅ Temperature: **0.3** (consistência nas respostas)
- ✅ Todos os 8 agentes usarão o mesmo modelo
- ✅ Carregado via variável de ambiente

### 4. Para mudar:
1. Edite o arquivo `.env`
2. Mude a linha `OPENAI_MODEL_NAME=`
3. Execute o projeto novamente

### 5. Estimativa de custo por execução:
- **gpt-4o-mini**: ~$0.50-1.00 por diagnóstico completo
- **gpt-4o**: ~$5.00-10.00 por diagnóstico completo  
- **gpt-4**: ~$15.00-25.00 por diagnóstico completo

### 6. Recomendação:
- **Desenvolvimento/Testes**: Use `gpt-4o-mini`
- **Produção**: Use `gpt-4o` 
- **Casos críticos**: Use `gpt-4`
