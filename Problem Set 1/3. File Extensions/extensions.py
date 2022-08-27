string = input("File name: ")
string = string.split(".", 1)[1].lower().replace(" ","")
if (string == "gif"):
    print("image/gif")
elif (string == "jpeg" or string == "jpg"):
    print("image/jpeg")
elif (string == "png"):
    print("image/png")
elif (string == "pdf"):
    print("application/pdf")
elif (string == "txt"):
    print("text/plain")
elif (string == "zip"):
    print("application/zip")
else:
    print("application/octet-stream")