__author__ = 'Bruno'

from ifes.cih.teclado import Teclado
from ifes.cci.control import Control
import pygame, sys

class ControleTelaInicial:


    def __init__(self):
        self.teclado = Teclado()
        self.posicao=[[0,0],[216,280],[144,280],[216,340],[216,400]]
        self.ctrl = Control()


    def controle(self, listaCadastral):


        print(listaCadastral)
        self.teclado.capturaTeclas()

        TelaInicial,TelaCadastro,TelaCadastroFunc,TelaRelatorio = 2,3,11,4
        opcao = TelaInicial
        papelparede,bcadastrar, seta, brelatorio, bsair = 0,1,2,3,4
        largura, altura = 0,1

        if self.teclado.teclas[self.teclado.letra] != "":
            print(self.teclado.teclas[self.teclado.letra])


        if self.teclado.teclas[self.teclado.cima] and self.posicao[seta][altura] > self.posicao[bcadastrar][altura]:
            print("subi")
            self.posicao[seta][altura] -= 60

        if self.teclado.teclas[self.teclado.baixo] and self.posicao[seta][altura] < self.posicao[bsair][altura]:
            print("desci")
            self.posicao[seta][altura] += 60

        cadastrar = (self.posicao[seta][altura] == self.posicao[bcadastrar][altura])
        relatorio = (self.posicao[seta][altura] == self.posicao[brelatorio][altura])
        sair = (self.posicao[seta][altura] == self.posicao[bsair][altura])
        log = 0

        if self.teclado.teclas[self.teclado.enter]:
            if cadastrar and listaCadastral[log] == 'admin':
                opcao = TelaCadastro

            elif cadastrar and listaCadastral[log] != 'admin':
                opcao = TelaCadastroFunc
                print("cadastrar")

            elif relatorio:
                opcao = TelaRelatorio
                #self.ctrl.controle(1,0)
                print("relatorio")

            elif sair:
                print("sair")
                pygame.quit()
                sys.exit()
                #self.ctrl.controle(3,0)
        return opcao, listaCadastral