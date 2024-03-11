import random
import time
name = input("Inserisci il tuo nickname:")

p1 = {"name": name, "vita": 100, "energia": 1500}
p2 = {"name": "boss", "vita": 100}

print("Scegli le giuste mosse per battere il boss")
def bvo():
    while True:
        #mosse
        ms = input("Scegli tra queste mosse (hai "+str(p1["energia"])+" di energia rimanente): 1:PUGNO(-10 Energy) 2:CALCIO(-15 Energy) 3:TESTATA(-20 Energy) 4:TRASFORMAZIONE-GOKU(-1000 Energy)")
        if(ms == "1"):
            if(p1["energia"] >= 10):
                danno = random.randint(0, 15)
                p1["energia"] -= 10
                p2["vita"] -= danno
                print("Hai usato pugno!!\nE hai inflitto " + str(danno) + " al tuo avversario il " + p2["name"] + " ora ha " + str(p2["vita"]) + " di vita")
            else:
                print("Non hai abbastanza energia per usare questa mossa")
                bvo()
        elif(ms == "2"):
            if(p1["energia"] >= 15):
                danno = random.randint(5, 20)
                p1["energia"] -= 15
                p2["vita"] -= danno
                print("Hai usato calcio!!\nE hai inflitto " + str(danno) + " al tuo avversario il " + p2["name"] + " ora ha " + str(p2["vita"]) + " di vita")
            else:
                print("Non hai abbastanza energia per usare questa mossa")
                bvo()
        elif(ms == "3"):
            if(p1["energia"] >= 20):
                danno = random.randint(10, 30)
                p1["energia"] -= 20
                p2["vita"] -= danno
                print("Hai usato testata!!\nE hai inflitto " + str(danno) + " al tuo avversario il " + p2["name"] + " ora ha " + str(p2["vita"]) + " di vita")
            else:
                print("Non hai abbastanza energia per usare questa mossa")
                bvo()
        elif(ms == "4"):
            if(p1["energia"] >= 1000):
                danno = random.randint(60, 100)
                p1["energia"] -= 1000
                p2["vita"] -= danno
                print('Hai usato trasformazione-goku!!\nE hai inflitto ' + str(danno) + " al tuo avversario il " + p2["name"] + " ora ha " + str(p2["vita"]) + " di vita")
            else:
                print("Non hai abbastanza energia per usare questa mossa")
                bvo()
        else:
            print("Non esiste nessuna mossa con questo numero!")
            bvo()
    
        #Controlli vita e energia
        if(p1["vita"] <= 0):
            print("Hai perso")
            break
        elif(p2["vita"] <= 0):
            print("Hai vinto")
            break
        elif(p1["energia"] <= 0):
            print("Hai finito l'energia e di conseguenza hai perso")
            break
        
        #Boss
        time.sleep(5)
        danno = random.randint(0, 50)
        p1["vita"] -= danno
        print("Il "+p2["name"]+" ti ha inflitto "+str(danno)+" di danno ora hai "+str(p1["vita"])+" di vita")
        
time.sleep(3)
bvo()
