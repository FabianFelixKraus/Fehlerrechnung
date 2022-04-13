from sympy import symbols, diff
from math import sqrt

# data sind die Messdaten von import_data 
def main_gauss(data):
    #############################################################################################
    """
    # Hello, als erstes bitte die zwei Zeilen unten implementieren. Dabei a, b und c durch alle in der Formel vorkommenden Variablen ersetzen. 
    # Wichtig!! Die Variablen dürfen nur aus EINEM Buchstaben bestehen
    
    a, b, c = symbols('a b c', real=True)
    variablen = [a,b,c]

    # Als nächstes bitte die Formel angeben für die die gaußsche Fehlerfortpflanzung berechnet werden soll
    # Bitte in diesem Format: 

    f = a+b*c

    """
    ##############################################################################################

    a, b, c = symbols('a b c', real=True)
    variablen = [a,b,c]
    f = a*b*c

    def create_formular_actual_value():
        return str(f)

    def read_User_input_file():

        #Entfert alle Zeilen ohne Daten
        def first_correction(raw_data):
            data = []
            for element in raw_data:
                if "!!" and "??" in element:
                    data.append(element)
            return data

        #Extrahiert Daten aus der Zeile, entfernt Leerzeichen und returnt ("f = a+b*c",[("a",0.01),("b",0.5),("c",0.2)])
        def second_correction(raw_data):
            def eliminate_spaces(string):
                string = string[2::]
                string = string[:-4:]
                while string[0] == " ":
                    string = string[1::]
                while string[-1] == " ":
                    string = string[:-1:]
                return string

            def create_tupels(raw):
                
                def remove_spaces(string):
                    while string[0] == " ":
                        string = string[1::]
                    while string[-1] == " ":
                        string = string[:-1:]
                    return string

                raw = raw.split("=")

                return (remove_spaces(raw[0]),float(remove_spaces(raw[1])))
            
            return [create_tupels(eliminate_spaces(a)) for a in raw_data]

        raw_data = []
        with open("User_input.txt","r") as file:
            for line in file.readlines():
                raw_data.append(line)
        return second_correction(first_correction(raw_data))

    def create_formular(fehler):
        term=''
        for var in variablen:
            ableitung= str(diff(f,var))
            for i in range(len(fehler)):
                if fehler[i][0] == str(var):
                    term = term + "(" +ableitung+"*"+str(fehler[i][1])+  ")**2+"
        term = term[:-1]			
        return "sqrt(" + term + ")"


    def gauss(data,formular):
        #[[(ein csv Datenpunkt), Wert in Formel eingesetzt, GaussFehler],[...]]
      
        names, data_points = data
       
        def get_string(formel,data_tupel,names):

            def get_index_of_name(names, char):
                for i, name in enumerate(names):
                    if name == char:
                        return i

            output = ""
            for char in formel:
                if char in names:
                    output += str(data_tupel[get_index_of_name(names, char)])
                else:
                    output += char

            return output

        results = []
        for data_point in data_points:
            get_string(formular,data_point,names)
            results.append(eval(get_string(formular,data_point,names)))

        return results


    #Hier wird nun der tatsächliche Wert berechnet
    tats_wert = gauss(data,create_formular_actual_value())

    #Hier werden die Gauss Fehler berechnet
    gauss_Fehler = gauss(data,create_formular(read_User_input_file()))

    return (tats_wert,gauss_Fehler,create_formular_actual_value(),create_formular(read_User_input_file()))


