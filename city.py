import sys
import numpy as np


def drawTree():

    print("        _/\_        ") #8, 2, 2, 8
    print("      _/    \_      ")
    print("    _/     |  \_    ")
    print("  _/            \_  ")
    print(" |   |            | ")
    print(" |           |   | ")
    print(" |________________| ")
    print("        |  |        ")
    print("        |  |        ")
    print("        |  |        ")
    print("        |  |        ")
    print("        |__|        ")

    return 0


def drawappleTree(height, trunk): #Assume width is 20

    for x in range(height-1):
        air = " "*(8-x)
        left = "_/"
        right = "\_"
        space = " "
        apple = np.random.randint(0,3)
        for y in range((20 - len(air)*2 -4)):
            if (y == apple):
                space += "*"
            else:
                space += " "
        #space = " "* (20 - len(air)*2 -4)

        middle = "" + space
        print(air + left + middle +right+ air)
    base = (20-(height-2)*2)
    side = (height-2)
    print(" "*side+("-"*base) + " "*side )
    air = " "*8
    for x in range(trunk -1):
        print(air + "| |"+ air)
    print(air + "|_|"+ air)


def drawmoreTrees(n):
    size = np.random.randint(7,20)
    for x in range(n):
        apples = np.random.randint(0,3)
        drawTree()
    return 0


def main():   
    print(drawappleTree(6,5)) #Assume width of drawing is 20

if __name__ == "__main__": 
    main()
    sys.exit(0)
else:
    print("fail")
    sys.exit(1)