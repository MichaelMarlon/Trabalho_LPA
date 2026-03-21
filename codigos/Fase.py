import pygame

from codigos.Constantes import MENU_OPCAO
from codigos.Entidade import Entidade
from codigos.EntidadeFactory import EntidadeFactory


class Fase:
    def __init__(self, window, nome, game_mode):
        self.window = window
        self.nome = nome
        self.game_mode = game_mode
        self.lista_entidade: list[Entidade] = []
        self.lista_entidade.append(EntidadeFactory.get_entidade('Fundo1'))
        self.lista_entidade.append(EntidadeFactory.get_entidade('Jogador1'))
        if game_mode == MENU_OPCAO[1]:
            self.lista_entidade.append(EntidadeFactory.get_entidade('Jogador2'))


    def run(self):
        pygame.mixer_music.load(f'./asset/{self.nome}.mp3')
        pygame.mixer_music.play(-1)
        # usado para o programa rodar em uma taxa de atualizaçao especifica
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)# informando o numero de
            # loop para inserir cada imagem da lista lista_entidade
            for ent in self.lista_entidade:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

