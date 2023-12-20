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
    
def downControl(y,x):
    # if m[y][x]==m[y-1][x]:
    for c in range(4):
        if m[y][x]==m[y+(c+1)][x] and m[y][x]!="":
            pass
        else:
            break
        if c==2:
            print("vittoria!")

def rightControl(y):
    # for c in range(4):
    #     if m[y][x]==m[y][x+(c+1)] and m[y][x]!="":
    #         pass
    #     else:
    #         break
    #     if c==3:
    #         print("vittoria!")
    
    counter=1
    for c in range((len(m[y]))-1):
        print ("lavoro su",m[y] )
        if m[y][c]==m[y][c+1]:
            counter=counter+1
            # print("il counter sale à",counter,"perchè ",m[y][c],"è uauale a ",m[y][c+1])
        else:
            counter=1
            # print("azzero il counter",counter,"perchè ",m[y][c],"è diverso da ",m[y][c+1])
        if counter==4:
            print("vittoria")

def LRCrossConrtol(y,x):
    # counter=0     NON FUNZIONA NEI CASI TIPO TABELLA 4X8
    # rounds=0
    # controlY=y
    # controlX=x
    # if y>=x:
    #     x=0
    #     rounds=(len(m[0])-controlX)
    # elif x>y:
    #     y=0
    #     rounds=(len(m[0])-controlY)
    # for c in range(rounds):
    #     if m[y][x]==m[y+(c+1)][x+(c+1)]:
    #         counter=counter+1
    #         # print("il counter sale à",counter,"perchè ",m[y][c],"è uauale a ",m[y][c+1])
    #     else:
    #         counter=1
    #         # print("azzero il counter",counter,"perchè ",m[y][c],"è diverso da ",m[y][c+1])
    #     if counter==4:
    #             print("vittoria")
    while x!=0 or y!=0
        c=1
        x=x-c
        y=y-c
        c=c+1
        




# def victoryCheck(lastPointY,lastPointX):
#     print(lastPointY,lastPointX)
#     if lastPointY



def placement(col):
    if player==1:
        playersign="x"
    if player==2:
        playersign="o"
    for i in range(6):
        if (m[i][col-1])=="" and i<=5:
            # print("0")
            # print(i)
            if i==5 :
                (m[i][col-1])=playersign
                # print("1")
                # downControl(i,col-1)
                rightControl(i)
            elif (m[i+1][col-1])!="":
                (m[i][col-1])=playersign
                # print("2")
                # downControl(i,col-1)
                rightControl(i)
        else:
            pass
            # print("sono nel pass")
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
    
