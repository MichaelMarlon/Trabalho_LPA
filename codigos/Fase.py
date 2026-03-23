import random

import pygame

from codigos.EntidadeMediator import EntidadeMediator
from codigos.Constantes import MENU_OPCAO, EVENTO_INIMIGO
from codigos.Entidade import Entidade
from codigos.EntidadeFactory import EntidadeFactory
from codigos.Inimigo import Inimigo
from codigos.Jogador import Jogador


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
        pygame.time.set_timer(EVENTO_INIMIGO,2000) # setando tempo para um evento

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
                if isinstance(ent,(Jogador,Inimigo)):
                    tiro = ent.tiro()
                    # se a tecla de tiro for pressionada adiciona a entidade na lista
                    if tiro is not None:
                        self.lista_entidade.append(tiro)

            pygame.display.flip()
            # Colicões
            EntidadeMediator.verificar_colisao(entidade_lista=self.lista_entidade)
            EntidadeMediator.verificar_vida(entidade_lista=self.lista_entidade)
            # Conferido todos os eventos
            for event in pygame.event.get():
                # Evento de saida
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # Evento para instanciar inimigos
                if event.type == EVENTO_INIMIGO:
                    # variavel que escolherá entre o inimigo 1 ou 2
                    escolha = random.choice(('Inimigo1','Inimigo2'))
                    self.lista_entidade.append(EntidadeFactory.get_entidade(escolha))

