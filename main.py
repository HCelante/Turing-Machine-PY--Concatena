import sys
#import TuringMachine

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
        for line in auxList:
                print(line)
        #print (auxList)
if __name__ == "__main__":
  main()
