# classe para gerenciar as interaçoes das outras classes: (colisões)
from codigos.Entidade import Entidade
from codigos.Inimigo import Inimigo


class EntidadeMediator:

    @staticmethod
    def __verificar_colisao_window(ent: Entidade):# verificar se passou o limite da tela
        if isinstance(ent,Inimigo):
            pass


    @staticmethod
    def verificar_colisao(entidade_lista: list[Entidade]):
        for i in  range(len(entidade_lista)):
            teste_entidade = entidade_lista[i]
            EntidadeMediator.__verificar_colisao_window(teste_entidade)