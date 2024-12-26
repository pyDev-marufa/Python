

#the len function expects a data type: String not int

print(len("Hello"))

print(type(123))


#conversion

print(int("123") + int("456"))

#value error
# print(int("abd") + int("123"))



#concatenation 
name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)


print("Number of letters in your name: " + str(len(length_of_name)))