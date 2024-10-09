# This script gets your IP information from https://www.showmyip.com/
#
# Modules used _
#               |-> requests: Make the HTTP request
#               |-> bs4: To extract the data that interests us (IP, country, ISP)
#               |-> colorama: It makes the output fancy
#
# by Diffuso, 09-10-2024

import requests
from bs4 import BeautifulSoup
from colorama import Fore, init

init(autoreset=True)

print(Fore.LIGHTWHITE_EX + '''
.d8888. db   db  .d88b.  db   d8b   db      .88b  d88. db    db      d888888b d8888b. 
88'  YP 88   88 .8P  Y8. 88   I8I   88      88'YbdP`88 `8b  d8'        `88'   88  `8D 
`8bo.   88ooo88 88    88 88   I8I   88      88  88  88  `8bd8'          88    88oodD' 
  `Y8b. 88~~~88 88    88 Y8   I8I   88      88  88  88    88            88    88~~~   
db   8D 88   88 `8b  d8' `8b d8'8b d8'      88  88  88    88           .88.   88      
`8888Y' YP   YP  `Y88P'   `8b8' `8d8'       YP  YP  YP    YP         Y888888P 88
''')
print(Fore.GREEN + "Loading...")
try:
    request = requests.get("https://www.showmyip.com/", headers = {'User-Agent' : 'Mozilla/5.0 kk'})
    soup = BeautifulSoup(request.text, 'html.parser')
    ip = soup.find('td', string="Your IPv4").find_next_sibling("td").text
    country = soup.find('td', string="Country").find_next_sibling("td").text
    isp = soup.find('td', string="Internet Service Provider (ISP)").find_next_sibling("td").text

    print(Fore.LIGHTCYAN_EX + "IP:", ip)
    print(Fore.LIGHTMAGENTA_EX + "Country:", country)
    print(Fore.LIGHTYELLOW_EX + "ISP:", isp)
    print(Fore.GREEN + "Done.")
except:
    print(Fore.RED + "Error.")