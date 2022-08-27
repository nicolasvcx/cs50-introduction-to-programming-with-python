string = input("Input: ")
print("Output: ", end="")
for i in string:
    if i.lower() in ("a","e","i","o","u"):
        continue
    else:
        print(i, end="")

print("")