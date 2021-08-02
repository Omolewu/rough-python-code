import sys
from termcolor import colored, cprint
import pyfiglet
# from random import randint
# print(help(termcolor))
text= colored("Hello python Module", color="white", on_color="on_blue", attrs=['reverse',"bold"])
print(text)
help(pyfiglet.figlet_format)