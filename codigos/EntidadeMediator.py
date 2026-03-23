# classe para gerenciar as interaçoes das outras classes: (colisões)
from codigos.Constantes import TELA_ALTURA
from codigos.Entidade import Entidade
from codigos.Inimigo import Inimigo
from codigos.Jogador import Jogador
from codigos.TiroInimigo import TiroInimigo
from codigos.TiroJogador import TiroJogador


class EntidadeMediator:

    @staticmethod
    def __verificar_colisao_window(ent: Entidade):# verificar se passou o limite da tela
        if isinstance(ent,Inimigo):
            if ent.rect.bottom > TELA_ALTURA + 70:
                ent.vida = 0
        if isinstance(ent, TiroJogador):
            if ent.rect.bottom < 0:
                ent.vida = 0
        if isinstance(ent,TiroInimigo):
            if ent.rect.bottom > TELA_ALTURA + 70:
                ent.vida = 0

    @staticmethod
    def __verificar_colisao_entidade(ent1, ent2):
        valida_interacao = False
        # certificando que as colisoes ocorra somente entre tiros e jogadores ou inimigos
        if isinstance(ent1, Inimigo) and isinstance(ent2,TiroJogador):
            valida_interacao = True
        elif isinstance(ent1, TiroJogador) and isinstance(ent2, Inimigo):
            valida_interacao = True
        elif isinstance(ent1, Jogador) and isinstance(ent2, TiroInimigo):
            valida_interacao = True
        elif isinstance(ent1, TiroInimigo) and isinstance(ent2, Jogador):
            valida_interacao = True

        if valida_interacao:
            # veridicando as colisões de fato
            if (ent1.rect.right >= ent2.rect.left and
                ent1.rect.left <= ent2.rect.right and
                ent1.rect.bottom >= ent2.rect.top and
                ent1.rect.top <= ent2.rect.bottom):
                ent1.vida -= ent2.dano
                ent2.vida -= ent1.dano
                ent1.ultimo_dmg = ent2.nome
                ent2.ultimo_dmg = ent1.nome






    @staticmethod
    def verificar_colisao(entidade_lista: list[Entidade]):
        for i in  range(len(entidade_lista)):
            entidade1 = entidade_lista[i]
            EntidadeMediator.__verificar_colisao_window(entidade1)
            # i+1 dentro do range para nao fazer comparações redundantes
            for j in range(i+1,len(entidade_lista)):
                entidade2 = entidade_lista[j]
                EntidadeMediator.__verificar_colisao_entidade(entidade1,entidade2)
    # metodo para destruir objeto(Inimigo) se acabar a vida
    @staticmethod
    def verificar_vida(entidade_lista: list[Entidade]):
        for ent in entidade_lista:
            if ent.vida <= 0:
                entidade_lista.remove(ent)
