import requests
import colorama
import base64
from colorama import Fore

from datetime import datetime


while True:
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    date_time = datetime.fromtimestamp(ts)
    time = date_time.strftime("%H:%M:%S")
    x = requests.get('https://discord.com/api/v9/experiments')
    if x.status_code == 200:
        finger = x.json()['fingerprint']
        print( Fore.LIGHTRED_EX,"[",time,"]",Fore.CYAN,"{+} Fingerprint", finger)
        with open("fingerprint.txt", "a", encoding="utf-8") as file:
                    file.write(f"{finger}\n")
    else:
        print(Fore.RED,"{!} Eror Could not get fingerprint > ",x)
    x2 = requests.get('https://discord.com',timeout=5).cookies
    dcf = str(x2).split('__dcfduid=')[1].split(' ')[0]
    sdc = str(x2).split('__sdcfduid=')[1].split(' ')[0]
    print(Fore.LIGHTRED_EX,"[",time,"]",Fore.CYAN,"{+} Cookie",f'__dcfduid={dcf}; __sdcfduid={sdc}')
    with open("cookie.txt", "a", encoding="utf-8") as file:
                    file.write(f"__dcfduid={dcf}; __sdcfduid={sdc}\n")
