

text = open("day6-data.txt").read()

for i in range(len(text) - 14):
    letters = text[i:i+14]
    if len(letters) == len(set(letters)):
        print(letters)
        print(i+14)
        break
