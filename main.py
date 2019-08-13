import sys

def main():
    auxList = []
    with open((sys.argv[1]), "r") as f:
        auxList = [line.strip().split(" ") for line in f]
        
if __name__ == "__main__":
  main()
