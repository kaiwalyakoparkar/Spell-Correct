from textblob import TextBlob

file = open("Text_file.txt", "r+")
a = file.read()

print("Original text : ", str(a))

b = TextBlob(a)

print("Correct text : " + str(b.correct()))
file.close()

d = open("Text_file.txt", "w")
d.write(str(b.correct()))
d.close()
