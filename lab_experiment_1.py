#WAP to demonstrate type checking of various data types and demonstrate the use of following built in functions in python
# ex:- abs(), len(), min(), round(), isalnum(), type()


a=-5
b=5.5
c="hello"
li=[1,2,3,4,5,6]
print(type(a))
print(type(b))
print(type(c))
print(type(li))

x=-110
print("Absolute value of {} is {}".format(x,abs(x)))
print("length of string is:",len(c))
print("Minimum value in the list is:",min(li))
print("Round-off of {} is {}".format(b,round(b)))
print("Is the string alphanumeric?",c.isalnum())

