#!/usr/bin/env python3
import os, requests, sys, time
from colorama import init, Fore, Style
from concurrent.futures import ThreadPoolExecutor
from socket import gethostbyname

init()
r = Fore.RED + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
oo = Fore.YELLOW + Style.BRIGHT
o = Fore.RESET + Style.RESET_ALL

banner = """
   (                              (    (     
{}  )\ )        )        *   )     )\ ) )\ )  
{} (()/( (   ( /(   (  ` )  /(    (()/((()/(  
{}  /(_)))\  )\()) ))\  ( )(_))(   /(_))/(_)) 
{} (_)) ((_)(_))/ /((_)(_(_()) )\ (_)) (_))   
{} / __| (_)| |_ (_))  |_   _|((_)|_ _|| _ \  
{} \__ \ | ||  _|/ -_)   | | / _ \ | | |  _/  
{} |___/ |_| \__|\___|   |_| \___/|___||_|    
                                             

{} https://xploitsec.com - Underground Forum

            """.format(g, r, oo, c, r, g, r, o)


def sitetoip(i):
    try:
        ip = gethostbyname(i)
        print('{}[+] '"{}{} ""{} ==> ""{}[{}]".format(c, o, i, o, g, ip))
        open('ips.txt', 'a').write(ip + '\n')
    except:
        print('{}[-] '"{}{}""{} ==> ""{}[ ERROR ]".format(r, o, i, o, r))

def Main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)

    lists = input('\n{}[+] {}Website List{} > {}'.format(o, r, o, r))
    thread = input('{}[+] {}Thread{} > {}'.format(o, r, o, c))
    print('')
    try:
        domain = lists.replace('"','')
        process = open(domain, 'r').read().splitlines()
        with ThreadPoolExecutor(max_workers=int(thread)) as e:
            [e.submit(sitetoip, i) for i in process]
    except:
          print('{}[!] {}Incorrect'.format(o, r))
        
if __name__ == '__main__':
    Main()
