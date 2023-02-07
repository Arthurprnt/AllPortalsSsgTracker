import csv

def opencsv(path):
    file = open(path)
    file_csv = csv.reader(file, delimiter=",")
    return list(file_csv)

def updateoverlay(nb_portal):
    ov_file = open("overlay/progress.txt", "w")
    ov_file.write(f"Portal {nb_portal}/128")
    ov_file.close()