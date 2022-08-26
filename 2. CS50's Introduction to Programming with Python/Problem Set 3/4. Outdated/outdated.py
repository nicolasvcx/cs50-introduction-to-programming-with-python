months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
};
def __main__():

        date = input("Date: ")
        if "/" in date:
            month, day, year = date.split("/")
            if month.isalpha():
                __main__()
            if int(day) > 31:
                __main__()
            if int(month) > 12:
                __main__()
            if len(day) == 1:
                day = "0" + day
            if len(month) == 1:
                month = "0" + month


            print(year + "-" + month + "-" + day)

        else:
            month, day, year = date.split(" ")
            day = day.replace(",", "")

            if month.isnumeric():
                __main__()
            if day.isalpha():
                __main__()
            if len(day) == 1:
                day = "0" + day

            for i in months:
                if months[i] == month:
                    if i < 10:
                        month = "0" + str(i)
                    else:
                        month = str(i)

            if int(day) > 31:
                __main__()
            if int(month) > 12:
                __main__()



            print(year + "-" + month + "-" + day)

__main__()