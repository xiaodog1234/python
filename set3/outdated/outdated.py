month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    while True:
        date = input("Date ")
        if "/" in date:
            date = date.split("/")
            if int(date[1])>=1 and int(date[1])<=31:
                if date[0] in month:
                    continue
                elif int(date[0])<=12 and int(date[0])>=1:
                    date[0] = date[0].strip()
                    date[1] = date[1].strip()
                    date[2] = date[2].strip()
                    print(f"{date[2]}-{int(date[0]):02}-{int(date[1]):02}")
                    break
        elif " " in date:
            date = date.split(" ")
            if "," in date[1]:
                if date[0] in month and int(date[1].replace(",",""))<=31 and int(date[1].replace(",",""))>=1:
                    date[1] = date[1].replace(",","")
                    printDate(date)
                    break

def printDate(date):
    date[1] = date[1].strip()
    date[2] = date[2].strip()
    match date[0]:
        case "January":
            print(f"{date[2]}-01-{int(date[1]):02}")
        case "February":
            print(f"{date[2]}-02-{int(date[1]):02}")
        case "March":
            print(f"{date[2]}-03-{int(date[1]):02}")
        case "April":
            print(f"{date[2]}-04-{int(date[1]):02}")
        case "May":
            print(f"{date[2]}-05-{int(date[1]):02}")
        case "June":
            print(f"{date[2]}-06-{int(date[1]):02}")
        case "July":
            print(f"{date[2]}-07-{int(date[1]):02}")
        case "August":
            print(f"{date[2]}-08-{int(date[1]):02}")
        case "September":
            print(f"{date[2]}-09-{int(date[1]):02}")
        case "October":
            print(f"{date[2]}-10-{int(date[1]):02}")
        case "November":
            print(f"{date[2]}-11-{int(date[1]):02}")
        case "December":
            print(f"{date[2]}-12-{int(date[1]):02}")
        case _:
            print("Error no matching month")

main()
