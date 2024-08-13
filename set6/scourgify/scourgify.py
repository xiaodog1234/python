import sys
import csv

if len(sys.argv) <3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
elif not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    students = []
    try:
        with open(sys.argv[1],"r") as file:
            reader = csv.DictReader(file)
            #students.append({"first":"first","last":"last","house":"house"})
            for row in reader:
                lastname,firstname = row["name"].split(",")
                students.append({"first": firstname.strip(),"last":lastname.strip(),"house":row["house"]})
        #print(students)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    try:
        with open(sys.argv[2],"w") as file:
            writer = csv.DictWriter(file, fieldnames=["first","last","house"])
            #writer.writerow({"first":"first","last":"last","house":"house"})
            writer.writeheader()
            for student in students:
                writer.writerow({"first":student["first"],"last":student["last"],"house":student["house"]})
    except FileNotFoundError:
        sys.exit("File does not exist")
