def main():
    time = convert(input("What time is it? "))
    #print(time)
    #if time >= 7 and time <=8:
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <=13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    if "a.m." in time:
        hours, minutes = time.replace(" a.m.","").split(":")
        if int(hours) > 12:
            return float(hours) - 12 + (float(minutes)/60)
        elif int(hours) == 12:
            return 24 + (float(minutes)/60)
        else:
            return float(hours) + (float(minutes)/60)
    elif "p.m." in time:
        hours, minutes = time.replace(" p.m.","").split(":")
        if int(hours) < 12:
            return float(hours) + 12 + (float(minutes)/60)
        else:
            return float(hours) + (float(minutes)/60)
    else:
        hours, minutes = time.split(":")
        return float(hours) + (float(minutes)/60)

if __name__ == "__main__":
    main()
