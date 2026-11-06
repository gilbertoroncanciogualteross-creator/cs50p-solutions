# Implement a program that prompts the user for the answer to the
# Great Question of Life, the Universe and Everything.

answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")

answer = answer.lower()
answer = answer.replace(" ", "")

if answer == "42" or answer == "forty-two":
    print("Yes")
else:
    print("No")