class CSVFile:

    def __init__(self, name,):
        self.name = name

    def get_data(self, start=None, end=None):
        try:
            file = open(self.name,"r")
        except Exception as e:
            print('Errore nella lettura del file: "{}"'.format(e))

        if not isinstance(self.name, str):
            raise Exception( "Il nome del file non e' una stringa" )     

        total_values = []
        counter = 0

        for line in file:
            
            elements=line.split(",")

            if elements[0] != "Date":
                value=elements[1]
                if counter >= start and counter <= end:
                    try:
                        total_values.append(float(value))

                    except:
                        print("errore sconosciuto alla linea {}".format(counter))

            counter += 1

        file.close()
        return total_values

    def predict(self, lista):
        diff = lista[-1] - lista[0]
        diff_media = diff/(len(lista)-1)

        return lista[-1] + diff_media


file = CSVFile('shampoo_sales.csv')
#dati = file.get_data(5,8)
#print(file.name)
#print(dati)
lista = file.get_data(0, 37)
x = file.predict(lista)
print(x)