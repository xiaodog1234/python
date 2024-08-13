import sys
import csv
#https://pypi.org/project/tabulate/
from tabulate import tabulate

if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    menu = []
    try:
        with open(sys.argv[1],"r") as file:
            dict_reader  = csv.DictReader(file)
            #get header row and assigns it to headers
            headers = dict_reader.fieldnames
            for line in dict_reader:
                #https://stackoverflow.com/questions/28836781/reading-column-names-alone-in-a-csv-file
                menu.append({headers[0]:line[headers[0]],headers[1]:line[headers[1]],headers[2]:line[headers[2]]})
                #print("headers[0]: ", headers[0])
                #print("line[headers[0]]: ", line[headers[0]])
            #csv_reader = csv.reader(file, delimiter = ',')
        print(tabulate(menu, headers="keys",tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")
