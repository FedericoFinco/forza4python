counter=0
player=0
x="ciao"
print(x)
import numpy as nmp
m=nmp.array([["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["c","c","c","c","c","c","c"]])
print(m)

def read():
    for c in range(7):
        for i in range(7):
            # format per verificare la lettura corretta della matrice
            # if (m[c][i])=="1":
            #     print("|   ", end='')
            # elif (m[c][i])=="2":
            #     print("|    |")
            # elif (m[c][i])=="":
            #     print("|  o ", end='')
            # elif (m[c][i])=="c":
            #     print("col{x}|".format(x=i+1),end='')
            # format strano non so perche
            # if c==0 and i==0:
            #     print("|  o ", end='')
            # elif i==6 and c!=(5+1):
            #     print("|  o |")
            # elif c==(5+1):
            #     if c==(5+1) and i==0:
            #         print("|  {x} |".format(x=i+1),end='')
            #     else:
            #         print("  {x} |".format(x=i+1),end='')
            # else :
            #     print("|  o ", end='')
            if i == 0 and c!=(5+1):
                print("||", end='')
            if (m[c][i])=="":
                print("   |", end='')
            elif (m[c][i])=="x":
                print(" x |", end='')
            elif (m[c][i])=="o":
                print(" o |", end='')
            if i == 6 and c!=(5+1):
                print("|")
            elif c==(5+1):
                if i==0:
                    print(" | {x} |".format(x=i+1),end='')
                else:
                    print(" {x} |".format(x=i+1),end='')

def turnCounter():
    # counter=0
    global counter
    counter=(counter+1)

    
    print("\n è il turno: ",counter)
    # che brutto pyton devo specificare ogni volta che sto lavorando su una variabile globale bleah
    global player
    if counter%2==0:
        player=2
    else:
        player=1
    print("tocca al giocatore: ",player)
    


def placement(col):
    if player==1:
        playersign="x"
    if player==2:
        playersign="o"
    for i in range(6):
        if (m[i][col-1])=="" and i<=5:
            print("0")
            print(i)
            if i==5 :
                (m[i][col-1])=playersign
                print("1")
            if (m[i+1][col-1])!="":
                (m[i][col-1])=playersign
                print("2")
        else:
            # pass
            print("sono nel pass")
    read()


read()

# p1ChoosenCol=int(input("\n scegli una colonna:  "))
# placement(p1ChoosenCol)
victory=""
while victory!="p1" or victory!="p2":
    # counter=counter+1 risolto con il global nella funzione turncounter
    turnCounter()
    print("conferma turno player",player)
    p1ChoosenCol=int(input("\n scegli una colonna:  "))
    placement(p1ChoosenCol)
