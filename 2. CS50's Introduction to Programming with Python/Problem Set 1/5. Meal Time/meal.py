def main():
    string = input("What time is it? ")

    if (convert(string) >= 7.0 and convert(string) <= 8.0):
        print ("breakfast time")
    elif (convert(string) >= 12.0 and convert(string) <= 13.0):
        print ("lunch time")
    elif (convert(string) >= 18.0 and convert(string) <= 19.0):
        print ("dinner time")

def convert(time):
    hours, minutes = time.split(":")

    hours = int(hours)
    minutes = int(minutes) / 60
    hours += minutes

    return hours
if __name__ == "__main__":
    main()
