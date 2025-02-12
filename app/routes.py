from flask import Blueprint, render_template, request, jsonify, send_file
from app import mail
from .forms import process_contact_form
import os
from .github_utils import get_github_repos


bp = Blueprint('main', __name__)

# Função para obter repositórios do GitHub com tratamento de erro
def get_repos():
    try:
        return get_github_repos()
    except Exception as e:
        print(f"Erro ao buscar repositórios: {e}")
        return []


# Função para renderizar templates com repositórios
def render_templates(template_name, **context):
    repos = get_repos()
    return render_template(template_name, repos=repos, **context)


# Rota principal (Home)
@bp.route('/')
def index():
    return render_templates('index.html', title="Portfólio Guilherme Carlos")


# Rota para a seção de Projetos
@bp.route('/projects')
def projects():
    return render_templates('index.html', title="Projects", section='projects')


# Rota para a seção "Sobre mim"
@bp.route('/about')
def about():
    return render_templates('index.html', title="About Me", section='about')


# Rota para o envio do formulário de contato
@bp.route('/contact', methods=['POST'])
def contact():
    # Validação e processamento do formulário de contato
    success, msg = process_contact_form(request, mail, os)
    
    if success:
        try:
            mail.send(msg)
            return jsonify({"success": True, "message": "Mensagem enviada com sucesso!"}), 200
        except Exception:
            return jsonify({"success": False, "message": "Ocorreu um erro ao enviar a mensagem. Tente novamente mais tarde."}), 500
    return jsonify({"success": False, "message": "Dados inválidos."}), 400


# Rota para a seção de Skills
@bp.route('/skills')
def skills():
    return render_templates('index.html', title="Skills", section='skills')

@bp.route('/curriculo')
def baixar_curriculo():
    return send_file('static/curriculo/curriculo.pdf', mimetype='application/pdf', as_attachment=False)