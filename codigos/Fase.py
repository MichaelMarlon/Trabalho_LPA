import pygame

from codigos import Entidade
from codigos.EntidadeFactory import EntidadeFactory


class Fase:
    def __init__(self, window, nome, game_mode):
        self.window = window
        self.nome = nome
        self.game_mode = game_mode
        self.lista_entidade: list[Entidade] = []
        self.fundo1 = EntidadeFactory.get_entidade('Fundo1')

    def run(self):
        while True:
            self.window.blit(source=self.fundo1.surf,dest=self.fundo1.rect)
            pygame.display.flip()

