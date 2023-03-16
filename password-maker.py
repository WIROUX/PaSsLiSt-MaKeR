#!/usr/bin/python3
#-------------------------------------
#=           made By SaDWX          =#
#-------------------------------------
#import
import itertools
import sys ,time
#from-import
from os import name , system
try:
    system("pip3 install --upgrade pip")
except:
    pass
#colorama install or not?
try:
    import colorama
except:
    print("installing libary colorama:")
    system("pip3 install colorama")
    import colorama
#urllib install or not?
try:
    import urllib
except:
    print("installing libary urllib:")
    system("pip3 install urllib")
    import urllib
#request install or not?
try:
    import requests
except:
    print("installing libary request:")
    system("pip3 install requests")
    import requests
from colorama import Fore
from time import sleep
def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    value = input()  
    return value
def clear():
    try:
        system("clear")
    except:
        system("cls")
clear()
typingPrint(Fore.RED+'''                                                              
           ▓▓▓▓▓▓▓▓▒░░░░░▒▒░░░░░░░▓
          ▓▓▓▓▓▓▓▓▒░░░░░▒▒▒░░░░░░░░▓
         ▓▓▓▓▓▓▓▓▒░░░░░░▒▒▒░░░░░░░░░▓
        █▓▓▓▓▓▓▓▓▒░░░░░░░▒▒▒░░░░░░░░░░
       ▓▓▓▓▓▓▓▓▒░░▒▓░░░░░░░░░░░░░░░░░
      ▓▓▓▓▓▓▓▓▒░▓████░░░░░▒▓░░░░░░░░░
     ▓▒▓▓▓▓▓▒░▒█████▓░░░░▓██▓░░░░░░░▒
    ▓▒▓▒▒▒░░▒███████░░░░▒████░░░░░░░░
   ▓▒▒▒░░▒▓████████▒░░░░▓████▒░░░░░░▒
  ▓▒▒░░▒██████████▓░░░░░▓█████░░░░░░░
  ▓▒░░███████████▓░░░░░░▒█████▓░░░░░░
  ▓▒░▒██████████▓▒▒▒░░░░░██████▒░░░░░▓
  ▓▒░░▒███████▓▒▒▒▒▒░░░░░▓██████▓░░░░▒
   ▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░███████▓░░░▓
   ▓░░░░░▒▒▒▓▓▒▒▒▒░░░░░░░░░██████▓░░░
    ▓▒▒▒▒▓▓▓▓▓▓▒▒▓██▒░░░░░░░▓███▓░░░░
          ▓▓▓▓▒▒█████▓░░░░░░░░░░░░░░
         ▓▓▓▓▒▒░▓█▓▓██░░░░░░░░░░░░░
       ▓▓▓▓▓▒▒▒░░░░░░▒░░░░░░░░░░░░
      ▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░▒▓
      ▓▓▓▓▓▒▒▒░░░░░░░░░░░░░░░▓
      ▓▓▓▓▒▒██████▒░░░░░░░░░▓
      ▓▓▓▒▒█████████▒░░░░░░▓
      ▓▓▒▒███████████░░░░░▒
      ▓▓░████████████░░░░▒
      ▓░░████████████░░░░
      ▓░▓███████████▒░░░
      ▓░███████████▓░░░
      ▓░███████████░░░
      ▓▒██████████░░░
      ▒▒█████████▒░▓
      ░▒████████▓░
      ░▓████████░
      ░████████░▒
     ▓░███████▒░
     ▒░███████░▓
     ░▒██████░░
     ░▒█████▓░
     ░▓█████░▒
     ░▓████▒░
     ░▓███▓░▓
      ░▓▓▒░▓
       ▒░▒

'''+Fore.CYAN+'''SaDWX'''+Fore.RED+'''                                                                  
'''+Fore.CYAN+'''                     💀+++++++++++'''+Fore.RED+'''<'''+Fore.MAGENTA+'''Coded by SaDWX'''+Fore.RED+'''>'''+Fore.CYAN+'''++++++++++💀
'''+Fore.YELLOW+'''                      ---------------------------------------\n'''
+Fore.LIGHTGREEN_EX+'''                      ☠='''+Fore.RED+'''            ['''+Fore.CYAN+'''01'''+Fore.RED+''']'''+Fore.MAGENTA+''' Start            '''+Fore.LIGHTGREEN_EX+'''=☠\n'''
+Fore.LIGHTGREEN_EX+'''                      ☠='''+Fore.RED+'''            ['''+Fore.CYAN+'''02'''+Fore.RED+''']'''+Fore.MAGENTA+''' Developer        '''+Fore.LIGHTGREEN_EX+'''=☠\n'''
+Fore.LIGHTGREEN_EX+'''                      ☠='''+Fore.RED+'''            ['''+Fore.CYAN+'''03'''+Fore.RED+''']'''+Fore.MAGENTA+''' other tools      '''+Fore.LIGHTGREEN_EX+'''=☠\n'''
+Fore.LIGHTGREEN_EX+'''                      ☠='''+Fore.RED+'''            ['''+Fore.CYAN+'''04'''+Fore.RED+''']'''+Fore.MAGENTA+''' exit tool        '''+Fore.LIGHTGREEN_EX+'''=☠\n'''
+Fore.YELLOW+'''                  💀---------------------------------------💀\n''')
wx = typingInput(Fore.CYAN+'Please Enter Number For Use'+Fore.YELLOW+':')
if wx == '1':
    posschar=typingInput(Fore.CYAN+'Password list'+Fore.LIGHTGREEN_EX+' character '+Fore.RED+'+'+Fore.YELLOW+'--'+Fore.MAGENTA+'>>>')
    repeatnum=typingInput(Fore.LIGHTGREEN_EX+'Number '+Fore.RED+'of '+Fore.LIGHTGREEN_EX+'characters '+Fore.RED+'in '+Fore.YELLOW+'the password list '+Fore.RED+'+'+Fore.YELLOW+'--'+Fore.MAGENTA+'>>>')
    file=open("SaDWXpAsSlIsT.txt","a")
    letters=itertools.product(posschar,repeat=int(repeatnum))
    typingPrint(Fore.CYAN+'Please Wait'+Fore.MAGENTA+'....'+Fore.CYAN+'...\n')
    for i in letters:
        file.write("".join(i)+'\n')
    file.close()
    print(Fore.RED+"Boooooom! file is here! name: SaDWXpAsSlIsT.txt")
    time.sleep(5)
    clear()
