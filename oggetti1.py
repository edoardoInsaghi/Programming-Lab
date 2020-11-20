class CSVFile:

    def __init__(self, name):
        self.name = name

    def get_data(self):

        file = open(self.name,"r")

        total_values = []

        for line in file:
            elements=line.split(",")

            if elements[0] != "Date":
                value=elements[1]
                
                try:
                    total_values.append(float(value))

                except:
                    print("errore scpnosciuto alla linea {}".format(line))    

        file.close()
        return(total_values)


file = CSVFile('shampoo_sales.csv')
dati = file.get_data()
print(file.name)
print(dati)