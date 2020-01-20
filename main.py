from textblob import TextBlob

file = open("Text_file.txt", "r+")
a = file1.read()

print("Original text : ", str(a))

b = TextBlob(a)

print("Correct text : " + str(b.correct()))
file1.close()

d = open("Text_file.txt", "w")
d.write(str(b.correct()))
d.close()