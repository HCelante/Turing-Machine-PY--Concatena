import sys
import TuringMachine

def main():
        auxList = []
        with open((sys.argv[1]), "r") as f:
                auxList = [line.strip().split(" ") for line in f]
        # leu o arquivo e cortou
        # linha 1 alfabeto de entrada
        # linha 2 fita
        # linha 3 simbolo que representa o espaço em branco (padrao: B)
        # linha 4 estados
        # linha 5 estado inicial
        # linha 6 conjunto de estados finais
        # quantidade de fitas 

        
if __name__ == "__main__":
  main()
