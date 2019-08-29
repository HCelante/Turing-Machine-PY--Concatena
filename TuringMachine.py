import fita
import estado


class Machine():

    def __init__(self):
        self.Alfabeto = [] # alfabeto da maquina
        self.estados_Iniciais = [] # lista de estados iniciais
        self.finais = [] # lista de estados finais
        self.qtd_fitas = [] # qtd de fitas 
        self.blank_space = ''
    
    
    def set_atributos(self,lista):
        self.Alfabeto = lista[1]
        self.estados_Iniciais = lista[4]
        self.finais = lista[5]
        self.qtd_fitas = lista[-1]
        self.blank_space = lista[2]

    def print_maquina(self):
        print("> alfabeto: ", self.Alfabeto)
        print("> estados iniciais: ", self.estados_Iniciais)
        print("> estados finais: ",self.finais)
        print("> qtd de fitas: ", self.qtd_fitas)
        print("> blank space: ", self.blank_space)




    def fita_Anda(self, posfita, proxpossivel):
        if (proxpossivel.lado) == ['R']:
            posfita += 1
        else:
            posfita -= 1
        return posfita


    def prox_Est(self, vertice, fitatual, posfita): # funcao para percorrer os estados
        if len(vertice.prox_Estado) > 1: # se tiver mais que um prox estado
            for proxpossivel in vertice.prox_Estado: #percorre os proximos estados checando a possibilidade de prosseguir
                if (proxpossivel.consome == fitatual[posfita] ):# checa se pode avancar. 
                    fitatual[posfita] = proxpossivel.escreve # escreve na fita 
                    posfita = self.fita_Anda(posfita, proxpossivel) # atualiza a posicao da fita
                    if (proxpossivel.prox_Estado != None) and (proxpossivel not in self.finais):# nao eh estado de aceitacao e o prox nao eh nulo
                        self.prox_Est(vertice,fitatual,posfita)
                    elif (proxpossivel.prox_Estado != None) and (proxpossivel in self.finais):
                        print (fitatual)
                        return True
                    else:
                        return False
        else:
            proxpossivel = vertice.prox_Estado
            if (proxpossivel.consome == fitatual[posfita] ):# checa se pode avancar. 
                    fitatual[posfita] = proxpossivel.escreve # escreve na fita 
                    posfita = self.fita_Anda(posfita, proxpossivel) # atualiza a posicao da fita
                    if (proxpossivel.prox_Estado != None) and (proxpossivel not in self.finais):# nao eh estado de aceitacao e o prox nao eh nulo
                        self.prox_Est(vertice,fitatual,posfita)
                    elif (proxpossivel.prox_Estado != None) and (proxpossivel in self.finais):
                        print (fitatual)
                        return True
                    else:
                        return False
            else:
                return False
#    def inicia_consome(self):
#        atual_est = self.atual_State
#        fita = self.Fita
#        atualpos = 0
#
#    def consome_Fita(self,atual_est, atualpos):
#
#        if atual_est in self.finals:
#            return True, fita
#
#
#        else:
#            for i in atual_est.prox_Estado:# procura uma transicao valida
#                if fita[fita.atualpos] == i.consome:# se pode avancar
#                    fita[fita.atualpos] = i.escreve # escreve na fita
#                    atualpos += 1
#                    consome_Fita(atual_est.prox_Estado,atualpos) # recomeca a busca por proximos estados validos
            

