import os
import curses
import sys, tty, termios
import sys
import time

def getch(char_width=1):
    '''get a fixed number of typed characters from the terminal. 
    Linux / Mac only'''
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(char_width)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


sys.stdout.write("\x1b]2;Spotify Patcher\x07")
os.system("printf '\e[9;1t'")
os.system('clear')


home = os.path.expanduser('~')
oldspotifysettings = home+'/Library/Application Support/Spotify/prefs'

class bcolors:
    HEADER = '\033[95m'
    CYAN = '\u001b[36m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    MAGENTA = '\u001b[35m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


logo = (f'''{bcolors.FAIL}
  ██████  ██▓███   ▒█████  ▄▄▄█████▓ ██▓  █████▒▓██   ██▓   
▒██    ▒ ▓██░  ██▒▒██▒  ██▒▓  ██▒ ▓▒▓██▒▓██   ▒  ▒██  ██▒   
░ ▓██▄   ▓██░ ██▓▒▒██░  ██▒▒ ▓██░ ▒░▒██▒▒████ ░   ▒██ ██░   
  ▒   ██▒▒██▄█▓▒ ▒▒██   ██░░ ▓██▓ ░ ░██░░▓█▒  ░   ░ ▐██▓░   
▒██████▒▒▒██▒ ░  ░░ ████▓▒░  ▒██▒ ░ ░██░░▒█░      ░ ██▒▓░   
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░ ▒░▒░▒░   ▒ ░░   ░▓   ▒ ░       ██▒▒▒    
░ ░▒  ░ ░░▒ ░       ░ ▒ ▒░     ░     ▒ ░ ░       ▓██ ░▒░    
░  ░  ░  ░░       ░ ░ ░ ▒    ░       ▒ ░ ░ ░     ▒ ▒ ░░     
      ░               ░ ░            ░           ░ ░        
                                                 ░ ░        
 ██▓███   ▄▄▄     ▄▄▄█████▓ ▄████▄   ██░ ██ ▓█████  ██▀███  
▓██░  ██▒▒████▄   ▓  ██▒ ▓▒▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▒██  ▀█▄ ▒ ▓██░ ▒░▒▓█    ▄ ▒██▀▀██░▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒░██▄▄▄▄██░ ▓██▓ ░ ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░ ▓█   ▓██▒ ▒██▒ ░ ▒ ▓███▀ ░░▓█▒░██▓░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░ ▒▒   ▓▒█░ ▒ ░░   ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░       ▒   ▒▒ ░   ░      ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░
░░         ░   ▒    ░      ░         ░  ░░ ░   ░     ░░   ░ 
               ░  ░        ░ ░       ░  ░  ░   ░  ░   ░     
                           ░                                
{bcolors.ENDC}''')

print(logo)
print(f'\n{bcolors.OKBLUE}=>{bcolors.ENDC} {bcolors.UNDERLINE}Welcome to the Spotify Patcher{bcolors.ENDC}')
def install():
  print(f'{bcolors.OKBLUE}=>{bcolors.ENDC} This script will proceed to install the required dependencies to implement the tor network into the Spotify client.')

  input(f'\n{bcolors.OKBLUE}Press {bcolors.OKGREEN}ENTER{bcolors.OKBLUE} to continue...{bcolors.ENDC}')
  os.system('clear')

  print(f'\n{bcolors.FAIL}=>{bcolors.ENDC} By running this script you are agreeing to take {bcolors.UNDERLINE}full responsibility.{bcolors.ENDC}')
  print(f'\n{bcolors.OKBLUE}=>{bcolors.ENDC} This script will proceed to install {bcolors.OKGREEN}tor{bcolors.ENDC} for free, which will be able configured on Spotify.')
  print(f'{bcolors.OKBLUE}=>{bcolors.ENDC} For the geeks, this script installs Homebrew and sets-up a Tor SOCKS proxy which routes the tor network, then it configures spotify to use the Tor SOCKS proxy.')
  print(f'{bcolors.OKGREEN}=>{bcolors.ENDC} The next page may ask you for your Mac Password so that it can {bcolors.OKGREEN}properly install{bcolors.ENDC} the programs.')

  input(f'\n{bcolors.OKBLUE}Press {bcolors.OKGREEN}ENTER{bcolors.OKBLUE} to continue...{bcolors.ENDC}')
  os.system('clear')
  print(f'{bcolors.FAIL}=>{bcolors.ENDC} You may be asked for your MacBook password to proceed with the installation.')
  os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"')
  time.sleep(3)
  os.system('clear')
  print(f'{bcolors.OKGREEN}=>{bcolors.ENDC} Homebrew Installation {bcolors.OKGREEN}successful{bcolors.ENDC}!')
  print(f'{bcolors.OKGREEN}=>{bcolors.ENDC} Proceeding to attempt to install VPN... (Tor Proxy)')
  print(f'{bcolors.WARNING}-----------{bcolors.ENDC}')
  os.system('brew install Tor')
  time.sleep(3)
  os.system('clear')
  print(f'{bcolors.OKGREEN}=>{bcolors.ENDC} Tor/VPN Service Installation {bcolors.OKGREEN}successful{bcolors.ENDC}!')
  print(f'{bcolors.OKGREEN}=>{bcolors.ENDC} Starting VPN Service... (Tor Proxy)')
  print(f'{bcolors.WARNING}-----------{bcolors.ENDC}')
  print(f'{bcolors.FAIL}=>{bcolors.ENDC} You may be asked for your Mac password to finish the installation.')
  os.system('sudo brew services start Tor')
  time.sleep(3)
  os.system('clear')

  print(f'{bcolors.OKGREEN}=>{bcolors.ENDC} Started {bcolors.OKGREEN}Tor/VPN Service{bcolors.ENDC}!')
  print(f'{bcolors.FAIL}=>{bcolors.ENDC} Applying {bcolors.OKGREEN}Spotify Patch{bcolors.ENDC}...\n')

  os.system('killall -9 Spotify >/dev/null 2>&1')

  badvar1 = 'network.proxy.mode='
  badvar2 = 'network.proxy.addr='

  newset = [line.rstrip('\n') for line in open(oldspotifysettings)]

  newset.insert(2, 'network.proxy.mode=4')
  newset.insert(7, 'network.proxy.addr="127.0.0.1:9050@socks5"')
  newset.insert(8, 'core.clock_delta=0')

  with open(oldspotifysettings, mode='wt', encoding='utf-8') as myfile:
      myfile.write('\n'.join(newset))

  print(logo)
  print(f'\n{bcolors.OKGREEN}=>{bcolors.ENDC} {bcolors.UNDERLINE}Applied {bcolors.OKGREEN}Spotify Patch{bcolors.ENDC}!')
  print(f'{bcolors.OKGREEN}=>{bcolors.ENDC} Start {bcolors.OKGREEN}Spotify{bcolors.ENDC} and you should be able to connect normally. (connection may be slightly slower than usual)')
  input(f'\n{bcolors.OKBLUE}Press {bcolors.OKGREEN}ENTER{bcolors.OKBLUE} to close...{bcolors.ENDC}')
  sys.exit(0)
def remove():
  print(f'{bcolors.OKBLUE}=>{bcolors.ENDC} This script will proceed to remove the installed Tor dependencies and Spotify proxy configuration.')

  input(f'\n{bcolors.OKBLUE}Press {bcolors.OKGREEN}ENTER{bcolors.OKBLUE} to continue...{bcolors.ENDC}')
  os.system('clear')

  print(f'\n{bcolors.FAIL}=>{bcolors.ENDC} By running this script you are agreeing to take {bcolors.UNDERLINE}full responsibility.{bcolors.ENDC}')
  print(f'{bcolors.OKGREEN}=>{bcolors.ENDC} It may ask you for your Mac Password so that it can {bcolors.OKGREEN}properly uninstall{bcolors.ENDC} the programs.')
  os.system('clear')
  print(f'{bcolors.OKGREEN}=>{bcolors.ENDC} Proceeding to attempt to uninstall Tor and Homebrew...')
  print(f'{bcolors.WARNING}-----------{bcolors.ENDC}')
  os.system('brew uninstall Tor')
  os.system('sudo /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall.sh)"')
  os.system('clear')
  print(f'{bcolors.OKGREEN}=>{bcolors.ENDC} Homebrew and Tor uninstallation {bcolors.OKGREEN}successful{bcolors.ENDC}!')
  print(f'{bcolors.OKGREEN}=>{bcolors.ENDC} Resetting Spotify configuration...')
  print(f'{bcolors.WARNING}-----------{bcolors.ENDC}')
  os.system('killall -9 Spotify >/dev/null 2>&1')
  open(oldspotifysettings, "w").close()
  print(logo)
  print(f'\n{bcolors.OKGREEN}=>{bcolors.ENDC} {bcolors.UNDERLINE}Removed {bcolors.OKGREEN}Spotify Patch{bcolors.ENDC}!')
  print(f'{bcolors.OKGREEN}=>{bcolors.ENDC} Start {bcolors.OKGREEN}Spotify{bcolors.ENDC} and you should be able to connect normally without Tor')
  input(f'\n{bcolors.OKBLUE}Press {bcolors.OKGREEN}ENTER{bcolors.OKBLUE} to close...{bcolors.ENDC}')
  sys.exit(0)

print(f"\n{bcolors.FAIL}[{bcolors.ENDC}1{bcolors.FAIL}]{bcolors.ENDC} Install and apply Tor to Spotify")
print(f"{bcolors.FAIL}[{bcolors.ENDC}2{bcolors.FAIL}]{bcolors.ENDC} Remove and uninstall Tor from Spotify")
loop = True
while loop:
    preference = (getch())
    if preference.upper() == "1":
        install()
        loop=False

    elif preference.upper() == "2":
        remove()
        loop=False
    else:
        sys.exit(0)