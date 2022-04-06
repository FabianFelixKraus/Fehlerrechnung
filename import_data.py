def import_der_daten():
    csv_data = []
    with open('test.csv','r') as file:                              # Datei wird geöffnet als 'file'
        for line in file.readlines():
            csv_data.append(line.split(","))
    return csv_data
    
def strukturierung_der_daten(csv_data):

    data = []
    for i,liste in enumerate(csv_data):
        if i != 0:
            data.append(tuple([a[:-1] if i == 2 else a for i, a in enumerate(liste)]))
        else:
            names = [a if (i != len(liste)-1) else a[:-1] for i,a in enumerate(liste)]

    return (names,data)

def main_data():
    return strukturierung_der_daten(import_der_daten())


