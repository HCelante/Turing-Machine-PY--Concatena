import fita
import estado


class Machine():

    def __init__(self):
        self.Alfabeto = []
        self.estados_Iniciais = []
        self.finais = []
        self.qtd_fitas = []
    
    def set_atributos(self,lista):
        self.Alfabeto = lista[1]
        self.estados_Iniciais = linha[5]
        self.finais = lista[6]
        self.qtd_fitas = lista[7]

    











    def inicia_consome(self):
        atual_est = self.atual_State
        fita = self.Fita
        atualpos = 0

    def consome_Fita(self,atual_est, atualpos):

        if atual_est in self.finals:
            return True, fita


        else:
            for i in atual_est.prox_Estado:# procura uma transicao valida
                if fita[fita.atualpos] == i.consome:# se pode avancar
                    fita[fita.atualpos] = i.escreve # escreve na fita
                    atualpos += 1
                    consome_Fita(atual_est.prox_Estado,atualpos) # recomeca a busca por proximos estados validos
            

