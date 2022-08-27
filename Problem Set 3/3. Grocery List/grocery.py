list  = {}

while True:
    try:
        item = input().upper()
        if item in list:
            list[item] += 1
        else:
            list[item] = 1

    except EOFError:
        for key, value in sorted(list.items()):
            print(value, key)
        break
