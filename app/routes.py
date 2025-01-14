from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import mail
from .forms import process_contact_form
import os
from .github_utils import get_github_repos

bp = Blueprint('main', __name__)


@bp.route('/')
def home():
    repos = get_github_repos()
    return render_template('home.html', repos=repos)


@bp.route('/about')
def about():
    return render_template('about.html')


@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        success, msg = process_contact_form(request, mail, os)
        # Se o processamento do formulário foi bem-sucedido
        if success:
            try:
                mail.send(msg)
                flash("Mensagem enviada com sucesso!", 'success')
                return redirect(url_for('main.home'))

            except Exception as e:
                # Em caso de erro no envio do e-mail
                print(f"Erro ao enviar e-mail: {e}")
                flash("Ocorreu um erro ao enviar a mensagem. Tente novamente mais tarde.", 'error')
                return render_template('contact.html')

        # Caso tenha falhado na validação ou no processamento do formulário
        return render_template('contact.html')

    return render_template('contact.html')


@bp.route('/projects')
def projects():
    repos = get_github_repos()
    return render_template('projects.html', repos=repos)


@bp.route('/skills')
def skills():
    return render_template('skills_me.html')

