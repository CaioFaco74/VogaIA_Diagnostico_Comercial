"""
Ferramentas Python especializadas para cálculo de métricas comerciais
Diagnóstico Comercial Voga.IA - CrewAI Project
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Any, Optional
import json
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

try:
    from crewai.tools import BaseTool
except ImportError:
    try:
        from crewai_tools import BaseTool
    except ImportError:
        from crewai import BaseTool
import os

# Paths para os arquivos CSV
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
DADOS_ENTRADA_PATH = os.path.join(DATA_DIR, 'dados_entrada.csv')
METRICAS_PATH = os.path.join(DATA_DIR, 'metricas_calculadas.csv')

class CalcularCAC(BaseTool):
    name: str = "calcular_cac"
    description: str = "Calcula o Custo de Aquisição de Cliente (CAC)"
    
    def _run(self, custo_vendas_marketing: float, novos_clientes: int) -> Dict[str, Any]:
        try:
            if novos_clientes == 0:
                return {"cac": 0, "status": "erro", "mensagem": "CAC não pode ser calculado com zero novos clientes"}
            cac = custo_vendas_marketing / novos_clientes
            status = "bom" if cac <= 2000 else "atencao" if cac <= 5000 else "critico"
            return {"cac": round(cac, 2), "status": status, "formula": f"{custo_vendas_marketing:,.2f} ÷ {novos_clientes} = R$ {cac:,.2f}"}
        except Exception as e:
            return {"cac": 0, "status": "erro", "mensagem": str(e)}

class CalcularLTV(BaseTool):
    name: str = "calcular_ltv"
    description: str = "Calcula o Lifetime Value (LTV)"
    
    def _run(self, receita_total: float, clientes_ativos: int, churn_rate: Optional[float] = None) -> Dict[str, Any]:
        try:
            if clientes_ativos == 0:
                return {"ltv": 0, "status": "erro", "mensagem": "LTV não pode ser calculado com zero clientes"}
            ltv = receita_total / clientes_ativos
            status = "excelente" if ltv > 10000 else "bom" if ltv > 1000 else "atencao"
            return {"ltv": round(ltv, 2), "status": status, "formula": f"R$ {receita_total:,.2f} ÷ {clientes_ativos} = R$ {ltv:,.2f}"}
        except Exception as e:
            return {"ltv": 0, "status": "erro", "mensagem": str(e)}

class CalcularROISimples(BaseTool):
    name: str = "calcular_roi_simples"
    description: str = "Calcula o Return on Investment (ROI) simples"
    
    def _run(self, receita_total: float, investimento_total: float) -> Dict[str, Any]:
        try:
            if investimento_total == 0:
                return {"roi": 0, "status": "erro", "mensagem": "ROI não pode ser calculado com investimento zero"}
            roi = ((receita_total - investimento_total) / investimento_total) * 100
            status = "excelente" if roi > 300 else "bom" if roi > 200 else "atencao" if roi > 100 else "critico"
            return {"roi": round(roi, 2), "status": status, "formula": f"(R$ {receita_total:,.2f} - R$ {investimento_total:,.2f}) ÷ R$ {investimento_total:,.2f} × 100 = {roi:.2f}%"}
        except Exception as e:
            return {"roi": 0, "status": "erro", "mensagem": str(e)}

class CalcularROS(BaseTool):
    name: str = "calcular_ros"
    description: str = "Calcula o Return on Sales (ROS)"
    
    def _run(self, receita_total: float, custos_totais: float) -> Dict[str, Any]:
        try:
            if receita_total == 0:
                return {"ros": 0, "status": "erro", "mensagem": "ROS não pode ser calculado com receita zero"}
            lucro = receita_total - custos_totais
            ros = (lucro / receita_total) * 100
            status = "excelente" if ros > 15 else "bom" if ros > 5 else "atencao" if ros > 0 else "critico"
            return {"ros": round(ros, 2), "status": status, "lucro": round(lucro, 2), "formula": f"R$ {lucro:,.2f} ÷ R$ {receita_total:,.2f} × 100 = {ros:.2f}%"}
        except Exception as e:
            return {"ros": 0, "status": "erro", "mensagem": str(e)}

class CalcularTicketMedio(BaseTool):
    name: str = "calcular_ticket_medio"
    description: str = "Calcula o ticket médio"
    
    def _run(self, receita_total: float, negocios_fechados: int) -> Dict[str, Any]:
        try:
            if negocios_fechados == 0:
                return {"ticket_medio": 0, "status": "erro", "mensagem": "Ticket médio não pode ser calculado sem negócios fechados"}
            ticket = receita_total / negocios_fechados
            categoria = "Premium" if ticket > 50000 else "Alto" if ticket > 10000 else "Médio" if ticket > 1000 else "Baixo"
            return {"ticket_medio": round(ticket, 2), "categoria": categoria, "formula": f"R$ {receita_total:,.2f} ÷ {negocios_fechados} = R$ {ticket:,.2f}"}
        except Exception as e:
            return {"ticket_medio": 0, "status": "erro", "mensagem": str(e)}

class CalcularWinRate(BaseTool):
    name: str = "calcular_win_rate"
    description: str = "Calcula a taxa de conversão Win Rate"
    
    def _run(self, negocios_fechados: int, propostas_enviadas: int) -> Dict[str, Any]:
        try:
            if propostas_enviadas == 0:
                return {"win_rate": 0, "status": "erro", "mensagem": "Win rate não pode ser calculado sem propostas"}
            win_rate = (negocios_fechados / propostas_enviadas) * 100
            status = "excelente" if win_rate > 35 else "bom" if win_rate > 20 else "atencao" if win_rate > 10 else "critico"
            return {"win_rate": round(win_rate, 2), "status": status, "formula": f"{negocios_fechados} ÷ {propostas_enviadas} × 100 = {win_rate:.2f}%"}
        except Exception as e:
            return {"win_rate": 0, "status": "erro", "mensagem": str(e)}

class CalcularPipelineVelocity(BaseTool):
    name: str = "calcular_pipeline_velocity"
    description: str = "Calcula a velocidade do pipeline"
    
    def _run(self, ticket_medio: float, win_rate: float, ciclo_vendas_dias: int) -> Dict[str, Any]:
        try:
            if ciclo_vendas_dias == 0:
                return {"pipeline_velocity": 0, "status": "erro", "mensagem": "Pipeline velocity não pode ser calculada com ciclo zero"}
            velocity = (ticket_medio * (win_rate / 100)) / ciclo_vendas_dias
            status = "excelente" if velocity > 1000 else "bom" if velocity > 100 else "atencao"
            return {"pipeline_velocity_diaria": round(velocity, 2), "pipeline_velocity_mensal": round(velocity * 30, 2), "status": status}
        except Exception as e:
            return {"pipeline_velocity": 0, "status": "erro", "mensagem": str(e)}

class CalcularProdutividadeRep(BaseTool):
    name: str = "calcular_produtividade_rep"
    description: str = "Calcula a produtividade por representante"
    
    def _run(self, receita_total: float, reps_ativos: int) -> Dict[str, Any]:
        try:
            if reps_ativos == 0:
                return {"produtividade_rep": 0, "status": "erro", "mensagem": "Produtividade não pode ser calculada sem representantes"}
            produtividade = receita_total / reps_ativos
            status = "excelente" if produtividade > 500000 else "bom" if produtividade > 200000 else "atencao" if produtividade > 50000 else "critico"
            return {"produtividade_rep": round(produtividade, 2), "status": status, "formula": f"R$ {receita_total:,.2f} ÷ {reps_ativos} = R$ {produtividade:,.2f}"}
        except Exception as e:
            return {"produtividade_rep": 0, "status": "erro", "mensagem": str(e)}

class CalcularConversaoFunil(BaseTool):
    name: str = "calcular_conversao_funil"
    description: str = "Calcula as taxas de conversão do funil"
    
    def _run(self, leads_gerados: int, propostas_enviadas: int, negocios_fechados: int) -> Dict[str, Any]:
        try:
            resultado: Dict[str, Any] = {"gargalos": [], "oportunidades": []}
            
            if leads_gerados > 0:
                conv_lead_proposta = (propostas_enviadas / leads_gerados) * 100
                resultado["conversao_lead_proposta"] = round(conv_lead_proposta, 2)
                if conv_lead_proposta < 10:
                    resultado["gargalos"].append("Baixa conversão Lead → Proposta")
            
            if propostas_enviadas > 0:
                conv_proposta_fechamento = (negocios_fechados / propostas_enviadas) * 100
                resultado["conversao_proposta_fechamento"] = round(conv_proposta_fechamento, 2)
                if conv_proposta_fechamento < 20:
                    resultado["gargalos"].append("Baixa conversão Proposta → Fechamento")
            
            if leads_gerados > 0:
                conv_total = (negocios_fechados / leads_gerados) * 100
                resultado["conversao_lead_fechamento"] = round(conv_total, 2)
            
            resultado["status"] = "critico" if len(resultado["gargalos"]) > 1 else "atencao" if len(resultado["gargalos"]) == 1 else "bom"
            return resultado
        except Exception as e:
            return {"status": "erro", "mensagem": str(e)}

class DetectarOutliers(BaseTool):
    name: str = "detectar_outliers"
    description: str = "Detecta valores atípicos nos dados"
    
    def _run(self, dados: Optional[Dict[str, float]] = None) -> Dict[str, Any]:
        try:
            if dados is None or not dados:
                return {"outliers_detectados": [], "status": "info", "mensagem": "Nenhum dado fornecido para análise de outliers"}
            
            valores = list(dados.values())
            if len(valores) < 4:
                return {"outliers_detectados": [], "status": "info", "mensagem": "Poucos dados para análise de outliers"}
            
            q1, q3 = np.percentile(valores, [25, 75])
            iqr = q3 - q1
            limite_inf = q1 - (1.5 * iqr)
            limite_sup = q3 + (1.5 * iqr)
            
            outliers = []
            for nome, valor in dados.items():
                if valor < limite_inf or valor > limite_sup:
                    outliers.append({"metrica": nome, "valor": valor, "tipo": "superior" if valor > limite_sup else "inferior"})
            
            status = "bom" if len(outliers) == 0 else "atencao" if len(outliers) <= 2 else "critico"
            return {"outliers_detectados": outliers, "status": status}
        except Exception as e:
            return {"outliers_detectados": [], "status": "erro", "mensagem": str(e)}

class GerarBenchmarkSetor(BaseTool):
    name: str = "gerar_benchmark_setor"
    description: str = "Gera benchmarks do setor"
    
    def _run(self, setor: str = "geral", tamanho_empresa: str = "media") -> Dict[str, Any]:
        try:
            benchmarks = {
                "geral": {
                    "cac": {"min": 500, "max": 3000, "ideal": 1500},
                    "ltv": {"min": 3000, "max": 30000, "ideal": 10000},
                    "win_rate": {"min": 15, "max": 35, "ideal": 25},
                    "roi": {"min": 200, "max": 450, "ideal": 300}
                }
            }
            
            return {
                "setor": setor,
                "tamanho_empresa": tamanho_empresa,
                "benchmarks": benchmarks.get(setor, benchmarks["geral"]),
                "fonte": "Benchmarks baseados no mercado brasileiro 2024-2025"
            }
        except Exception as e:
            return {"benchmarks": {}, "status": "erro", "mensagem": str(e)}

class CriarGraficosPerformance(BaseTool):
    name: str = "criar_graficos_performance"
    description: str = "Cria visualizações para relatórios baseado nas métricas reais do CSV"
    
    def _run(self, metricas_csv: Optional[List[Dict]] = None) -> Dict[str, str]:
        try:
            graficos = {}
            
            # Se não recebeu métricas, ler do CSV
            if metricas_csv is None:
                if os.path.exists(METRICAS_PATH):
                    df = pd.read_csv(METRICAS_PATH)
                    metricas_dict = dict(zip(df['metrica'], df['valor']))
                else:
                    return {"erro": "Arquivo de métricas não encontrado"}
            else:
                # Converter lista de dicts em dict simples
                metricas_dict = {m.get('metrica', ''): m.get('valor', 0) for m in metricas_csv}
            
            # Extrair métricas principais
            cac = metricas_dict.get('CAC', 0)
            ltv = metricas_dict.get('LTV', 0)
            roi = metricas_dict.get('ROI', 0)
            win_rate = metricas_dict.get('Win_Rate', 0)
            magic_number = metricas_dict.get('Magic_Number', 0)
            
            # Gráfico CAC vs LTV
            ratio = ltv / cac if cac > 0 else 0
            status_ratio = '✅ Excelente' if ratio >= 4 else '🟡 Bom' if ratio >= 3 else '⚠️ Atenção' if ratio >= 2 else '❌ Crítico'
            
            graficos["cac_ltv_analysis"] = f"""
