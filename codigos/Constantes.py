import pygame
#A
ATRASO_ENTIDADE_TIRO = {
    'Jogador1': 20,
    'Jogador2': 15,
    'Inimigo1': 100,
    'Inimigo2': 200,

}
#C
COR_LARANJA = (255,128,0)
COR_PRETA = (0,0,0)
COR_BRANCA = (255,255,255)
COR_AMARELA = (255,255,0)
COR_AZUL = (0,0,255)
COR_VERDE =(0,128,0)
COR_CIANO = (0,128,128)
#D
DANO_ENTIDADE = {
    'Fundo': 0,
    'Fase1': 0,
    'Fase2': 0,
    'Jogador1': 1,
    'Jogador2': 1,
    'TiroJogador1': 25,
    'TiroJogador2': 25,
    'Inimigo1': 1,
    'Inimigo2': 1,
    'TiroInimigo1': 15,
    'TiroInimigo2': 20,

}
#E
EVENTO_INIMIGO = pygame.USEREVENT +1
#F

#J
JOGADOR_CIMA ={
    'Jogador1': pygame.K_UP,
    'Jogador2': pygame.K_w
}
JOGADOR_BAIXO = {
    'Jogador1': pygame.K_DOWN,
    'Jogador2': pygame.K_s
}
JOGADOR_ESQUERDA = {
    'Jogador1': pygame.K_LEFT,
    'Jogador2': pygame.K_a
}
JOGADOR_DIREITA = {
    'Jogador1': pygame.K_RIGHT,
    'Jogador2': pygame.K_d
}
JOGADOR_TIRO = {
        'Jogador1':pygame.K_RCTRL,
        'Jogador2': pygame.K_LCTRL
}
#M
MENU_OPCAO = (
    'NOVO JOGO 1P',
    'NOVO JOGO 2P',
    'PONTUAÇÃO',
    'SAIR'
)
#P
PONTOS_ENTIDADE = {
    'Fundo': 0,
    'Fase1': 0,
    'Fase2': 0,
    'Jogador1': 0,
    'Jogador2': 0,
    'TiroJogador1': 0,
    'TiroJogador2': 0,
    'Inimigo1': 100,
    'Inimigo2': 100,
    'TiroInimigo1': 0,
    'TiroInimigo2': 0,
}

#T
TELA_ALTURA = 509
TELA_LARGURA = 900
TEMPO_EVENTO = pygame.USEREVENT + 2
TEMPO_FASE = 10000
#
VEL_ENTIDADE = {
    'Jogador1': 6,
    'Jogador2': 6,
    'Inimigo1': 1,
    'Inimigo2': 1,
    'TiroJogador1':3,
    'TiroJogador2': 3,
    'TiroInimigo1':5,
    'TiroInimigo2': 2,
}
PONTUACAO_POSICAO ={
    'Título':(TELA_LARGURA/2,50),
    'DigiteNome':(TELA_LARGURA/2,80),
    'Label': (TELA_LARGURA/2,90),
    'Nome':(TELA_LARGURA/2,110),
    0:(TELA_LARGURA/2,110),
    1:(TELA_LARGURA/2,130),
    2:(TELA_LARGURA/2,150),
    3:(TELA_LARGURA/2,170),
    4:(TELA_LARGURA/2,190),
    5:(TELA_ALTURA/2,210),
    6:(TELA_ALTURA/2,230),
    7:(TELA_ALTURA/2,250),
    8:(TELA_ALTURA/2,270),
    9:(TELA_ALTURA/2,290),
}
VIDA_ENTIDADE = {
    'Fundo': 999,
    'Fase1': 999,
    'Fase2': 999,
    'Jogador1': 200,
    'Jogador2': 200,
    'TiroJogador1':1,
    'TiroJogador2': 1,
    'Inimigo1': 50,
    'Inimigo2': 60,
    'TiroInimigo1': 1,
    'TiroInimigo2': 1
}