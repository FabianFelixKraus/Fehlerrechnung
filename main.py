from import_data import main_data  
from statistisch import main_statistisch
from gauss import main_gauss
from output import main_output


def create_final_file(final_text):
    with open("Ergebnis_WUHU@EZ.txt", "w") as file:
        file.write(final_text)

# Hier werden alle files geordnet aufgerufen, um 
def main():
    #1. Daten von import_data.py holen
    #name_of_rows entspricht den Namen von der csv-Datei
    name_of_rows, actual_data = main_data()


    #2. Gaussche Fehlerfortpflanzung machen & Tatsächlichen Wert aka. Berechneter Wert bestimmen
    data = main_data()
    tats_wert, gauss_Fehler, actual_formular, gauss_calc_formular = main_gauss(data)


    #3. Statistischen Fehler berechnen
    #3.1 Statistischer Fehler von den csv Daten bestimmen:
    new_order = []
    for i in range(len(actual_data[0])):
        new_order.append([])
        for value in actual_data:
            new_order[i].append(float(value[i]))
    #statistischer_Fehler = main_statistisch([(i,new_order[0][i]) for i in range(len(new_order))])
    
    all_statistischer_Fehler = dict()
    for i, data_row in enumerate(new_order):
        all_statistischer_Fehler[name_of_rows[i]] = main_statistisch(data_row)

    #3.2 Statistischer Fehler von dem berechneten Wert bestimmen
    all_statistischer_Fehler["Berechneter Wert"] = main_statistisch(tats_wert)

    #4. Output String erstellen um das file zu erstellen
    ausgabe_string = main_output(gauss_Fehler, all_statistischer_Fehler, tats_wert, actual_formular, gauss_calc_formular, data)
    create_final_file(ausgabe_string)
    print("\n")
    print("Das Ausgabefile wurde erfolgreich erstellt!!")
    print("\n")

main()


"""
Am Ende dieses Abschnittes passiert:

Variable a hat 1 sigma Umgebung 0,5135 und 3 sigma Umgebung 1,35343
Variable b hat 1 sigma Umgebung 0,235 und 3 sigma Umgebung 1,1473
Variable c hat 1 sigma Umgebung 0,86684 und 3 sigma Umgebung 2,15673
Berechneter Wert hat 1 sigma Umgebung 0,7351 und 3 sigma Umgebung 1,9684

Die Variable all_statistischer Fehler sieht dann wie folgt aus:
{
"a":                (0.5135,1.35343),
"b":                (0.235,1.1473),
"c":                (0.86684,2.15673),
"Berechneter Wert": (0.7351, 1.9684)
}
"""