## 📊 Análise CAC vs LTV

| Métrica | Valor | Status |
|---------|-------|--------|
| CAC | R$ {cac:,.2f} | {'🔴 Alto' if cac > 3000 else '🟡 Moderado' if cac > 2000 else '🟢 Bom'} |
| LTV | R$ {ltv:,.2f} | {'🟢 Excelente' if ltv > 10000 else '🟡 Bom' if ltv > 5000 else '🔴 Baixo'} |
| **Magic Number** | **{ratio:.1f}:1** | **{status_ratio}** |

### Interpretação:
- Cada R$ 1 investido em CAC gera R$ {ratio:.2f} em LTV
- Benchmark ideal: 4:1 ou superior
- Status atual: {status_ratio}
"""
            
            # Gráfico Performance Geral
            graficos["performance_overview"] = f"""
## 📈 Overview de Performance

| KPI | Valor | Benchmark | Status |
|-----|-------|-----------|--------|
| ROI | {roi:.1f}% | 300% | {'🟢' if roi >= 300 else '🟡' if roi >= 200 else '🔴'} |
| Win Rate | {win_rate:.1f}% | 25% | {'🟢' if win_rate >= 25 else '🟡' if win_rate >= 20 else '🔴'} |
| Magic Number | {magic_number:.1f}:1 | 4:1 | {'🟢' if magic_number >= 4 else '🟡' if magic_number >= 3 else '🔴'} |
"""
            
            return graficos
        except Exception as e:
            return {"erro": f"Erro ao criar gráficos: {str(e)}"}

class GerarPlanilhaDiagnostico(BaseTool):
    name: str = "gerar_planilha_diagnostico"
    description: str = "Gera estrutura para planilha Excel baseada nas métricas reais do CSV"
    
    def _run(self, dados_completos: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        try:
            # Ler métricas do CSV
            if os.path.exists(METRICAS_PATH) and os.path.exists(DADOS_ENTRADA_PATH):
                df_metricas = pd.read_csv(METRICAS_PATH)
                df_dados = pd.read_csv(DADOS_ENTRADA_PATH)
                
                # Converter em dicionários
                metricas = dict(zip(df_metricas['metrica'], df_metricas['valor']))
                dados = dict(zip(df_dados['campo'], df_dados['valor']))
                
                estrutura = {
                    "resumo_executivo": {
                        "data_geracao": datetime.now().strftime("%d/%m/%Y %H:%M"),
                        "empresa": dados.get('Setor_Empresa', 'SaaS'),
                        "porte": dados.get('Porte_Empresa', 'Media'),
                        "periodo_analise": "Q4 2025",
                        "metricas_principais": {
                            "receita_total": f"R$ {dados.get('Receita_Total', 0):,.2f}",
                            "meta_receita": f"R$ {dados.get('Meta_Receita_Periodo', 0):,.2f}",
                            "roi": f"{metricas.get('ROI', 0):.1f}%",
                            "cac": f"R$ {metricas.get('CAC', 0):,.2f}",
                            "ltv": f"R$ {metricas.get('LTV', 0):,.2f}",
                            "magic_number": f"{metricas.get('Magic_Number', 0):.1f}:1",
                            "win_rate": f"{metricas.get('Win_Rate', 0):.1f}%"
                        }
                    }
                }
                return {"estrutura_planilha": estrutura, "status": "sucesso"}
            else:
                return {"estrutura_planilha": {}, "status": "erro", "mensagem": "Arquivos CSV não encontrados"}
        except Exception as e:
            return {"estrutura_planilha": {}, "status": "erro", "mensagem": str(e)}

class LerDadosCSV(BaseTool):
    name: str = "ler_dados_csv"
    description: str = "Lê dados dos arquivos CSV"
    
    def _run(self, arquivo: str = "dados_entrada") -> Dict[str, Any]:
        try:
            # Mapear diferentes nomes para o arquivo correto
            if arquivo in ["dados_entrada", "dados_entrada.csv", "dados_cliente.csv", "dados_cliente", "dados_metrica.csv"]:
                if os.path.exists(DADOS_ENTRADA_PATH):
                    df = pd.read_csv(DADOS_ENTRADA_PATH)
                    dados = {}
                    for _, row in df.iterrows():
                        dados[row['campo']] = {
                            'valor': row['valor'],
                            'unidade': row['unidade'],
                            'descricao': row['descricao']
                        }
                    return {"dados": dados, "status": "sucesso", "total_campos": len(dados)}
                else:
                    return {"dados": {}, "status": "erro", "mensagem": f"Arquivo não encontrado: {DADOS_ENTRADA_PATH}"}
            elif arquivo == "metricas":
                if os.path.exists(METRICAS_PATH):
                    df = pd.read_csv(METRICAS_PATH)
                    return {"metricas": df.to_dict('records'), "status": "sucesso"}
                else:
                    return {"metricas": [], "status": "erro", "mensagem": f"Arquivo não encontrado: {METRICAS_PATH}"}
            else:
                # Tentar ler arquivo personalizado
                file_path = os.path.join(DATA_DIR, f"{arquivo}.csv")
                if os.path.exists(file_path):
                    df = pd.read_csv(file_path)
                    return {"dados": df.to_dict('records'), "status": "sucesso"}
                else:
                    return {"dados": {}, "status": "erro", "mensagem": f"Arquivo não encontrado: {file_path}"}
        except Exception as e:
            return {"dados": {}, "status": "erro", "mensagem": f"Erro ao ler arquivo: {str(e)}"}

class SalvarMetricasCSV(BaseTool):
    name: str = "salvar_metricas_csv"
    description: str = "Salva métricas calculadas no CSV"
    
    def _run(self, metricas_calculadas: Dict[str, float]) -> Dict[str, Any]:
        try:
            df = pd.read_csv(METRICAS_PATH)
            
            for metrica, valor in metricas_calculadas.items():
                if metrica in df['metrica'].values:
                    df.loc[df['metrica'] == metrica, 'valor'] = valor
            
            df.to_csv(METRICAS_PATH, index=False)
            return {"status": "sucesso", "mensagem": f"Métricas salvas: {list(metricas_calculadas.keys())}"}
        except Exception as e:
            return {"status": "erro", "mensagem": str(e)}

class ExportarRelatorioMD(BaseTool):
    name: str = "exportar_relatorio_md"
    description: str = "Exporta relatório em Markdown"
    
    def _run(self, dados_analise: Dict[str, Any], insights: List[str], recomendacoes: List[str]) -> str:
        try:
            relatorio = f"""# 📊 Diagnóstico Comercial - Relatório Executivo

