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
        if estado in maq2[3]: # se existe um com mesmo nome na maquina 2, renomeia
            para = 1

            if cont <= len(maq2[3]):
                
                cont += 1
                ind = maq2[3].index(estado) # recebe o  indice do estado a ser renomeado
                if ((estado + maq2[3][ind]) not in maq2[3]) and ((estado + maq2[3][ind]) not in maq1[3]):
                    maq2[3][ind] = estado + maq2[3][ind] # renomeia o estado com a concatenacao do seu correspondente ex: 'a' e 'a' vira 'aa'
                else:
                    print("> O estado ",maq2[3][ind], "precisou de um novo nome")
                    maq2[3][ind] = busca_NNE(maq1[3] + maq2[3])

                
            else:
                break
    return replace(maq1, maq2, para)# repete ate nao haver nenhuma correspondencia

def busca_NNE(lista): # busca nome nao existente
    sai = None
    nume = 0
    while sai == None:
        nume+=1
        if str(nume) not in lista:
            break
    print (" - Novo nome valido encontrado",nume)
    
    au = (str(nume))
    return   au


# FIM REPLACE ##########################################################################################
########################################################################################################

########################################################################################################
########################## FUNCAO RENOMEIA #############################################################
#_________________________________________ RENOMEIA AS TRANSICOES ######################################
def renomeia(maq2, auxList2):
    nomes1 = []
    nomes1 = auxList2[3]
    cont = 7
    aux = (auxList2[7:])
    indini = nomes1.index(auxList2[4][0]) # indice do estado inicial
    maq2[4] = [maq2[3][indini] ] # lista com a string dentro # string referente estado inicial
    indifi = nomes1.index(auxList2[5][0]) # indice do estado inicial
    maq2[5] = [maq2[3][indifi] ] # lista com a string dentro # string referente estado final
    for tr in aux:
        indsub = nomes1.index(tr[0])
        maq2[cont][0] = maq2[3][indsub]
        indsub2 = nomes1.index(tr[1])
        maq2[cont][1] = maq2[3][indsub2]
        cont += 1
    return maq2


# FIM RENOMEIA #########################################################################################
########################################################################################################


########################################################################################################
########################## CRIACAO DA MAQUINA 3 ########################################################
#_________________________________________ CRIA A MAQUINA RESULTADO DA CONCATENACAO ####################
def monta(maq1, maq2):
    maq3 = []

    for i in range(4):
        maq3.append(maq1[i] + maq2[i])
    maq3.append(maq1[4])
    maq3.append(maq2[5])
    maq3.append(maq1[6])
    for trans in (maq1[7:]):
        maq3.append(trans)
    lista_trs = []
    lista_trs = cria_nova_tr(maq1,maq2)
    for trs in lista_trs:
        
        print("> Transicao de conexao adicionada")
        print(" - ",trs)
        maq3.append(trs)

    for tr2 in (maq2[7:]):
        maq3.append(tr2)
    
    return maq3

def cria_nova_tr(maq1,maq2):
    tr_novas = []
    for final in maq1[5]:
        for inicial in maq2[4]:
                # para cada final, uma transicao para cada inicial da maq2 [final_maq1, inicial_maq2, branco, branco, Stay]
                tr_novas.append([final,inicial,maq1[2][0],maq1[2][0],'S'])
    return tr_novas

        

# FIM CRIACAO  #########################################################################################
########################################################################################################

########################################################################################################
# OPERACOES EM ARQUIVO #################################################################################
#_____________________________METODOS DE LEITURA E GRAVACAO EM ARQUIVO #################################

# Abre os dois arquivos e retorna as duas maquinas em 3 variaveis ######################################
def le_maquina():
    with open((sys.argv[1]), "r") as f:
        auxList1 = [line.strip().split(" ") for line in f]
     
    with open((sys.argv[2]), "r") as f:
        auxList2 = [line.strip().split(" ") for line in f]
    maqold = []

     
    with open((sys.argv[2]), "r") as f:
        maqold = [line.strip().split(" ") for line in f]

    return auxList1, auxList2, maqold

# Grava a nova maquina criada ###########################################################################

def grava_maquina(maq3):
    arquivo = open((str((sys.argv[1]).strip(".txt")) + str((sys.argv[2]).strip(".txt"))) + '.txt', 'w')
    for linhas in maq3:

        for chs in linhas:
            arquivo.write(str(chs + ' '))
        arquivo.write('\n')    
    arquivo.close()
    print("> Maquina 3 gravada no arquivo",(str((sys.argv[1]).strip(".txt")) + str((sys.argv[2]).strip(".txt"))) + '.txt' )

# FIM OPERACOES EM ARQUIVO ##############################################################################
#########################################################################################################

##### NOTAS 
    # linha 1 alfabeto de entrada (indice 0)
    # linha 2 fita                (indice 1)
    # linha 3 simbolo que representa branco
    # linha 4 estados
    # linha 5 estado inicial
    # linha 6 conjunto de estados finais
    # quantidade de fitas

# FIM NOTAS ##################################
##############################################

def main(): # recebe por parametro os dois arquivos  txt referente as maquinas 
    print('Processo iniciado _____________________________/')
    auxList1 = []
    auxList2 =[]  
    maqold = []
    maq21 = []
    maq3 = []

    #### abrindo os arquivos
    auxList1, auxList2, maqold = le_maquina()
    # ______________________________________________________
    
    #### renomeando os estados
    maq2 = replace(auxList1, auxList2, 1)
    maq21 = renomeia(maq2, maqold)
    # ______________________________________________________

    #### criando a maquina 3
    maq3 = monta(auxList1,maq21)
    # ______________________________________________________
    
    #### gravando a maquina 3 em arquivo 
    grava_maquina(maq3)
    # ______________________________________________________
    print("Terminado _____________________________________/")
if __name__ == "__main__":
  main()
