def main_output(g_fehler,s_fehler,wert,formel,gauss_formel, messwerte):
    #hier ist die kommandozentrale für dieses File
    ausgabe = " "

    ausgabe += "Formel:       "+formel+"\n\n"
    ausgabe += "Formel zur Gaussschen-Fehlerfortpflanzung:        "+gauss_formel+"\n\n"
    ausgabe+= "______________________________________________________________________________ \n\n"
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

    ausgabe+= "______________________________________________________________________________ \n"
    ausgabe+= "______________________________________________________________________________ \n\n\n"
    ausgabe += "Variable | Statistischer Fehler 1-Sigma Umgebung (68,3%) | Statistischer Fehler 1-Sigma Umgebung (95,5%) |  Statistischer Fehler 3-Sigma Umgebung (99,7%) \n"
    ausgabe+= "______________________________________________________________________________ \n"
    
    for key in s_fehler:
        ausgabe += str(key)
        ausgabe += "  |  "
        ausgabe+= str(s_fehler[key][0])
        ausgabe+= "  |  "
        ausgabe+= str(s_fehler[key][1])
        ausgabe+= "  |  "
        ausgabe+= str(s_fehler[key][2])
        ausgabe+= "\n\n"
    return ausgabe