**Data:** {datetime.now().strftime("%d/%m/%Y")}
**Gerado por:** Sistema Diagnóstico Voga.IA

## 🎯 Sumário Executivo

- **Receita Total:** R$ {dados_analise.get('receita_total', 0):,.2f}
- **ROI:** {dados_analise.get('roi', 0):.1f}%
- **CAC:** R$ {dados_analise.get('cac', 0):,.2f}
- **LTV:** R$ {dados_analise.get('ltv', 0):,.2f}

## 💡 Principais Insights

"""
            
            for i, insight in enumerate(insights[:5], 1):
                relatorio += f"{i}. {insight}\n"
            
            relatorio += "\n## 🚀 Recomendações Priorizadas\n\n"
            
            for i, rec in enumerate(recomendacoes[:5], 1):
                relatorio += f"{i}. {rec}\n"
            
            relatorio += f"\n---\n*Gerado automaticamente em {datetime.now().strftime('%d/%m/%Y às %H:%M')}*"
            
            return relatorio
        except Exception as e:
            return f"# Erro na Geração do Relatório\n\nErro: {str(e)}"

class SalvarRelatorioAgente(BaseTool):
    name: str = "salvar_relatorio_agente"
    description: str = "Salva relatório específico de um agente em arquivo MD"
    
    def _run(self, conteudo_relatorio: str, nome_agente: str, numero_agente: int) -> Dict[str, Any]:
        try:
            # Criar diretório outputs se não existir
            outputs_dir = os.path.join(os.path.dirname(DATA_DIR), 'outputs')
            os.makedirs(outputs_dir, exist_ok=True)
            
            # Nome do arquivo baseado no número e nome do agente
            filename = f"{numero_agente:02d}_{nome_agente.lower().replace(' ', '_')}_report.md"
            file_path = os.path.join(outputs_dir, filename)
            
            # Adicionar cabeçalho ao relatório
            relatorio_completo = f"""# 📊 Relatório do Agente: {nome_agente}

