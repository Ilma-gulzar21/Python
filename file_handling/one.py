f = open("text.txt", "r")

line_count =0
char_count=0
word_count=0


for line in f:
    line_count=line_count+1
    sentences = line.split(".")
    for words in line:
        word_count=word_count+1

    for ch in words:
           char_count=char_count+1

f.close()
print("total lines =",line_count)
print("total sentences = ",len(sentences))
print("total words = ", word_count)
print("total characters = ", char_count)       
