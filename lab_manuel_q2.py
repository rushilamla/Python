#write a program to illustrate iteration over the list and dictionary
l=[1,2,3,4,5]
for i in l:
    print(i,end=" ")
print("")
dict={"name":["rushil","piyush","aditya"],"age":[19,20,69]}
for j in dict.keys():
    print(j,end=" ")
print("")
for k in dict.values():
    print(k,end=" ")
