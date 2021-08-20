from __future__ import annotations
import random
from abc import ABC, abstractmethod
from typing import List
from CriadorDeFabrica import CriadorDeFabrica

class CentralPrint:
    _instancia = None
    impressorasDisponiveis = []
    def __init__(self):
      pass

    @classmethod
    def getInstancia(cls):
      if cls._instancia is None:
        cls._instancia = cls()
      return cls._instancia
     
    def gerarImpressora(self,fabrica ):
      impressoraLaser = fabrica.criarImpressaLaser()
      impressoraJatoDeTinta = fabrica.criarImpressoraJatoDeTinta()
      return [impressoraLaser, impressoraJatoDeTinta]

    def criacao(self):
      fab = CriadorDeFabrica()
      print('### Gerando fabricas')
      fabEpson = fab.criarFabrica('epson')
      fabHP = fab.criarFabrica('hp')
      print('### Gerando Impressoras')
      self.salvaImpressoras( (self.gerarImpressora(fabHP) + self.gerarImpressora(fabEpson)) )
      print('Impressoras criadas e disponíveis para uso')
      return 0

    def salvaImpressoras(self, impressoras = [] ):
      self.impressorasDisponiveis=  self.impressorasDisponiveis +impressoras
    
    def enviarParaImpressao(self, valor=''):
      print('Imprimindo')
      impressoraAleatoria = random.choice(self.impressorasDisponiveis) 
      impressoraAleatoria.imprimir(valor)
      # impressoraAleatoria[index ].print(valor)
    def testarImpressorasDisponiveis(self):
      for impressora in self.impressorasDisponiveis:
        impressora.imprimir()
      print('Quantidade de impressoras ',  len(self.impressorasDisponiveis))
      return 0

