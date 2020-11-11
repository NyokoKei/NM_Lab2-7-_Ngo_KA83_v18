from pandas import read_csv
import csv


def csv_s(data, path):
    """
    To save results into .cvs file

    :param data: list of the outputs
    :param path: str, path to save
    :return: None
    """
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


def csv_e(path):
    """
    To extract first 4 entrances of 'Runge-Kutta h [h] .csv

    :param path: str
    :return: y0, y1, y2, y3
    """
    file = read_csv(path)
    y_0, y_1, y_2, y_3 = file['y_i'][0:4]
    return y_0, y_1, y_2, y_3