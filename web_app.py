#!/usr/bin/env python3
"""
Aplicação Web Completa - Diagnóstico Comercial Voga.IA
Sistema com login, dashboards interativos e visualização de métricas
"""

import os
import sys
import json
import pandas as pd
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import plotly.graph_objs as go
import plotly.utils
from plotly.subplots import make_subplots

# Carregar variáveis de ambiente
load_dotenv()

# Adicionar o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Configuração da aplicação Flask
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'voga-ia-secret-key-2025')

# Configuração do Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Simulação de banco de dados de usuários (em produção, usar banco real)
users_db = {
    'admin@vogaia.com': {
        'password': generate_password_hash('admin123'),
        'name': 'Administrador',
        'role': 'admin'
    },
    'user@vogaia.com': {
        'password': generate_password_hash('user123'),
        'name': 'Usuário Padrão',
        'role': 'user'
    }
}

class User(UserMixin):
    def __init__(self, email, name, role):
        self.id = email
        self.email = email
        self.name = name
        self.role = role

@login_manager.user_loader
def load_user(user_id):
    if user_id in users_db:
        user_data = users_db[user_id]
        return User(user_id, user_data['name'], user_data['role'])
    return None

def load_metrics_data():
    """Carrega dados das métricas do CSV"""
    try:
        df = pd.read_csv('src/diagnostico_comercial_voga_ia/data/metricas_calculadas.csv')
        return df
    except Exception as e:
        print(f"Erro ao carregar métricas: {e}")
        return pd.DataFrame()

def load_input_data():
    """Carrega dados de entrada do CSV"""
    try:
        df = pd.read_csv('src/diagnostico_comercial_voga_ia/data/dados_entrada.csv')
        return df
    except Exception as e:
        print(f"Erro ao carregar dados de entrada: {e}")
        return pd.DataFrame()

def create_dashboard_charts():
    """Cria gráficos para o dashboard"""
    df = load_metrics_data()
    if df.empty:
        return {}
    
    charts = {}
    
    # Gráfico 1: Métricas Financeiras
    financeiras = df[df['categoria'] == 'Financeira']
    if not financeiras.empty:
        fig1 = go.Figure(data=[
            go.Bar(
                x=financeiras['metrica'],
                y=financeiras['valor'],
                text=[f"R$ {v:,.0f}" for v in financeiras['valor']],
                textposition='auto',
                marker_color=['green' if s == 'excelente' else 'orange' if s == 'bom' else 'red' for s in financeiras['status']]
            )
        ])
        fig1.update_layout(
            title='Métricas Financeiras',
            xaxis_title='Métrica',
            yaxis_title='Valor (R$)',
            height=400
        )
        charts['financeiras'] = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    
    # Gráfico 2: Funil de Vendas
    funil = df[df['categoria'] == 'Funil']
    if not funil.empty:
        fig2 = go.Figure(data=[
            go.Funnel(
                y=funil['metrica'],
                x=funil['valor'],
                textinfo="value+percent initial"
            )
        ])
        fig2.update_layout(
            title='Funil de Vendas',
            height=400
        )
        charts['funil'] = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    
    # Gráfico 3: Performance por Categoria
    categorias = df.groupby('categoria')['valor'].mean().reset_index()
    fig3 = go.Figure(data=[
        go.Pie(
            labels=categorias['categoria'],
            values=categorias['valor'],
            hole=0.3
        )
    ])
    fig3.update_layout(
        title='Distribuição por Categoria',
        height=400
    )
    charts['categorias'] = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    
    return charts

# Rotas da aplicação

@app.route('/')
def index():
    """Página inicial"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Página de login"""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if email in users_db and check_password_hash(users_db[email]['password'], password):
            user = User(email, users_db[email]['name'], users_db[email]['role'])
            login_user(user)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Email ou senha incorretos!', 'error')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    """Logout do usuário"""
    logout_user()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    """Dashboard principal"""
    df = load_metrics_data()
    charts = create_dashboard_charts()
    
    # Estatísticas resumidas
    stats = {
        'total_metricas': len(df),
        'metricas_excelentes': len(df[df['status'] == 'excelente']),
        'metricas_atencao': len(df[df['status'] == 'atencao']),
        'metricas_criticas': len(df[df['status'] == 'critico'])
    }
    
    return render_template('dashboard.html', 
                         metrics=df.to_dict('records'), 
                         charts=charts, 
                         stats=stats)

@app.route('/metrics')
@login_required
def metrics():
    """Página detalhada de métricas"""
    df = load_metrics_data()
    return render_template('metrics.html', metrics=df.to_dict('records'))

@app.route('/reports')
@login_required
def reports():
    """Página de relatórios"""
    reports_dir = 'src/diagnostico_comercial_voga_ia/outputs'
    reports = []
    
    if os.path.exists(reports_dir):
        for file in os.listdir(reports_dir):
            if file.endswith('.md'):
                file_path = os.path.join(reports_dir, file)
                timestamp = os.path.getmtime(file_path)
                reports.append({
                    'name': file.replace('_', ' ').replace('.md', ''),
                    'file': file,
                    'date': datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')
                })
    
    return render_template('reports.html', reports=reports)

@app.route('/report/<filename>')
@login_required
def view_report(filename):
    """Visualizar relatório específico"""
    report_path = f'src/diagnostico_comercial_voga_ia/outputs/{filename}'
    
    if os.path.exists(report_path):
        with open(report_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return render_template('view_report.html', content=content, filename=filename)
    else:
        flash('Relatório não encontrado!', 'error')
        return redirect(url_for('reports'))

@app.route('/run_diagnosis')
@login_required
def run_diagnosis():
    """Executar diagnóstico completo"""
    try:
        # Importar e executar o diagnóstico
        from diagnostico_comercial_voga_ia.main import main
        main()
        flash('Diagnóstico executado com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao executar diagnóstico: {str(e)}', 'error')
    
    return redirect(url_for('dashboard'))

@app.route('/api/metrics')
@login_required
def api_metrics():
    """API para dados das métricas"""
    df = load_metrics_data()
    return jsonify(df.to_dict('records'))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080) 