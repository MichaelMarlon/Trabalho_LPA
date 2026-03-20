# Design Pattern: classe responsavel por gerar as entidades

class EntidadeFactory:
    # classe não tem um metodo construtor

    @staticmethod
    def get_entidade(nome_entidade:str, posicao=(0,0)):

        match nome_entidade:
            case 'Fase1':

            case 'Fase2':
                pass