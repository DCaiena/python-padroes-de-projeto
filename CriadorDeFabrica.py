from FabricaEpson import FabricaEpson
from FabricaHP import FabricaHP


class CriadorDeFabrica():
  def criarFabrica(self):
    if('epson'):
      print('Retorna Fabrica Epson ')
      return FabricaEpson()
    elif('hp'):
      print('Retorna Fabrica HP ')
      return FabricaHP()
