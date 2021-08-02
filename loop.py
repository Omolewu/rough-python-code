#For Loop
#while loop
#num=range(1,101)
# repeat=int(input("How many time do you want us to repeat your statement "))
# statement = input("Kindly enter your statement ")
# print(repeat)
# print(statement)
# for num in range(repeat):
#     print(f" {num + 1}  {statement * (num + 1)}")
# for char in "SUNDAY":
#     print(char)
userpassword=input("Kindly enter your password")
password="sunday"

while password != userpassword:
    print("incorrect password")
    userpassword=input("Kindly enter correct password")
else:
    print("Correct password you are good to go")

    
# a =1
# while a <= 20:
#     print(a)
#     a=a+1