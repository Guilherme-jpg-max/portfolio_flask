from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app import mail
from .forms import process_contact_form
import os
from .github_utils import get_github_repos

bp = Blueprint('main', __name__)

def get_repos():
    return get_github_repos()

@bp.route('/')
def index():
    repos = get_repos()
    return render_template('index.html', repos=repos, title="Home")

@bp.route('/projects')
def projects():
    repos = get_repos()
    return render_template('index.html', repos=repos, title="Projects", section='projects')


@bp.route('/about')
def about():
    return render_template('index.html', title="About Me", section='about')

@bp.route('/contact', methods=['POST'])
def contact():
    success, msg = process_contact_form(request, mail, os)
    if success:
        try:
            mail.send(msg)
            return jsonify({"success": True, "message": "Mensagem enviada com sucesso!"}), 200
        except Exception:
            return jsonify({"success": False, "message": "Ocorreu um erro ao enviar a mensagem. Tente novamente mais tarde."}), 500
    return jsonify({"success": False, "message": "Dados inválidos."}), 400

@bp.route('/skills')
def skills():
    return render_template('index.html', title="Skills", section='skills')