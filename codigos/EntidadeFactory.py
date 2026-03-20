# Design Pattern: classe responsavel por gerar as entidades
from codigos.Fundo import Fundo


class EntidadeFactory:
    # classe não tem um metodo construtor

    @staticmethod
    def get_entidade(nome_entidade:str):

        match nome_entidade:
            case 'Fundo1':
                return Fundo('Fase1',(0,0))

            case 'Fundo2':
                return Fundo('Fase2',(0,0))
