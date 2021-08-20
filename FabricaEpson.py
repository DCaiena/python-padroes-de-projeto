from ImpressoraLaserEpson import ImpressoraLaserEpson 
from ImpressoraJatoDeTintaEpson import ImpressoraJatoDeTintaEpson
from FabricaDeImpressoraMixin import FabricaDeImpressoraMixin
from ImpressoraJatoDeTinta import ImpressoraJatoDeTinta
from ImpressoraLaser import ImpressoraLaser

class FabricaEpson(FabricaDeImpressoraMixin):
  def criarImpressaLaser(self) -> ImpressoraLaser:
    return ImpressoraLaserEpson()
  def criarImpressoraJatoDeTinta(self) -> ImpressoraJatoDeTinta:
    return ImpressoraJatoDeTintaEpson()