**Data:** {datetime.now().strftime("%d/%m/%Y")}
**Hora:** {datetime.now().strftime("%H:%M:%S")}
**Agente:** {numero_agente} - {nome_agente}
**Sistema:** Diagnóstico Comercial Voga.IA

---

{conteudo_relatorio}

---
*Relatório gerado automaticamente pelo sistema Voga.IA*
"""
            
            # Salvar arquivo com tratamento de encoding
            try:
                with open(file_path, 'w', encoding='utf-8', errors='replace') as f:
                    f.write(relatorio_completo)
            except UnicodeEncodeError:
                # Fallback: remover caracteres problemáticos
                relatorio_limpo = relatorio_completo.encode('utf-8', errors='ignore').decode('utf-8')
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(relatorio_limpo)
            
            return {
                "status": "sucesso",
                "arquivo": filename,
                "path": file_path,
                "tamanho": len(relatorio_completo),
                "mensagem": f"Relatório salvo: {filename}"
            }
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro ao salvar relatório: {str(e)}"}

class CriarDashboardSpecs(BaseTool):
    name: str = "criar_dashboard_specs"
    description: str = "Cria especificações técnicas para dashboard"
    
    def _run(self, metricas_principais: Dict[str, Any], paginas_dashboard: List[str]) -> str:
        try:
            specs = f"""# 📊 Especificações Técnicas do Dashboard

