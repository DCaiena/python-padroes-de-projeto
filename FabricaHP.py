
from ImpressoraLaserHP import ImpressoraLaserHP
from ImpressoraJatoDeTintaHP import ImpressoraJatoDeTintaHP
from FabricaDeImpressoraMixin import FabricaDeImpressoraMixin
from ImpressoraLaser import ImpressoraLaser
from ImpressoraJatoDeTinta import ImpressoraJatoDeTinta

class FabricaHP(FabricaDeImpressoraMixin):
  def criarImpressaLaser(self) -> ImpressoraLaser:
    return ImpressoraLaserHP()
  def criarImpressoraJatoDeTinta(self) -> ImpressoraJatoDeTinta:
    return ImpressoraJatoDeTintaHP()
