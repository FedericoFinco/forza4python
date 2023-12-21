counter=0
player=0
vittoria=4
colonne=7
righe=6
victory=""
ReCCustom=""
colErr=0
# SCELTA DELLE GRIGLIE SE MODIFICATE    
while ReCCustom!="y" and ReCCustom!="n":
    ReCCustom=str(input("vuoi impostare righe e colonne?\nSe scegli no i valori di defaut sono 7 colonne e 6 righe\n y/n"))

if ReCCustom=="y":
    colonne=int(input("inserisci il numero di colonne: "))
    righe=int(input("inserisci il numero di right: "))
else:
    print("i valori di default sono stati impostati.")




import numpy as nmp
# m=nmp.array([["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["c","c","c","c","c","c","c"]])
d=[]
for c in range(righe):

    for c in range(colonne):
        d.append("")
for c in range(colonne):
    d.append("c")
# print(d)
f=nmp.array(d)
# print(f)
m = f.reshape((righe +1), colonne)
# print(d)
print(m)



def read():
    for c in range(righe+1):
        for i in range(colonne):
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
            if i == 0 and c!=(righe):
                print("||", end='')
            if (m[c][i])=="":
                print("   |", end='')
            elif (m[c][i])=="x":
                print(" x |", end='')
            elif (m[c][i])=="o":
                print(" o |", end='')
            if i == (colonne-1) and c!=(righe):
                print("|")
            elif c==(righe):
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
        player="p2"
    else:
        player="p1"
    print("tocca al giocatore: ",player)
    
def downControl(y,x):
    # if m[y][x]==m[y-1][x]:
    global victory
    for c in range(4):
        if m[y][x]==m[y+(c+1)][x] and m[y][x]!="":
            pass
        else:
            break
        if c==2:
            print("vittoria!")
            victory=player

def rightControl(y):
    # for c in range(4):
    #     if m[y][x]==m[y][x+(c+1)] and m[y][x]!="":
    #         pass
    #     else:
    #         break
    #     if c==3:
    #         print("vittoria!")
    global victory
    counter=1
    for c in range((len(m[y]))-1):
        print ("lavoro su",m[y] )
        if m[y][c]==m[y][c+1] and m[y][c]!="":
            counter=counter+1
            # print("il counter sale à",counter,"perchè ",m[y][c],"è uauale a ",m[y][c+1])
        else:
            counter=1
            # print("azzero il counter",counter,"perchè ",m[y][c],"è diverso da ",m[y][c+1])
        if counter==vittoria:
            print("vittoria")
            victory=player

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
    global victory
    while x!=0 and y!=0:
        c=1
        x=x-c
        y=y-c
        c=c+1
    print("sto partendo da:",y,",",x)
    if y==0:
        if x<=(len(m[0])-1 -vittoria):
            counter=1
            while y!=(righe -1) and (x!=colonne-1):
                print("lavoro sulla posizione",y,x)
                c=1
                
                
                if m[y][x]==m[y+1][x+1] and m[y][x]!="":
                    counter=counter+1
                    print("il counter sale à",counter,"perchè ",m[y][x],"è uauale a ",m[y+1][x+1])
                else:
                    counter=1
                    print("azzero il counter",counter,"perchè ",m[y][x],"è diverso da ",m[y+1][x+1])
                if counter==vittoria:
                    print("vittoria")
                    victory=player
                x=x+c
                y=y+c
                c=c+1
        else:
            print("il controllo CrossLR non serve perche",x,"è troppo avanti")
    elif x==0:
        if y<=((righe) -(vittoria)):
            counter=1
            while y!=(righe -1) and x!=(colonne -1):
                print("lavoro sulla posizione",y,x)
                
                c=1
                
                
                if m[y][x]!="":
                    print("la confronto con ",y+1,x+1)
                    if m[y][x]==m[y+1][x+1]:
                        counter=counter+1
                        print("y è ",y,"x è ",x)
                        print("il counter sale à",counter,"perchè ",m[y][x],"è uauale a ",m[y+1][x+1])
                    else:
                        counter=1
                        print("y è ",y,"x è ",x)
                        print("azzero il counter",counter,"perchè ",m[y][x],"è diverso da ",m[y+1][x+1])
                    if counter==vittoria:
                        print("vittoria")
                        victory=player
                else:
                    print("la posizione ",y,x,"è vuota te la stampo :",m[y][x])
                x=x+c
                y=y+c
                c=c+1
        else:
            print("il controllo CrossLR non serve perche",y,"è troppo giù")
            print("il conto viene da posizione ",((righe +1) -(vittoria)))


