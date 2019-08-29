import sys
import TuringMachine 

def main():
        auxList = []
        #auxaux =[]
        with open((sys.argv[1]), "r") as f:
                #for i in f:
                #        if i == '\n':
                #                auxList.append(auxaux)
                #        if i != ' ':
                #                auxaux.append(i)
                auxList = [line.strip().split(" ") for line in f]
        #for line in auxList:
        #        print(line)
        #print (auxList)
        # leu o arquivo e cortou
        # linha 1 alfabeto de entrada
        # linha 2 fita
        # linha 3 simbolo que representa branco
        # linha 4 estados
        # linha 5 estado inicial
        # linha 6 conjunto de estados finais
        # quantidade de fitas
        machine = TuringMachine.Machine()
        machine.set_atributos(auxList) 
        machine.print_maquina()
if __name__ == "__main__":
  main()
