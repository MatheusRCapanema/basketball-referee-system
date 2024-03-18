from flask import Flask, redirect, url_for
from flask_restful import Api
from app.api import TimeManagement
from flask_swagger_ui import get_swaggerui_blueprint
from flask import send_from_directory

from app.api.routes import TempoDecorrido

app = Flask(__name__)
api = Api(app)

# Configurar Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/swagger/swagger.yaml'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Basketball Referee System API"}
)
app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

# Adicionar recursos à API
api.add_resource(TimeManagement, '/time-management')
api.add_resource(TempoDecorrido, '/tempo-decorrido')


# Rota raiz
@app.route('/')
def welcome():
    # Opção 1: Retornar uma mensagem de boas-vindas return "Bem-vindo à API do Sistema de Gerenciamento do Árbitro de
    # Basquete. Acesse /swagger para a documentação da API."

    # Opção 2: Redirecionar para a documentação Swagger
    return redirect(url_for('swagger_ui.show'))


@app.route('/swagger/swagger.yaml')
def serve_swagger_yaml():
    return send_from_directory('swagger', 'swagger.yaml')


if __name__ == '__main__':
    app.run(debug=True)
