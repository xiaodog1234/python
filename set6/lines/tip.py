#comment
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #return round(float(d.replace("$","")),1)
    #return round(float(d.lstrip("$")),1)
    return round(float(d.removeprefix("$")),1)
def percent_to_float(p):
    #return round(float(p.replace("%",""))/100,2)
    #return round(float(p.rstrip("%"))/100,2)
    return round(float(p.removesuffix("%"))/100,2)

main()
