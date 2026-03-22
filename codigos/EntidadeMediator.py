# classe para gerenciar as interaçoes das outras classes: (colisões)
from codigos.Constantes import TELA_ALTURA
from codigos.Entidade import Entidade
from codigos.Inimigo import Inimigo
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


    @staticmethod
    def verificar_colisao(entidade_lista: list[Entidade]):
        for i in  range(len(entidade_lista)):
            teste_entidade = entidade_lista[i]
            EntidadeMediator.__verificar_colisao_window(teste_entidade)
    # metodo para destruir objeto(Inimigo) se acabar a vida
    @staticmethod
    def verificar_vida(entidade_lista: list[Entidade]):
        for ent in entidade_lista:
            if ent.vida <= 0:
                entidade_lista.remove(ent)
