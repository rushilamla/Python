#WAP that inputs a text file. The program should print all of the unique words in file in alphabatical order

file = open("sample1", "w")
file.write("welcome to python\nbye python")
file.close()

file = open("sample1", "r")
f = file.readlines()
un=[]

for i in f:
    for j in i.split():
        un.append(j)
un=set(un) #to remove duplicates 
un=list(un) #so that we can use sort function 
un.sort()

for i in un:
    print(i)
file.close()