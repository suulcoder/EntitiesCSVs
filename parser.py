import csv

with open('Aldea.csv', 'r') as infile, open('NeAldea.csv', 'w',newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerows(reader)