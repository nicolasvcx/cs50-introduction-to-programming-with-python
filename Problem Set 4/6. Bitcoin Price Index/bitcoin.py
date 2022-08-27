import requests
import sys


if len(sys.argv) == 2:
    for i in sys.argv[1]:
        if i in ("!","#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~","."):
            print("Command-line argument is not a number")
        elif sys.argv[1].isalpha():
            print("Command-line argument is not a number")
else:
    print("Missing command-line argument")

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    request = r.json()
    print("$",('{:,}'.format(float(request['bpi']['USD']['rate'].replace(",", "")) * float(sys.argv[1]))), sep='')
except requests.RequestException:
    print("RE")

