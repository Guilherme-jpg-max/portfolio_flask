import re
from flask_mail import Message
from flask import flash


# Função para validar e-mail
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


# Função para processar o formulário de contato
def process_contact_form(request, mail, os):
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    message = request.form.get('message', '').strip()

    if not name or not email or not message:
        flash("Por favor, preencha todos os campos.", 'error')
        return False, None

    if not is_valid_email(email):
        flash("E-mail inválido. Por favor, insira um e-mail válido.", 'error')
        return False, None

    try:
        msg = Message(
            subject=f"Nova mensagem de {name}",
            sender=os.getenv('MAIL_DEFAULT_SENDER'),
            recipients=[os.getenv('MAIL_USERNAME')],
            body=f"Nome: {name}\nE-mail: {email}\n\nMensagem:\n{message}"
        )
        # Adiciona o campo Reply-To para que as respostas sejam direcionadas ao meu e-mail
        msg.reply_to = email

        return True, msg 

    except Exception as e:
        print(f"Erro ao processar o formulário: {e}")
        flash("Ocorreu um erro ao enviar a mensagem. Tente novamente mais tarde.", 'error')
        return False, None