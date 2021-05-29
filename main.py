import os
import ctypes
import colorama
import time
from colorama import Fore, Back, Style
colorama.init()
ctypes.windll.kernel32.SetConsoleTitleW("Shitty pinger I made in 5 minutes")
print(f"{Fore.RED}")
print("""

██████╗░██╗███╗░░██╗░██████╗░███████╗██████╗░
██╔══██╗██║████╗░██║██╔════╝░██╔════╝██╔══██╗
██████╔╝██║██╔██╗██║██║░░██╗░█████╗░░██████╔╝
██╔═══╝░██║██║╚████║██║░░╚██╗██╔══╝░░██╔══██╗
██║░░░░░██║██║░╚███║╚██████╔╝███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝░░╚═╝

""")
print(f"{Fore.BLUE}")




ip_to_check = input('type the ip:')

icmp_num = input('how many times to ping?:')


os.system('ping -n {} {}'.format(icmp_num, ip_to_check))

 
print(f"{Fore.GREEN}")
print("check complete!")
os.system('pause')

#the only reason I made this was bc it looks nice XD