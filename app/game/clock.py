from threading import Thread
import time


class GameClock:
    def __init__(self):
        self.is_running = False
        self.game_time_seconds = 1200  # 20 minutos convertidos em segundos
        self.game_real_time = 0
        self.iniciado = False
        # Inicia a thread de tempo total assim que a classe é instanciada
        self.thread2 = Thread(target=self.increment_time)
        self.thread2.start()

    def start(self):
        if not self.is_running:
            self.is_running = True
            if not self.iniciado:
                self.iniciado = True
                thread = Thread(target=self.decrement_time)
                thread.start()
            return "Relógio iniciado."
        else:
            return "Relógio já está rodando."

    def stop(self):
        self.is_running = False
        return "Relógio parado."

    def set_time(self, minutes, seconds):
        self.game_time_seconds = minutes * 60 + seconds
        return f"Tempo de jogo configurado para {minutes} minutos e {seconds} segundos."

    def decrement_time(self):
        while self.is_running and self.game_time_seconds > 0:
            time.sleep(1)
            self.game_time_seconds -= 1

    def increment_time(self):
        while not self.iniciado:
            time.sleep(1)  # Espera até o jogo ser iniciado
        while self.game_time_seconds > 0:
            time.sleep(1)
            self.game_real_time += 1

    def get_time(self):
        minutes, seconds = divmod(self.game_time_seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"

    def get_time_total(self):
        minutes, seconds = divmod(self.game_real_time, 60)
        return f"{minutes:02d}:{seconds:02d}"
