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
# creazione della matrice a due dimensioni
d=[]
#con il doppio for creo il mio array mono dimensionale
for c in range(righe):

    for c in range(colonne):
        d.append("")
for c in range(colonne):
    d.append("c")
# print(d)
f=nmp.array(d)
# print(f)
#con il reshape gli dò la seconda dimensione 
m = f.reshape((righe +1), colonne)
# print(d)
print(m)



def read():
    for c in range(righe+1):
        for i in range(colonne):


            #  VECCHIO CODICE MIGLIORATO format per verificare la lettura corretta della matrice
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

            #formattatore della griglia, crea la doppia || all'inizio e alla fine per la parte da gioco,
            # sotto invece inserisce i numeri delle colonne
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

#tiene il conto dei turni tramite la viarabile globale counter, e scrive a terminale di chi è il turno
def turnCounter():
    
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

#funzione che effettua il controllo verticale delle pedine, andando eventualmente a modificare la variabile
# globale victory. Per una vittoria verticale devo controllare solo le pedine sottostanti se sono uguali, 
# quindi controllo andando ad aumentare la y : per ogni iterazione con successo salirà il mio c, altrimenti
# con il break si interrompe il ciclo e il contatore c non arriverà mai al valore corretto.
def downControl(y,x):
    
    global victory
    for c in range(vittoria):
        if m[y][x]==m[y+(c+1)][x] and m[y][x]!="":
            pass
        else:
            break
        if c==(vittoria - 2):
            print("vittoria!")
            victory=player

#funzione che effettua il controllo orizzontale delle pedine, andando eventualmente a modificare la variabile
# globale victory. Il modo piu semplice di farlo è anziche agire partendo dalla posizione dell'ultima pedina
# inserita lavoro direttamente su tutta la riga. controllo ogni posizione a partire da 0 fino ad arrivare all
# ultima posizione (r 136). quindi controllo se la posizione attuale è uguale a quella seguente e diversa da
# stringhe vuote,  in caso positivo aumento il mio counter interno di uno. in caso siano diverse faccio 
# tornare il counter a 1 (che sarebbe la mia pedina attuale).
def rightControl(y):

    # CODICE OBSOLETO 
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

#questa funzione effettua il controllo obliquo da sx verso dx partendo dall'alto. La commenterò tra le righe
# di codice essendo più complessa. 
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
    #qui salendo di una riga e una colonna per volta arrivo alla prima posizione della diagonale che mi
    # interessa
    while x!=0 and y!=0:
        c=1
        x=x-c
        y=y-c
        c=c+1
    print("sto partendo da:",y,",",x)
    #se la mia Y è arrivata a 0 significa che la casella di partenza si trova al limite superiore della 
    # griglia. 
    if y==0:
        #trovandomi sulla prima riga della griglia e muovendomi da sinistra a destra, devo avere
        # orizzontalmente abbastanza caselle per poter avere una diagonale con la lunghezza minima per la 
        # vittoria ( la lunghezza della riga - le caselle necessarie per la vittoria ) 
        if x<=(len(m[0])-1 -vittoria):
            counter=1
            #effettuerò il controllo finche non sarò arrivato all'ultima riga in basso o all'ultima colonna
            while y!=(righe -1) and (x!=colonne-1):
                print("lavoro sulla posizione",y,x)
                c=1
                
                #qui inizio a confrontare la casella inizale con la successiva nella diagonale sempre con il 
                # controllo che non sia vuota. in caso positivo counter+1 altrimenti si resetta ad 1
                if m[y][x]==m[y+1][x+1] and m[y][x]!="":
                    counter=counter+1
                    print("il counter sale à",counter,"perchè ",m[y][x],"è uauale a ",m[y+1][x+1])
                else:
                    counter=1
                    print("azzero il counter",counter,"perchè ",m[y][x],"è diverso da ",m[y+1][x+1])
                if counter==vittoria:
                    print("vittoria")
                    victory=player
                # per andare a controllare la casella successiva incremento di uno i valori della posizione
                # posizione precedente
                x=x+c
                y=y+c
                c=c+1  #dubbioso riguardo al perchè io abbia messo questa riga
        else:
            print("il controllo CrossLR non serve perche",x,"è troppo avanti")
    #se la mia x invece è quella che è arrivata a zero significa che sono sul limite sinistro della griglia
    elif x==0:
        #qui per avere la diagonale abbastanza lunga devo non trovarmi troppo "all'angolo", per precisione devo
        # avere verticalmente almeno tante caselle quanto la vittoria (quindi numero totale di righe - vittoria)
        if y<=((righe) -(vittoria)):
            counter=1
            #effettuerò il controllo finche non sarò arrivato all'ultima riga in basso o all'ultima colonna
            while y!=(righe -1) and x!=(colonne -1):
                print("lavoro sulla posizione",y,x)
                
                c=1
                
                #uguale al blocco precedente, faccio il confronto tra le caselle e uso il counter
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
