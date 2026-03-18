from codigos.Menu import Menu

import pygame
class Jogo:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(900, 600))

    def run(self):
        while True:
            menu = Menu(self.window) # instanciando um objeto da classe Menu para implantantar o menu no jogo
            menu.run()
            pass

            # # checando todos os eventos
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()  # fechando a janela
            #         quit()  # finalizando pygame
        pass