## 🎯 Páginas do Dashboard

"""
            for i, pagina in enumerate(paginas_dashboard, 1):
                specs += f"{i}. **{pagina}**\n"
            
            specs += f"""
## 📈 Métricas Principais

| Métrica | Valor Atual | Status |
|---------|-------------|--------|
"""
            for metrica, valor in metricas_principais.items():
                if isinstance(valor, (int, float)):
                    specs += f"| {metrica} | {valor:,.2f} | ✅ Ativo |\n"
                else:
                    specs += f"| {metrica} | {valor} | ✅ Ativo |\n"
            
            specs += f"""
## 🛠️ Especificações Técnicas

### Ferramentas Recomendadas:
- **Power BI**: Para integração com Excel e Azure
- **Tableau**: Para visualizações avançadas
- **Metabase**: Para solução open-source
- **Grafana**: Para monitoramento em tempo real

### Estrutura de Dados:
- **Fonte**: CSV com métricas calculadas
- **Atualização**: Tempo real ou batch diário
- **Filtros**: Por período, canal, representante

### KPIs por Página:
1. **Overview**: CAC, LTV, ROI, Win Rate
2. **Financeiro**: Receita, Custos, Margens
3. **Operacional**: Pipeline, Produtividade
4. **Alertas**: Desvios e oportunidades
"""
            return specs
        except Exception as e:
            return f"# Erro na Criação das Specs\n\nErro: {str(e)}"

class GerarAlertas(BaseTool):
    name: str = "gerar_alertas"
    description: str = "Gera configurações de alertas baseadas nas métricas"
    
    def _run(self, metricas_atuais: Dict[str, float]) -> str:
        try:
            alertas = f"""# 🚨 Sistema de Alertas - Diagnóstico Comercial

## ⚠️ Alertas Críticos (Ação Imediata)

"""
            cac = metricas_atuais.get('cac', 0)
            ltv = metricas_atuais.get('ltv', 0)
            roi = metricas_atuais.get('roi', 0)
            win_rate = metricas_atuais.get('win_rate', 0)
            
            # Alertas críticos
            if roi < 100:
                alertas += "🔴 **ROI CRÍTICO**: ROI abaixo de 100% - Revisar estratégia imediatamente\n"
            if cac > 0 and ltv > 0 and (ltv/cac) < 3:
                alertas += f"🔴 **LTV/CAC BAIXO**: Ratio atual {ltv/cac:.1f} - Abaixo do mínimo 3:1\n"
            if win_rate < 10:
                alertas += "🔴 **WIN RATE CRÍTICO**: Taxa de conversão muito baixa\n"
            
            alertas += f"""
## 🟡 Alertas de Atenção

"""
            if 100 <= roi < 200:
                alertas += f"🟡 **ROI MODERADO**: {roi:.1f}% - Pode ser melhorado\n"
            if 2000 < cac <= 5000:
                alertas += f"🟡 **CAC ALTO**: R$ {cac:,.2f} - Otimizar aquisição\n"
            if 15 <= win_rate < 25:
                alertas += f"🟡 **WIN RATE MÉDIO**: {win_rate:.1f}% - Potencial de melhoria\n"
                
            alertas += f"""
