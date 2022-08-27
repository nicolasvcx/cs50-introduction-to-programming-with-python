print("What is the Answer to the Great Question of Lige, the Universe, and Everything? " , end="")
answer = input()
if (answer.lower() == "forty-two" or answer.lower() == "forty two" or answer.replace(" ", "") == "42"):
    print("Yes")
else:
    print("No")

