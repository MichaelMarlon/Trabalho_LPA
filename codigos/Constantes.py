import pygame
#C
COR_LARANJA = (255,128,0)
COR_PRETA = (0,0,0)
COR_BRANCA = (255,255,255)
COR_AMARELA = (255,255,0)
COR_AZUL = (0,0,255)

#E
EVENTO_INIMIGO = pygame.USEREVENT +1
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

#T
TELA_ALTURA = 509
TELA_LARGURA = 900

#V
VEL_ENTIDADE = {
    'Jogador1': 5,
    'Jogador2': 5,
    'Inimigo1': 2,
    'Inimigo2': 1
}