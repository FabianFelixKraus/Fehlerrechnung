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

    #2. Statistischen Fehler berechnen
    new_order = []
    for i in range(len(actual_data[0])):
        new_order.append([])
        for value in actual_data:
            new_order[i].append(float(value[i]))
    statistischer_Fehler = main_statistisch([(i,new_order[0][i]) for i in range(len(new_order))])
    
    #statistischer_Fehler = (1234.213423,1432.23432)

    #3. Gaussche Fehlerfortpflanzung & Tatsächlichen Wert bestimmen machen
    data = main_data()
    tats_wert, gauss_Fehler, actual_formular, gauss_calc_formular = main_gauss(data)

    #4. Output String erstellen um das file zu erstellen
    ausgabe_string = main_output(gauss_Fehler, statistischer_Fehler, tats_wert, actual_formular, gauss_calc_formular, data)
    create_final_file(ausgabe_string)


main()


