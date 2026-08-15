marks = [20,30,40,50,60,"ilma"]
print(marks)        #print full list
print(marks[:5])    #20,30,40,50,60,
print(marks[2])     #40
print(marks[1:4])   #30,40,50
print(len(marks))   #6
print(marks[-1])    #ilma
print(marks[-3:-1]) #50,60
print(marks[-3:len(marks)]) #50,60,ilma
print(marks[3:len(marks)])  #50,60,'ilma'
print(type(marks))   #list