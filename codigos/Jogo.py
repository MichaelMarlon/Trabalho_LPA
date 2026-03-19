from codigos.Constantes import TELA_LARGURA, TELA_ALTURA
from codigos.Menu import Menu

import pygame
class Jogo:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(TELA_LARGURA, TELA_ALTURA))

    def run(self):

        while True:
            menu = Menu(self.window) # instanciando um objeto da classe Menu para implantantar o menu no jogo
            menu.run()
            pass


        pass