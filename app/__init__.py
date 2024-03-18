from flask import Flask, redirect, url_for
from flask import current_app
from app.api.routes import api_bp
from flask_swagger_ui import get_swaggerui_blueprint
from flask import send_from_directory

def create_app():
    app = Flask(__name__)

    # Configurar Swagger UI
    SWAGGER_URL = '/swagger'
    API_URL = '/swagger/swagger.yaml'
    SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "Basketball Referee System API"}
    )
    app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

    # Registrar o Blueprint da API
    app.register_blueprint(api_bp, url_prefix='/api')

    # Rota raiz para redirecionar para a documentação Swagger
    @app.route('/')
    def welcome():
        return redirect(url_for('swagger_ui.show'))

    # Rota para servir o arquivo swagger.yaml
    @app.route('/swagger/swagger.yaml')
    def serve_swagger_yaml():
        return send_from_directory(current_app.root_path + '/swagger', 'swagger.yaml')

    return app
