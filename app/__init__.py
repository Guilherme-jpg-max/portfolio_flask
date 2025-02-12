from flask import Flask
from flask_mail import Mail

mail = Mail()


def create_app():
    app = Flask(__name__, static_folder='static')

    # Carregar configurações do arquivo config.py
    app.config.from_pyfile('../config.py')

    mail.init_app(app)

    # Importar e registrar as rotas
    from . import routes
    app.register_blueprint(routes.bp)

    return app
