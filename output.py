def main_output(g_fehler,s_fehler,wert,formel,gauss_formel, messwerte):
    #hier ist die kommandozentrale für dieses File
    ausgabe = " "

    ausgabe += "Formel:       "+formel+"\n\n"
    ausgabe += "Formel zur Gaußschen-Fehlerfortpflanzung:        "+gauss_formel+"\n\n"
    ausgabe+= "______________________________________________________________________________ \n\n"
    ausgabe+= "Statistischer Fehler 1-Sigma Umgebung (68,3%):      "+str(s_fehler[0])+"\n"
    ausgabe+= "Statistischer Fehler 3-Sigma Umgebung (99,7%):      "+str(s_fehler[1])+"\n"
    ausgabe+= "______________________________________________________________________________ \n\n"



    ausgabe +=  "             |" + str(messwerte[0]) + "                 | Wert +- Gaussfehler \n\n"
    ausgabe+= "________________________________________________________________________________\n\n"
    for i in range (len(g_fehler)):
        
        ausgabe += str(i+1)
     
        ausgabe+= ".        |  "
        
        ausgabe+= str(messwerte[1][i])
       
        ausgabe += "        |  "
       
        ausgabe += str(wert[0])
        
        ausgabe+= " +-  "
      
        ausgabe+= str(g_fehler[i])
      
        ausgabe+= "\n\n"
       
        
    return ausgabe

