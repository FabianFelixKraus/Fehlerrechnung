#Dieses file berchnet den statistischen Fehler
#Es wird ein Tupel aus zwei Werten ausgegeben
#Der erste Wert entspricht dem Fehler, des 1-Sigma (68.3%) Intervalls
#Der zweite Wert entspricht dem Fehler, des 3-Sigma (99.7%) Intervalls

from math import sqrt

#Berechnung Mittelwert
def calc_mittelwert(data):
    print(data)
    summ = 0
    for item in data:
        summ += item[1]
    return summ/len(data)

#Berechnung Standardabweichung
def calc_standardabweichung(data, mittelwert):
    n = len(data)
    summ = 0
    for item in data:
        summ += (item[1]-mittelwert)**2
    summ = summ * 1/(n-1)
    return sqrt(summ)

#Bestimmung des Faktors, falls es weniger als 20 Datenpunkte gibt
#Es müssen noch die Faktoren bestimmt werden für das 3-Sigma Intervall!
def get_faktor(data):
    length = len(data)
    faktoren_1 = [(3,1.32),(4,1.2),(5,1.15),(6,1.11),(7,1.095),(8,1.08),(9,1.07),(10,1.06),(11,1.057),(12,1.054),(13,1.051),(14,1.048),(15,1.045),(16,1.042),(17,1.039),(18,1.036),(19,1.033),(20,1.03)]
    faktoren_2 = [(3,19.2),(4,9.2),(5,6.6),(6,5.5),(7,5),(8,4.5),(10,4.1),(20,3.4)]

    if len(data) < 3:
        print("Zu wenige Datenpunkte. Es werden mindestens 3 für die Berechnung des statistischen Fehlers benötigt!!")

    output = []
    for item in faktoren_1:
        if item[0] == length:
            output.append(item[1])
            break
    if len(output) == 0:
        output.append(1)
    
    for item in faktoren_2:
        if item[0] == length:
            output.append(item[1])
            break
    if len(output) == 1:
        output.append(1)

    return output
    

def calc_statistischer_fehler(standardabweichung, n, faktor):
    return (faktor[0] * (standardabweichung/sqrt(n)), faktor[1] * (standardabweichung/sqrt(n)))

def main_statistisch(data):
    n = len(data)
    mittelwert = calc_mittelwert(data)
    standardabweichung = calc_standardabweichung(data,mittelwert)
    faktor = get_faktor(data)
    return calc_statistischer_fehler(standardabweichung, n, faktor)

#print(main_statistisch(data))


