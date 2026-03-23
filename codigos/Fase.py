import random

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from codigos.EntidadeMediator import EntidadeMediator
from codigos.Constantes import MENU_OPCAO, EVENTO_INIMIGO, COR_VERDE, COR_CIANO, TEMPO_EVENTO
from codigos.Entidade import Entidade
from codigos.EntidadeFactory import EntidadeFactory
from codigos.Inimigo import Inimigo
from codigos.Jogador import Jogador


class Fase:
    def __init__(self, window: Surface, nome:str, game_mode:str, pontos_jogadores:list[int]):
        self.timeout = 20000 # 20 segundos
        self.window = window
        self.nome = nome
        self.game_mode = game_mode
        self.lista_entidade: list[Entidade] = []
        self.lista_entidade.append(EntidadeFactory.get_entidade(self.nome))
        jogador = EntidadeFactory.get_entidade('Jogador1')
        jogador.pontos = pontos_jogadores[0]
        self.lista_entidade.append(jogador)
        if game_mode == MENU_OPCAO[1]:
            jogador = EntidadeFactory.get_entidade('Jogador2')
            jogador.pontos = pontos_jogadores[1]
            self.lista_entidade.append(jogador)
        pygame.time.set_timer(EVENTO_INIMIGO,2000) # setando tempo para um evento
        pygame.time.set_timer(TEMPO_EVENTO,100) # 100ms

    def run(self, pontos_jogadores:list[int]):
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
                if ent.nome == 'Jogador1':
                    self.texto_fase(25,f'Jogador1 - Vida: {ent.vida} | Pontos: {ent.pontos}',COR_VERDE,(10,10))
                if ent.nome == 'Jogador2':
                    self.texto_fase(25,f'Jogador2 - Vida: {ent.vida} | Pontos: {ent.pontos}',COR_CIANO,(10,30))
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
                if event.type == TEMPO_EVENTO:
                    #logica para mudar de fase
                    self.timeout -= 100
                    if self.timeout == 0:
                        for ent in self.lista_entidade:
                            if isinstance(ent, Jogador) and ent.nome == 'Jogador1':
                                pontos_jogadores[0] = ent.pontos
                            if isinstance(ent, Jogador) and ent.nome == 'Jogador2':
                                pontos_jogadores[1] = ent.pontos
                        return True
                busca_jogador = False
                for ent in self.lista_entidade:
                    if isinstance(ent, Jogador):
                        busca_jogador = True
                if not busca_jogador:
                    return False

    def texto_fase(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
