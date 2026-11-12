text = "The dog and the cat and the mouse"
# the 3
# and 2
# dog 1, cat 1, mouse 1

text = text.lower()
text = text.split()

words = {

}

for word in text:
    if word in words.keys():
        words[word] += 1
    else:
        words[word] = 1

print(words)