## 🟢 Alertas de Oportunidade

"""
            if roi > 300:
                alertas += f"🟢 **ROI EXCELENTE**: {roi:.1f}% - Escalabilidade possível\n"
            if ltv > 15000:
                alertas += f"🟢 **LTV ALTO**: R$ {ltv:,.2f} - Foco em retenção\n"
            if win_rate > 30:
                alertas += f"🟢 **WIN RATE SUPERIOR**: {win_rate:.1f}% - Replicar estratégia\n"
                
            alertas += f"""
## ⚙️ Configurações de Monitoramento

### Frequência de Verificação:
- **Métricas Críticas**: Diário
- **Métricas de Atenção**: Semanal  
- **Métricas de Oportunidade**: Mensal

### Notificações:
- 📧 Email para gestores comerciais
- 📱 Slack/Teams para equipe
- 📊 Dashboard com status visual
"""
            return alertas
        except Exception as e:
            return f"# Erro na Geração de Alertas\n\nErro: {str(e)}"

# ========== NOVAS FERRAMENTAS PARA 32 MÉTRICAS ==========

class CalcularMagicNumber(BaseTool):
    name: str = "calcular_magic_number"
    description: str = "Calcula o Magic Number (LTV/CAC ratio)"
    
    def _run(self, ltv: float, cac: float) -> Dict[str, Any]:
        try:
            if cac == 0:
                return {"magic_number": 0, "status": "erro", "mensagem": "Magic Number não pode ser calculado com CAC zero"}
            magic_number = ltv / cac
            status = "excelente" if magic_number >= 4 else "bom" if magic_number >= 3 else "atencao" if magic_number >= 2 else "critico"
            return {
                "magic_number": round(magic_number, 2),
                "status": status,
                "interpretacao": f"Para cada R$ 1 de CAC, geramos R$ {magic_number:.2f} de LTV",
                "formula": f"R$ {ltv:,.2f} ÷ R$ {cac:,.2f} = {magic_number:.2f}:1"
            }
        except Exception as e:
            return {"magic_number": 0, "status": "erro", "mensagem": str(e)}

class CalcularPaybackPeriod(BaseTool):
    name: str = "calcular_payback_period"
    description: str = "Calcula o período de payback do CAC"
    
    def _run(self, cac: Optional[float] = None, receita_total: Optional[float] = None, novos_clientes: Optional[int] = None, periodo_meses: int = 12) -> Dict[str, Any]:
        try:
            if cac is None or receita_total is None or novos_clientes is None:
                return {"payback_months": 0, "status": "erro", "mensagem": "Payback requer CAC, receita total e novos clientes"}
            
            if novos_clientes == 0 or receita_total == 0:
                return {"payback_months": 0, "status": "erro", "mensagem": "Payback não pode ser calculado com valores zero"}
            
            receita_mensal_cliente = (receita_total / novos_clientes) / periodo_meses
            payback = cac / receita_mensal_cliente if receita_mensal_cliente > 0 else 0
            
            status = "excelente" if payback <= 6 else "bom" if payback <= 12 else "atencao" if payback <= 18 else "critico"
            return {
                "payback_months": round(payback, 1),
                "receita_mensal_cliente": round(receita_mensal_cliente, 2),
                "status": status,
                "interpretacao": f"Recupera o CAC em {payback:.1f} meses",
                "formula": f"R$ {cac:,.2f} ÷ R$ {receita_mensal_cliente:,.2f} = {payback:.1f} meses"
            }
        except Exception as e:
            return {"payback_months": 0, "status": "erro", "mensagem": str(e)}

class CalcularMargemBruta(BaseTool):
    name: str = "calcular_margem_bruta"
    description: str = "Calcula margem bruta real vs esperada"
    
    def _run(self, receita_total: float, custo_produto_vendido: float, margem_esperada: float) -> Dict[str, Any]:
        try:
            if receita_total == 0:
                return {"margem_bruta": 0, "status": "erro", "mensagem": "Margem bruta não pode ser calculada com receita zero"}
            
            margem_real = ((receita_total - custo_produto_vendido) / receita_total) * 100
            diferenca = margem_real - margem_esperada
            
            status = "excelente" if diferenca >= 5 else "bom" if diferenca >= 0 else "atencao" if diferenca >= -5 else "critico"
            return {
                "margem_bruta_real": round(margem_real, 2),
                "margem_bruta_esperada": margem_esperada,
                "diferenca": round(diferenca, 2),
                "status": status,
                "lucro_bruto": round(receita_total - custo_produto_vendido, 2),
                "formula": f"(R$ {receita_total:,.2f} - R$ {custo_produto_vendido:,.2f}) ÷ R$ {receita_total:,.2f} × 100 = {margem_real:.2f}%"
            }
        except Exception as e:
            return {"margem_bruta": 0, "status": "erro", "mensagem": str(e)}

class CalcularMetaAchievement(BaseTool):
    name: str = "calcular_meta_achievement"
    description: str = "Calcula % de atingimento da meta"
    
    def _run(self, receita_real: float, meta_receita: float) -> Dict[str, Any]:
        try:
            if meta_receita == 0:
                return {"meta_achievement": 0, "status": "erro", "mensagem": "Meta Achievement não pode ser calculado com meta zero"}
            
            achievement = (receita_real / meta_receita) * 100
            status = "excelente" if achievement >= 110 else "bom" if achievement >= 100 else "atencao" if achievement >= 80 else "critico"
            
            return {
                "meta_achievement": round(achievement, 2),
                "status": status,
                "diferenca_absoluta": round(receita_real - meta_receita, 2),
                "diferenca_percentual": round(achievement - 100, 2),
                "formula": f"R$ {receita_real:,.2f} ÷ R$ {meta_receita:,.2f} × 100 = {achievement:.2f}%"
            }
        except Exception as e:
            return {"meta_achievement": 0, "status": "erro", "mensagem": str(e)}

class CalcularConversoesFunilDetalhado(BaseTool):
    name: str = "calcular_conversoes_funil_detalhado"
    description: str = "Calcula todas as conversões do funil detalhado com MQLs e SQLs"
    
    def _run(self, leads: int, mql: int, sql: int, reunioes: int, propostas: int, fechados: int) -> Dict[str, Any]:
        try:
            conversoes = {}
            gargalos = []
            oportunidades = []
            
            # Lead → MQL
            if leads > 0 and mql > 0:
                conv_lead_mql = (mql / leads) * 100
                conversoes["lead_to_mql"] = round(conv_lead_mql, 2)
                if conv_lead_mql < 30:
                    gargalos.append("Baixa conversão Lead → MQL")
                elif conv_lead_mql > 50:
                    oportunidades.append("Excelente conversão Lead → MQL")
            
            # MQL → SQL
            if mql > 0 and sql > 0:
                conv_mql_sql = (sql / mql) * 100
                conversoes["mql_to_sql"] = round(conv_mql_sql, 2)
                if conv_mql_sql < 40:
                    gargalos.append("Baixa conversão MQL → SQL")
                elif conv_mql_sql > 60:
                    oportunidades.append("Excelente conversão MQL → SQL")
            
            # SQL → Reunião
            if sql > 0 and reunioes > 0:
                conv_sql_reuniao = (reunioes / sql) * 100
                conversoes["sql_to_reuniao"] = round(conv_sql_reuniao, 2)
                if conv_sql_reuniao < 60:
                    gargalos.append("Baixa conversão SQL → Reunião")
                elif conv_sql_reuniao > 80:
                    oportunidades.append("Excelente conversão SQL → Reunião")
            
            # Reunião → Proposta
            if reunioes > 0 and propostas > 0:
                conv_reuniao_proposta = (propostas / reunioes) * 100
                conversoes["reuniao_to_proposta"] = round(conv_reuniao_proposta, 2)
                if conv_reuniao_proposta < 70:
                    gargalos.append("Baixa conversão Reunião → Proposta")
                elif conv_reuniao_proposta > 90:
                    oportunidades.append("Excelente conversão Reunião → Proposta")
            
            # Proposta → Fechamento
            if propostas > 0 and fechados > 0:
                conv_proposta_fechamento = (fechados / propostas) * 100
                conversoes["proposta_to_fechamento"] = round(conv_proposta_fechamento, 2)
                if conv_proposta_fechamento < 20:
                    gargalos.append("Baixa conversão Proposta → Fechamento")
                elif conv_proposta_fechamento > 35:
                    oportunidades.append("Excelente conversão Proposta → Fechamento")
            
            # Lead → Fechamento (conversão total)
            if leads > 0 and fechados > 0:
                conv_total = (fechados / leads) * 100
                conversoes["lead_to_fechamento"] = round(conv_total, 2)
                if conv_total < 3:
                    gargalos.append("Baixa conversão total Lead → Fechamento")
                elif conv_total > 7:
                    oportunidades.append("Excelente conversão total")
            
            # Determinar status geral
            if len(gargalos) >= 3:
                status = "critico"
            elif len(gargalos) >= 1:
                status = "atencao"
            elif len(oportunidades) >= 2:
                status = "excelente"
            else:
                status = "bom"
            
            return {
                "conversoes": conversoes,
                "gargalos": gargalos,
                "oportunidades": oportunidades,
                "status": status
            }
        except Exception as e:
            return {"status": "erro", "mensagem": str(e)}

class CalcularProdutividadeDetalhada(BaseTool):
    name: str = "calcular_produtividade_detalhada"
    description: str = "Calcula métricas de produtividade detalhadas por rep"
    
    def _run(self, dados: Dict[str, Any]) -> Dict[str, Any]:
        try:
            reps = dados.get('reps_ativos', 1)
            if reps == 0:
                return {"status": "erro", "mensagem": "Não é possível calcular produtividade sem representantes"}
            
            produtividade = {
                "leads_por_rep": round(dados.get('leads', 0) / reps, 2),
                "mql_por_rep": round(dados.get('mql', 0) / reps, 2),
                "sql_por_rep": round(dados.get('sql', 0) / reps, 2),
                "reunioes_por_rep": round(dados.get('reunioes', 0) / reps, 2),
                "propostas_por_rep": round(dados.get('propostas', 0) / reps, 2),
                "fechamentos_por_rep": round(dados.get('fechados', 0) / reps, 2),
                "receita_por_rep": round(dados.get('receita', 0) / reps, 2)
            }
            
            # Análise de eficiência
            receita_por_rep = produtividade["receita_por_rep"]
            if receita_por_rep > 200000:
                status = "excelente"
            elif receita_por_rep > 100000:
                status = "bom"
            elif receita_por_rep > 50000:
                status = "atencao"
            else:
                status = "critico"
            
            produtividade["status"] = status
            return produtividade
        except Exception as e:
            return {"status": "erro", "mensagem": str(e)}

class CalcularROAS(BaseTool):
    name: str = "calcular_roas"
    description: str = "Calcula Return on Ad Spend (ROAS)"
    
    def _run(self, receita_total: float, custo_marketing: float) -> Dict[str, Any]:
        try:
            if custo_marketing == 0:
                return {"roas": 0, "status": "erro", "mensagem": "ROAS não pode ser calculado com custo de marketing zero"}
            
            roas = receita_total / custo_marketing
            status = "excelente" if roas >= 5 else "bom" if roas >= 3 else "atencao" if roas >= 2 else "critico"
            
            return {
                "roas": round(roas, 2),
                "status": status,
                "interpretacao": f"Cada R$ 1 em marketing gera R$ {roas:.2f} em receita",
                "formula": f"R$ {receita_total:,.2f} ÷ R$ {custo_marketing:,.2f} = {roas:.2f}:1"
            }
        except Exception as e:
            return {"roas": 0, "status": "erro", "mensagem": str(e)}

class CalcularChurnEstimado(BaseTool):
    name: str = "calcular_churn_estimado"
    description: str = "Estima churn baseado na variação de clientes"
    
    def _run(self, clientes_iniciais: int, novos_clientes: int, clientes_finais: int) -> Dict[str, Any]:
        try:
            # Clientes que deveríamos ter se não houve churn
            clientes_esperados = clientes_iniciais + novos_clientes
            
            # Clientes que "saíram" (churn estimado)
            churn_estimado = max(0, clientes_esperados - clientes_finais)
            
            # Taxa de churn
            if clientes_esperados > 0:
                churn_rate = (churn_estimado / clientes_esperados) * 100
            else:
                churn_rate = 0
            
            # Taxa de crescimento líquido
            net_new_clients = clientes_finais - clientes_iniciais
            if clientes_iniciais > 0:
                growth_rate = (net_new_clients / clientes_iniciais) * 100
            else:
                growth_rate = 0
            
            # Status
            status = "excelente" if churn_rate <= 5 else "bom" if churn_rate <= 10 else "atencao" if churn_rate <= 15 else "critico"
            
            return {
                "churn_estimado": churn_estimado,
                "churn_rate": round(churn_rate, 2),
                "net_new_clients": net_new_clients,
                "growth_rate": round(growth_rate, 2),
                "status": status,
                "interpretacao": f"Taxa de churn estimada: {churn_rate:.1f}% - Crescimento líquido: {growth_rate:.1f}%"
            }
        except Exception as e:
            return {"churn_estimado": 0, "status": "erro", "mensagem": str(e)}

class AnaliseSPICED(BaseTool):
    name: str = "analise_spiced"
    description: str = "Analisa os dados SPICED fornecidos pelo cliente"
    
    def _run(self, spiced_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        try:
            if spiced_data is None:
                spiced_data = {}
            
            # Convert all values to strings and extract only SPICED-related fields
            spiced_only = {}
            for key, value in spiced_data.items():
                if any(spiced_key in key.lower() for spiced_key in ['situacao', 'problema', 'impacto', 'evento', 'decisao']):
                    spiced_only[key] = str(value) if value is not None else ""
            
            analise = {
                "situacao": spiced_only.get("situacao_atual", "Crescimento Acelerado"),
                "problema": spiced_only.get("problema_principal", "CAC Alto Conversão Baixa"),
                "impacto": spiced_only.get("impacto_problema", "Redução Margem Crescimento Lento"),
                "evento_critico": spiced_only.get("evento_critico", "Lançamento Novo Produto Q4"),
                "decisao_esperada": spiced_only.get("decisao_esperada", "Otimizar Marketing Treinar Vendas")
            }
            
            # Análise de prioridade baseada no evento crítico
            evento = analise["evento_critico"].lower()
            if "q4" in evento or "trimestre" in evento:
                prioridade = "alta"
                urgencia = "3 meses"
            elif "produto" in evento or "lancamento" in evento:
                prioridade = "alta"
                urgencia = "2 meses"
            elif "mercado" in evento or "concorrencia" in evento:
                prioridade = "media"
                urgencia = "6 meses"
            else:
                prioridade = "media"
                urgencia = "4 meses"
            
            # Análise do problema principal
            problema = analise["problema"].lower()
            areas_foco = []
            if "cac" in problema:
                areas_foco.append("otimizacao_marketing")
            if "conversao" in problema:
                areas_foco.append("treinamento_vendas")
            if "pipeline" in problema:
                areas_foco.append("gestao_funil")
            if "margem" in problema:
                areas_foco.append("estrutura_custos")
            
            return {
                "analise_spiced": analise,
                "prioridade": prioridade,
                "urgencia": urgencia,
                "areas_foco": areas_foco,
                "status": "analisado"
            }
        except Exception as e:
            return {"status": "erro", "mensagem": str(e)}
