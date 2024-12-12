# create a text file "myfile" in python and ask the user to write seperate 3 lines with 3 input statements from the user
file=open("myfile","w")
x=input("Enter line 1:")
y=input("Enter line 2:")
z=input("Enter line 3:")
file.write(x+"\n")

file.write(y+"\n")

file.write(z+"\n")

file.close()

file=open("myfile","r")
print(file.read())
file.close()