from __future__ import annotations
from abc import ABC, abstractmethod

from ImpressoraLaser import ImpressoraLaser
from ImpressoraJatoDeTinta import ImpressoraJatoDeTinta

class FabricaDeImpressoraMixin(ABC):
  @abstractmethod
  def criarImpressaLaser(self) -> ImpressoraLaser:
    pass
  @abstractmethod
  def criarImpressoraJatoDeTinta(self) -> ImpressoraJatoDeTinta:
    pass