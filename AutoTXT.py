import time
import os
from colorama import Fore

logo = print(Fore.BLUE + """
AutoMatic TXT file maker
""")

laman = input("[+] Enter message: ")
print("")
print("FileName must contain .txt at last")
name = input("[+] Enter FileName: ")
open(name, 'w').write(laman)