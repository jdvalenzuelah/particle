import csv

def read_csv(file_path):
    """
    Imports data from csv file formated as x,y,v
    """
    data = {}
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            _, y, v = row.items()
            data[float(row['x'])] = dict(map(lambda t: (t[0], float(t[1])), [y,v]))
    return data
