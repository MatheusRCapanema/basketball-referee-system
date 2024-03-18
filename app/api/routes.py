from flask import Blueprint
from flask_restful import Resource, reqparse, Api

from app.game.clock import GameClock

game_clock = GameClock()


class TimeManagement(Resource):
    # Método GET atualizado para usar get_time
    def get(self):
        return {"running": game_clock.is_running, "time": game_clock.get_time()}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('action', type=str, help='Ação para o relógio de jogo (start, stop, set)')
        parser.add_argument('minutes', type=int, help='Minutos para configurar', required=False)
        parser.add_argument('seconds', type=int, help='Segundos para configurar', required=False)
        args = parser.parse_args()

        action = args['action']
        minutes = args.get('minutes', 0)  # Padrão para 0 se não fornecido
        seconds = args.get('seconds', 0)  # Padrão para 0 se não fornecido

        if action == 'start':
            message = game_clock.start()
        elif action == 'stop':
            message = game_clock.stop()
        elif action == 'set':
            message = game_clock.set_time(minutes, seconds)
        else:
            message = "Ação desconhecida."

        return {"message": message, "data": {"running": game_clock.is_running, "time": game_clock.get_time()}}


class TempoDecorrido(Resource):
    def get(self):
        return {"running": game_clock.is_running, "time": game_clock.get_time_total()}


# Configure suas rotas aqui.
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(TimeManagement, '/time-management')
api.add_resource(TempoDecorrido, '/tempo-decorrido')
