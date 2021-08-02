import pdb
# colorize(34, "red")

a=int(input("enter your name"))
if(type(a) is str ):
    raise ValueError('Kindly enter a valid value')
print(a)
# try:
#     ade
# except:
#     print(TypeError('undefine variable'))
# try:
#     num = int(input('Enter your value'))
# except:
#     print("Is not a valid number")
# finally:
#     print('Run no matter what')
first="Sunday"
Surname="Omolewu"
fullname=first + Surname
pdb.set_trace()
print(fullname)