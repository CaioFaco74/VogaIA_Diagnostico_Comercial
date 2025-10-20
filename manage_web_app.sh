#!/bin/bash

# Script de gerenciamento da aplicação web Voga.IA
# Uso: ./manage_web_app.sh [start|stop|status|restart]

APP_NAME="Voga.IA Web App"
PORT=8080
PID_FILE="/tmp/voga_ia_web.pid"

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para imprimir mensagens coloridas
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Função para verificar se a porta está em uso
check_port() {
    if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null 2>&1; then
        return 0
    else
        return 1
    fi
}

# Função para obter PID do processo
get_pid() {
    lsof -ti :$PORT 2>/dev/null
}

# Função para verificar status
status() {
    print_status "Verificando status da $APP_NAME..."
    
    if check_port; then
        PID=$(get_pid)
        print_success "$APP_NAME está rodando (PID: $PID, Porta: $PORT)"
        print_status "Acesse: http://localhost:$PORT"
    else
        print_warning "$APP_NAME não está rodando"
    fi
}

# Função para parar a aplicação
stop() {
    print_status "Parando $APP_NAME..."
    
    if check_port; then
        PID=$(get_pid)
        print_status "Matando processo $PID..."
        kill -TERM $PID 2>/dev/null
        
        # Aguardar até 10 segundos para o processo terminar
        for i in {1..10}; do
            if ! check_port; then
                print_success "$APP_NAME parado com sucesso"
                return 0
            fi
            sleep 1
        done
        
        # Se ainda estiver rodando, forçar parada
        PID=$(get_pid)
        if [ ! -z "$PID" ]; then
            print_warning "Forçando parada do processo $PID..."
            kill -KILL $PID 2>/dev/null
            print_success "$APP_NAME parado forçadamente"
        fi
    else
        print_warning "$APP_NAME não estava rodando"
    fi
}

# Função para iniciar a aplicação
start() {
    print_status "Iniciando $APP_NAME..."
    
    if check_port; then
        print_warning "$APP_NAME já está rodando na porta $PORT"
        status
        return 1
    fi
    
    # Verificar se o ambiente virtual existe
    if [ ! -d "venv-python312" ]; then
        print_error "Ambiente virtual não encontrado!"
        print_status "Execute: python3 -m venv venv-python312"
        return 1
    fi
    
    # Verificar se o arquivo web_app.py existe
    if [ ! -f "web_app.py" ]; then
        print_error "Arquivo web_app.py não encontrado!"
        return 1
    fi
    
    # Ativar ambiente virtual e iniciar aplicação
    print_status "Ativando ambiente virtual..."
    source venv-python312/bin/activate
    
    print_status "Iniciando aplicação na porta $PORT..."
    nohup python web_app.py > /tmp/voga_ia_web.log 2>&1 &
    
    # Aguardar um pouco para verificar se iniciou
    sleep 3
    
    if check_port; then
        PID=$(get_pid)
        echo $PID > $PID_FILE
        print_success "$APP_NAME iniciado com sucesso (PID: $PID)"
        print_status "Acesse: http://localhost:$PORT"
        print_status "Logs: tail -f /tmp/voga_ia_web.log"
    else
        print_error "Falha ao iniciar $APP_NAME"
        print_status "Verifique os logs: cat /tmp/voga_ia_web.log"
        return 1
    fi
}

# Função para reiniciar a aplicação
restart() {
    print_status "Reiniciando $APP_NAME..."
    stop
    sleep 2
    start
}

# Função para mostrar logs
logs() {
    if [ -f "/tmp/voga_ia_web.log" ]; then
        print_status "Mostrando logs da $APP_NAME..."
        tail -f /tmp/voga_ia_web.log
    else
        print_warning "Arquivo de log não encontrado"
    fi
}

# Função para mostrar ajuda
show_help() {
    echo "Uso: $0 [comando]"
    echo ""
    echo "Comandos disponíveis:"
    echo "  start     - Iniciar a aplicação web"
    echo "  stop      - Parar a aplicação web"
    echo "  restart   - Reiniciar a aplicação web"
    echo "  status    - Verificar status da aplicação"
    echo "  logs      - Mostrar logs em tempo real"
    echo "  help      - Mostrar esta ajuda"
    echo ""
    echo "Exemplos:"
    echo "  $0 start"
    echo "  $0 status"
    echo "  $0 stop"
}

# Verificar argumentos
case "${1:-}" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        restart
        ;;
    status)
        status
        ;;
    logs)
        logs
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        print_error "Comando inválido: $1"
        echo ""
        show_help
        exit 1
        ;;
esac 