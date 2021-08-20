from CentralPrint import CentralPrint

class Main:
  def start(self):
      main = CentralPrint.getInstancia()
      sec = CentralPrint.getInstancia()
      # print('Mesma instancia iniciada? ',main == sec )
      main.criacao() 
      main.testarImpressorasDisponiveis()
      valor =  input('Digite o que deseja imprimir:\n')
      main.enviarParaImpressao(valor)
Main().start()