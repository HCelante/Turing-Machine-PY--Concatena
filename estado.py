
class estado():

  def __init__(self, lista_de_inf): # Recebe uma linha da lista de informacoes sobre estado
    self.nome_Estado = lista_de_inf[0]
    self.prox_Estado = []
    self.ante_Estado = []
    self.consome = self.set_consome()
    self.escreve = self.set_escreve()


  
