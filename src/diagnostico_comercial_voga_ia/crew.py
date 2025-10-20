from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os
from dotenv import load_dotenv
import yaml

# Carregar variáveis de ambiente
load_dotenv()

# Configurar modelo LLM via variável de ambiente
default_llm_model = os.getenv('OPENAI_MODEL_NAME', 'gpt-4o-mini')
os.environ['OPENAI_MODEL_NAME'] = default_llm_model

from diagnostico_comercial_voga_ia.tools.diagnostico_tools import (
    # Ferramentas originais
    CalcularCAC,
    CalcularLTV,
    CalcularROISimples,
    CalcularROS,
    CalcularTicketMedio,
    CalcularWinRate,
    CalcularPipelineVelocity,
    CalcularProdutividadeRep,
    CalcularConversaoFunil,
    DetectarOutliers,
    GerarBenchmarkSetor,
    CriarGraficosPerformance,
    GerarPlanilhaDiagnostico,
    LerDadosCSV,
    SalvarMetricasCSV,
    ExportarRelatorioMD,
    SalvarRelatorioAgente,
    CriarDashboardSpecs,
    GerarAlertas,
    # Novas ferramentas para 40 métricas
    CalcularMagicNumber,
    CalcularPaybackPeriod,
    CalcularMargemBruta,
    CalcularMetaAchievement,
    CalcularConversoesFunilDetalhado,
    CalcularProdutividadeDetalhada,
    CalcularROAS,
    CalcularChurnEstimado,
    AnaliseSPICED
)

@CrewBase
class DiagnosticoComercialVogaIaCrew():
	"""Diagnóstico Comercial Voga.IA crew"""

	def __init__(self):
		# Carregar configurações dos agentes
		with open(os.path.join(os.path.dirname(__file__), 'config', 'agents.yaml'), 'r', encoding='utf-8') as f:
			self.agents_config = yaml.safe_load(f)
		# Carregar configurações das tasks
		with open(os.path.join(os.path.dirname(__file__), 'config', 'tasks.yaml'), 'r', encoding='utf-8') as f:
			self.tasks_config = yaml.safe_load(f)

	@agent
	def data_collector_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['data_collector_agent'],
			tools=[LerDadosCSV(), SalvarRelatorioAgente()],
			verbose=True
		)

	@agent
	def data_governance_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['data_governance_agent'],
			tools=[DetectarOutliers(), SalvarRelatorioAgente()],
			verbose=True
		)

	@agent
	def metrics_calculator_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['metrics_calculator_agent'],
			tools=[
				# Leitura e salvamento
				LerDadosCSV(),
				SalvarMetricasCSV(),
				SalvarRelatorioAgente(),
				# Métricas financeiras básicas
				CalcularCAC(),
				CalcularLTV(),
				CalcularROISimples(),
				CalcularROS(),
				CalcularTicketMedio(),
				# Métricas de performance
				CalcularWinRate(),
				CalcularPipelineVelocity(),
				CalcularProdutividadeRep(),
				CalcularConversaoFunil(),
				# Novas métricas financeiras avançadas
				CalcularMagicNumber(),
				CalcularPaybackPeriod(),
				CalcularMargemBruta(),
				CalcularMetaAchievement(),
				CalcularROAS(),
				# Novas métricas de funil e produtividade
				CalcularConversoesFunilDetalhado(),
				CalcularProdutividadeDetalhada(),
				CalcularChurnEstimado()
			],
			verbose=True
		)

	@agent
	def business_analyst_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['business_analyst_agent'],
			tools=[
				LerDadosCSV(),
				GerarBenchmarkSetor(), 
				DetectarOutliers(), 
				AnaliseSPICED(),
				SalvarRelatorioAgente()
			],
			verbose=True
		)

	@agent
	def alert_monitor_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['alert_monitor_agent'],
			tools=[LerDadosCSV(), GerarAlertas(), SalvarRelatorioAgente()],
			verbose=True
		)

	@agent
	def visualization_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['visualization_agent'],
			tools=[LerDadosCSV(), CriarGraficosPerformance(), GerarPlanilhaDiagnostico(), SalvarRelatorioAgente()],
			verbose=True
		)

	@agent
	def dashboard_creator_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['dashboard_creator_agent'],
			tools=[LerDadosCSV(), CriarDashboardSpecs(), SalvarRelatorioAgente()],
			verbose=True
		)

	@agent
	def report_generator_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['report_generator_agent'],
			tools=[LerDadosCSV(), ExportarRelatorioMD(), SalvarRelatorioAgente()],
			verbose=True
		)

	@task
	def collect_and_validate_data_task(self) -> Task:
		return Task(
			config=self.tasks_config['collect_and_validate_data_task'],
			agent=self.data_collector_agent()
		)

	@task
	def apply_data_governance_task(self) -> Task:
		return Task(
			config=self.tasks_config['apply_data_governance_task'],
			agent=self.data_governance_agent(),
			context=[self.collect_and_validate_data_task()]
		)

	@task
	def calculate_all_metrics_task(self) -> Task:
		return Task(
			config=self.tasks_config['calculate_all_metrics_task'],
			agent=self.metrics_calculator_agent(),
			context=[self.apply_data_governance_task()],
			dependencies=[self.apply_data_governance_task()]
		)

	@task
	def analyze_business_insights_task(self) -> Task:
		return Task(
			config=self.tasks_config['analyze_business_insights_task'],
			agent=self.business_analyst_agent(),
			context=[self.calculate_all_metrics_task()],
			dependencies=[self.calculate_all_metrics_task()]
		)

	@task
	def configure_monitoring_alerts_task(self) -> Task:
		return Task(
			config=self.tasks_config['configure_monitoring_alerts_task'],
			agent=self.alert_monitor_agent(),
			context=[self.analyze_business_insights_task()]
		)

	@task
	def create_visualizations_task(self) -> Task:
		return Task(
			config=self.tasks_config['create_visualizations_task'],
			agent=self.visualization_agent(),
			context=[self.analyze_business_insights_task(), self.configure_monitoring_alerts_task()]
		)

	@task
	def create_dashboard_prototype_task(self) -> Task:
		return Task(
			config=self.tasks_config['create_dashboard_prototype_task'],
			agent=self.dashboard_creator_agent(),
			context=[self.create_visualizations_task()]
		)

	@task
	def generate_executive_report_task(self) -> Task:
		return Task(
			config=self.tasks_config['generate_executive_report_task'],
			agent=self.report_generator_agent(),
			context=[self.create_visualizations_task(), self.create_dashboard_prototype_task(), self.configure_monitoring_alerts_task()]
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Diagnóstico Comercial Voga.IA crew"""
		agents = [
			self.data_collector_agent(),
			self.data_governance_agent(),
			self.metrics_calculator_agent(),
			self.business_analyst_agent(),
			self.alert_monitor_agent(),
			self.visualization_agent(),
			self.dashboard_creator_agent(),
			self.report_generator_agent()
		]
		tasks = [
			self.collect_and_validate_data_task(),
			self.apply_data_governance_task(),
			self.calculate_all_metrics_task(),
			self.analyze_business_insights_task(),
			self.configure_monitoring_alerts_task(),
			self.create_visualizations_task(),
			self.create_dashboard_prototype_task(),
			self.generate_executive_report_task()
		]
		return Crew(
			agents=agents,
			tasks=tasks,
			process=Process.sequential,
			verbose=True,
			memory=True,
			share_crew=True,
			max_iter=3
		)
