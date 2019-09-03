import sys
########################################################################################################
########################## FUNCAO REPLACE ##############################################################
#_________________________________________ RENOMEIA OS ESTADOS COM NOMES IGUAIS ########################

def replace(maq1, maq2, para):# substitui o nome dos estados ate nao haver estados com o mesmo nome

        cont = 0
        if para == 0:
                return maq2
        para = 0
        for estado in maq1[3]: # checa estado por estado da máquina 1, 
                #print(type(estado), type(maq2[3][0]))

                if estado in maq2[3]: # se existe um com mesmo nome na maquina 2, renomeia
                        para = 1
                        #print("traaal")
                        if cont <= len(maq2[3]):
                                
                                cont += 1
                                ind = maq2[3].index(estado) # recebe o  indice do estado a ser renomeado
                                if ((estado + maq2[3][ind]) not in maq2[3]) and ((estado + maq2[3][ind]) not in maq1[3]):
                                        maq2[3][ind] = estado + maq2[3][ind] # renomeia o estado com a concatenacao do seu correspondente ex: 'a' e 'a' vira 'aa'
                                else:
                                        maq2[3][ind] = busca_NNE(maq1[3] + maq2[3])
                                print (maq1[3])
                                print (maq2[3])
                                
                        else:
                                break
        return replace(maq1, maq2, para)# repete ate nao haver nenhuma correspondencia

def busca_NNE(lista): # busca nome nao existente
        sai = None
        nume = 0
        print(lista)
        while sai == None:
                nume+=1
                if str(nume) not in lista:
                        break
        print ("nome valido encontrado ",nume)
        
        au = (str(nume))
        return   au

########################################################################################################
# FIM REPLACE ##########################################################################################
########################################################################################################

########################################################################################################
########################## FUNCAO EMENDA ###############################################################
#_________________________________________ FAZ A CONCATENACAO DAS MAQUINAS #############################
def emenda(maq1, maq2):# concatenacao das maquinas
        # concatenacao do alfabeto
        pass

########################################################################################################
# FIM EMENDA ###########################################################################################
########################################################################################################

def main(): # recebe por parametro os dois arquivos  txt referente as maquinas 
        auxList = []
        #auxaux =[]
        with open((sys.argv[1]), "r") as f:
                auxList1 = [line.strip().split(" ") for line in f]
         
        with open((sys.argv[2]), "r") as f:
                auxList2 = [line.strip().split(" ") for line in f]
        #for line in auxList1:
                #print(line)
        #for line in auxList2:
                #print(line)
        maq2 = replace(auxList1, auxList2, 1)
        print (maq2)
        maq1 = auxList1
        #maq3 = emenda(maq1, maq2)

        #print (auxList)
        # leu o arquivo e cortou
        # linha 1 alfabeto de entrada
        # linha 2 fita
        # linha 3 simbolo que representa branco
        # linha 4 estados
        # linha 5 estado inicial
        # linha 6 conjunto de estados finais
        # quantidade de fitas

if __name__ == "__main__":
  main()