def RLCrossConrtol(y,x):
    global victory
    while x!=colonne-1 and y!=0:
        c=1
        x=x+c
        y=y-c
        c=c+1
    print("sto partendo da:",y,",",x)
    if y==0:
        if x>= -vittoria:
            counter=1
            while y!=righe and x!=0:
                print("lavoro sulla posizione",y,x)
                c=1
                
                if m[y][x]!="":
                    if m[y][x]==m[y+1][x-1]:
                        counter=counter+1
                        print("il counter sale à",counter,"perchè ",m[y][x],"è uauale a ",m[y+1][x-1])
                    else:
                        counter=1
                        print("azzero il counter",counter,"perchè ",m[y][x],"è diverso da ",m[y+1][x-1])
                    if counter==vittoria:
                        print("vittoria")
                        victory=player
                else:
                    print("la posizione ",y,x,"è vuota te la stampo :",m[y][x])
                x=x-c
                y=y+c
                c=c+1
        else:
            print("il controllo CrossRL non serve perche",x,"è troppo avanti")
            print("il conto viene da questa x in poi ",(vittoria))
    elif x==colonne-1:
        if y>=((righe) -(vittoria)):
            counter=1
            while y!=(righe -1) and x!=(colonne):
                print("lavoro sulla posizione",y,x)
                
                c=1
                
                
                if m[y][x]!="":
                    print("la confronto con ",y+1,x-1)
                    if m[y][x]==m[y+1][x-1]:
                        counter=counter+1
                        print("y è ",y,"x è ",x)
                        print("il counter sale à",counter,"perchè ",m[y][x],"è uauale a ",m[y+1][x-1])
                    else:
                        counter=1
                        print("y è ",y,"x è ",x)
                        print("azzero il counter",counter,"perchè ",m[y][x],"è diverso da ",m[y+1][x-1])
                    if counter==vittoria:
                        print("vittoria")
                        victory=player
                else:
                    print("la posizione ",y,x,"è vuota te la stampo :",m[y][x])
                x=x-c
                y=y+c
                c=c+1
        else:
            print("il controllo CrossLR non serve perche",y,"è troppo giù")
            print("il conto viene da questa Y in poi ",((righe)-(vittoria)))

        




# def victoryCheck(lastPointY,lastPointX):
#     print(lastPointY,lastPointX)
#     if lastPointY



def placement(col):
    global counter
    global colErr
    if player=="p1":
        playersign="x"
    if player=="p2":
        playersign="o"
    
    if (m[0][col-1])!="":
        print("la colonna è piena")
        counter=counter-1
        colErr=1
    for i in range(righe):
        if (m[i][col-1])=="" and i<=(righe-1):
            # print("0")
            # print(i)
            if i==(righe-1) :
                (m[i][col-1])=playersign
                # print("1")
                downControl(i,col-1)
                rightControl(i)
                LRCrossConrtol(i,col-1)
                RLCrossConrtol(i,col-1)
            elif (m[i+1][col-1])!="":
                (m[i][col-1])=playersign
                # print("2")
                downControl(i,col-1)
                rightControl(i)
                LRCrossConrtol(i,col-1)
                RLCrossConrtol(i,col-1)
        else:
            pass
            # print("sono nel pass")
    read()

    


read()



# p1ChoosenCol=int(input("\n scegli una colonna:  "))
# placement(p1ChoosenCol)
victory=""

while victory!="p1" and victory!="p2":
    # counter=counter+1 risolto con il global nella funzione turncounter
    turnCounter()
    print("conferma turno player",player)
    if victory=="p1" or victory=="p2":
        break
    check=""
    while check !="ok":
        try:
            p1ChoosenCol=int(input("\n {x}  ".format(x="scegli una colonna" if colErr==0 else "colonna piena/colonna inesistente o non valida")))
        except ValueError:
            colErr=1
            print("non hai scritto un numero")
        if colErr==0:
            check="ok"
    if p1ChoosenCol>(colonne-1):
        print("la colonna non esiste")
        counter=counter-1
        colErr=1
    else:
        placement(p1ChoosenCol)
    colErr=0
    
print("\n ha vinto il player {x}".format(x=victory))
