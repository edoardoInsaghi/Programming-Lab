from matplotlib import pyplot as plt


class CSVTimeSeriesFile:
    def __init__(self, name=None):
        self.name = name

    def get_data(self):
        """
        Controllo che sia stato inserito il file, che sia
        una stringa e provo ad aprirlo. Se una delle precedenti
        azioni fallisce sollevo un'eccezione.
        """
        if not isinstance(self.name, str) or self.name is None:
            raise ExamException('Invalid or missing file.')
        try:
            file = open(self.name, "r")
        except:
            raise ExamException('An error occurred while reading the file.')

        time_series = []
        i = -1
        for line in file:
            line_data = line.split(',')
            """
            Convertendo i timestamps in interi e le temperature
            in floating points, controllo che entrambi 
            esistano e che siano accettabili.
            Altrimenti si passa all'iterazione successiva.
            """
            try:
                line_data[1] = float(line_data[1])
                line_data[0] = int(float(line_data[0]))
                if line_data[0] < 0:
                    continue
            except:
                continue

            time_series.append([line_data[0], line_data[1]])

            """
            Controllo che ogni timestamp accettato sia maggiore del
            precedente, altrimenti sollevo un'eccezione.
            """
            i += 1
            if i > 0 and time_series[i][0] <= time_series[i-1][0]:
                raise ExamException('Epochs not in order.')

        return time_series


def daily_stats(time_series):
    """
    Costruisco un dizionario nel quale ad ogni giorno corrisponde una lista
    che contiene tutte le misurazioni effettuate il giorno medesimo.
    """
    log = {}
    for line in time_series:
        """"
        la variabile 'day_counter' indica il giorno a cui appartiene la misurazione.
        """
        day_counter = line[0] // 86400
        if day_counter not in log:
            log[day_counter] = [line[1]]
        else:
            log[day_counter].append(line[1])

    """
    Calcolo i valori di minimo, massimo e media per ogni giorno,
    e li inserisco in una nuova lista.
    """
    result = []
    for key, values in log.items():
        MEAN = sum(values) / len(values)
        MAX = max(values)
        MIN = min(values)
        result.append([MIN, MAX, MEAN])

    """
    for i in range(len(result)):
        print(result[i][0], '\t||\t', result[i][1], '\t||\t', round(result[i][2], 2))
    """

    return result


def plot(data):
    font = {'family': 'serif',
            'color': 'black',
            'weight': 'normal',
            'size': 16
            }

    i = 0
    x_val = []
    y_max = []
    y_mean = []
    y_min = []
    for line in data:
        i += 1
        x_val.append(i)
        y_min.append(line[0])
        y_max.append(line[1])
        y_mean.append(line[2])

    plt.plot(x_val, y_min, color='blue')
    plt.plot(x_val, y_max, color='red')
    plt.plot(x_val, y_mean, color='black')
    plt.title("Temperature over one month", fontdict=font)
    plt.ylabel('max\navg\nmin', rotation=0, loc='top')
    plt.xlabel('days', loc='right')
    plt.show()


class ExamException(Exception):
    pass


"""
time_series_file = CSVTimeSeriesFile('data.csv')
time_series = time_series_file.get_data()
stats = daily_stats(time_series)
plot(stats)
"""

