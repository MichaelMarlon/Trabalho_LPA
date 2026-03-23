# Design Pattern: classe responsavel por gerar as entidades
import random

from codigos.Constantes import TELA_LARGURA
from codigos.Fundo import Fundo
from codigos.Inimigo import Inimigo
from codigos.Jogador import Jogador


class EntidadeFactory:
    # classe não tem um metodo construtor

    @staticmethod
    def get_entidade(nome_entidade:str):

        match nome_entidade:
            case 'Fase1':
                return Fundo('Fase1',(0,0))

            case 'Fase2':
                return Fundo('Fase2',(0,0))

            case 'Jogador1':
                return Jogador('Jogador1',(TELA_LARGURA/2-30,447))
            case 'Jogador2':
                return Jogador('Jogador2', (TELA_LARGURA / 2+30, 430))
            case 'Inimigo1':
                return Inimigo('Inimigo1',(random.randint(30,TELA_LARGURA-30),-10))
            case 'Inimigo2':
                return Inimigo('Inimigo2', (random.randint(30, TELA_LARGURA-30), -10))

