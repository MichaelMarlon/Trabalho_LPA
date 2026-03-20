from codigos import Entidade


class Fase:
    def __init__(self, window, nome, game_mode):
        self.window = window
        self.nome = nome
        self.game_mode = game_mode
        self.lista_entidade: list[Entidade] = []

    def run(self):
        pass