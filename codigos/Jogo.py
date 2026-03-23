from codigos.Constantes import TELA_LARGURA, TELA_ALTURA, MENU_OPCAO
from codigos.Menu import Menu

import pygame

from codigos.Fase import Fase


class Jogo:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(TELA_LARGURA, TELA_ALTURA))

    def run(self):

        while True:
            menu = Menu(self.window) # instanciando um objeto da classe Menu para implantantar o menu no jogo
            menu_return = menu.run() # variavel receberá o retorno do menu
            if menu_return in [MENU_OPCAO[0], MENU_OPCAO[1]]:
                pontos_jogadores = [0,0] # [Jogador1, Jogador2]
                fase = Fase(self.window,'Fase1',menu_return, pontos_jogadores)
                return_fase = fase.run(pontos_jogadores)
                if return_fase:
                    fase = Fase(self.window, 'Fase2', menu_return, pontos_jogadores)
                    return_fase = fase.run(pontos_jogadores)
            elif menu_return == MENU_OPCAO[3]:
                pygame.quit()  # fechando a janela
                quit()  # finalizando pygame
            else:
                pass