elif wx == '2':
    system('clear')
    system('xdg-open https://t.me/SaDWX_TM_CH')
elif wx == '3':
    clear()
    typingPrint(Fore.RED+'''
           ▄▄▄▄
         ▄██████      ▄▄▄█▄
       ▄██▀░░▀██▄    ████████▄
      ███░░░░░░██      █▀▀▀▀▀██▄▄
     ▄██▌░░░░░░░██    ▐▌        ▀█▄
     ███░░▐█░█▌░██    █▌          ▀▌'''+Fore.CYAN+'''SaDWX'''+Fore.RED+'''
    ████░▐█▌░▐█▌██   ██
   ▐████░▐░░░░░▌██   █▌
    ████░░░▄█░░░██  ▐█
    ████░░░██░░██▌  █▌
    ████▌░▐█░░███   █
    ▐████░░▌░███   ██
     ████░░░███    █▌
   ██████▌░████   ██
 ▐████████████  ███
 █████████████▄████
██████████████████
██████████████████
█████████████████▀
█████████████████
████████████████
████████████████
    '''+Fore.CYAN+'''                     💀+++++++++++'''+Fore.RED+'''<'''+Fore.MAGENTA+'''Coded by SaDWX'''+Fore.RED+'''>'''+Fore.CYAN+'''++++++++++💀
    '''+Fore.YELLOW+'''                    ---------------------------------------\n'''
    +Fore.LIGHTGREEN_EX+'''                        ☠='''+Fore.RED+'''          ['''+Fore.CYAN+'''01'''+Fore.RED+''']'''+Fore.MAGENTA+''' Admin panel finder WX '''+Fore.LIGHTGREEN_EX+'''=☠\n'''
    +Fore.LIGHTGREEN_EX+'''                        ☠='''+Fore.RED+'''          ['''+Fore.CYAN+'''02'''+Fore.RED+''']'''+Fore.MAGENTA+''' SMS bomber            '''+Fore.LIGHTGREEN_EX+'''=☠\n'''
    +Fore.LIGHTGREEN_EX+'''                        ☠='''+Fore.RED+'''          ['''+Fore.CYAN+'''03'''+Fore.RED+''']'''+Fore.MAGENTA+''' Developer             '''+Fore.LIGHTGREEN_EX+'''=☠\n'''
    +Fore.LIGHTGREEN_EX+'''                        ☠='''+Fore.RED+'''          ['''+Fore.CYAN+'''04'''+Fore.RED+''']'''+Fore.MAGENTA+''' exit tools            '''+Fore.LIGHTGREEN_EX+'''=☠\n'''
    +Fore.YELLOW+'''                         💀---------------------------------------💀\n''')
    Sad = typingInput(Fore.CYAN+'Please Enter Number For Use Tools '+Fore.RED+':')
    if Sad== '1':
        clear()
        system('pkg update -y && pkg upgrade -y && pkg install python2 -y && git clone https://github.com/WIROUX/panel_admn_finder_WX && cd panel_admn_finder_WX && chmod +x panel_finderWX.py && python2 panel_finderWX.py')
        clear()
    elif Sad== '2':
        clear()
        system('pkg update -y && pkg upgrade -y && pkg install git -y && pkg install python3 && git clone https://github.com/WIROUX/SBWX && cd SBWX && python3 SBWX.py')
    elif Sad== '3':
        clear()
        system('xdg-open https://t.me/ridam_dash')
    elif Sad == '4':
        clear()
        exit()
elif wx == '4':
    clear()
    exit()