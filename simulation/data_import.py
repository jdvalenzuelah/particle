import csv

def read_csv(file_path):
    """
    Imports data from csv file formated as x,v
    """
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data
