# INSTRUÇÕES PARA USO DOS ARQUIVOS CSV

## Arquivos disponíveis:

### 1. dados_entrada.csv
- Contém os 11 inputs principais que o cliente deve fornecer
- Estrutura: campo, valor, unidade, descricao
- Os agentes lerão estes dados para fazer os cálculos

### 2. metricas_calculadas.csv  
- Contém as métricas que serão calculadas automaticamente
- Estrutura: metrica, valor, formula, descricao
- Os agentes preencherão os valores baseado nos dados de entrada

## Como usar:

1. O cliente fornece os dados preenchendo a coluna "valor" no dados_entrada.csv
2. Os agentes CrewAI processam estes dados
3. As métricas são calculadas e salvas em metricas_calculadas.csv
4. Relatórios em Markdown são gerados com base nestes cálculos

## Vantagens dos CSVs:
- Mais simples de ler/escrever para os agentes
- Não há problemas de compatibilidade
- Fácil de converter para Excel depois
- Funciona perfeitamente com pandas e Python

## Próximos passos:
- Os agentes estão configurados para trabalhar com estes CSVs
- O projeto está pronto para executar
- Você pode testar inserindo dados de exemplo nos CSVs
