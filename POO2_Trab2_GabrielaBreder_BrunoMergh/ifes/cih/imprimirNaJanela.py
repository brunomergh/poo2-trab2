__author__ = 'Bruno'
import pygame,os


class ImprimirNaJanela:
    def __init__(self):
        self.fonte = pygame.font.SysFont("comicsansms",24) #define a fonte e o tamanho

    def imprime(self,janela,posicao,nome,x,y):
        file = os.path.split(os.path.abspath(__file__))[0]
        diretorio = file.replace("cci", "")
        self.file = os.path.join(diretorio, 'imagens', nome)
        self.imagem = pygame.image.load(self.file) # carrega a localizacao e a imagem
        self.imagem_redimensionada=pygame.transform.scale(self.imagem,(x,y)) # redimencionar
        #janela.screen.blit(self.imagem,(150,150)) # posicao (x,y)
        janela.screen.blit(self.imagem_redimensionada,posicao) # posicao (x,y)

    def imprime2(self,janela,posicao,nome):
        file = os.path.split(os.path.abspath(__file__))[0]
        self.imagem = pygame.image.load(self.file) # carrega a localizacao e a imagem
        janela.screen.blit(nome,posicao) # posicao (x,y)