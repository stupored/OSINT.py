import webbrowser, colorama, requests
from requests import get
from colorama import Fore
#https://github.com/stupored/

print(f'''{Fore.RESET}
           {Fore.CYAN}115 116 117 112 111 114{Fore.RESET}
────────────────────{Fore.CYAN}OSINT{Fore.RESET}────────────────────
{Fore.CYAN}phone{Fore.RESET}     phone number lookup, usa
{Fore.CYAN}email{Fore.RESET}     email lookup
{Fore.CYAN}ip{Fore.RESET}        ip lookup
{Fore.CYAN}ssn{Fore.RESET}       ssn lookup
────────────────────{Fore.CYAN}OSINT{Fore.RESET}────────────────────
any link with a {Fore.CYAN}!{Fore.RESET} is a manual use and will not
take your inputted value
────────────────────{Fore.CYAN}OSINT{Fore.RESET}────────────────────''')
x = input("OSINT:> ")
if x == 'phone':
	x113 = input('first 3 digits: ')
	x112 = input('second 3 digits: ')
	x111 = input('last 4 digits: ')
	webbrowser.open(f'https://800notes.com/Phone.aspx/1-{x113}-{x112}-{x111}', new=2, autoraise=True)
	webbrowser.open(f'https://www.okcaller.com/detail.php?number={x113}{x112}{x111}', new=2, autoraise=True)
	webbrowser.open(f'https://www.us-info.com/en/usa', new=2, autoraise=True)
	webbrowser.open(f'https://www.thisnumber.com/{x113}-{x112}-{x111}', new=2, autoraise=True)
	webbrowser.open(f'https://www.searchbug.com/peoplefinder/phone-search.aspx?TYPE=phonerev&TAG=people&FULLPHONE={x113}{x112}{x111}', new=2, autoraise=True)
	print(f'''
──{Fore.CYAN}{x113}-{x112}-{x113}{Fore.RESET}────────────────────────────────────────
opened {Fore.GREEN} https://800notes.com/Phone.aspx/1-{x113}-{x112}-{x111}{Fore.RESET}
opened {Fore.GREEN} https://www.okcaller.com/detail.php?number={x113}{x112}{x111}{Fore.RESET}
opened{Fore.CYAN}!{Fore.RESET} {Fore.GREEN}https://www.us-info.com/en/usa{Fore.RESET}
opened {Fore.GREEN} https://www.thisnumber.com/{x113}-{x112}-{x111}{Fore.RESET}
opened {Fore.GREEN} https://www.searchbug.com/peoplefinder/phone-search.aspx?TYPE=phonerev&TAG=people&FULLPHONE={x113}{x112}{x111}{Fore.RESET}
	''')
elif x == 'ssn':
	webbrowser.open('https://www.ssnvalidator.com/index.aspx', new=2, autoraise=True)
	print(f'''
────────{Fore.CYAN}ssn{Fore.RESET}────────────────────────────────────────────────────────────
opened{Fore.CYAN}!{Fore.RESET} {Fore.GREEN}https://www.ssnvalidator.com/index.aspx{Fore.RESET}''')
elif x == 'ip':
	x14 = input('host: ')
	x15 = requests.get("http://ip-api.com/json/%s?fields=65535" % x14)
	ipjson = x15.json()
	city = ipjson["city"]
	country = ipjson["country"]
	isp = ipjson["isp"]
	org = ipjson["org"]
	host = ipjson["as"]
	print(f'''
──{Fore.CYAN}{x14}{Fore.RESET}──────────────────────────────────────
ISP: {Fore.GREEN}{isp}{Fore.RESET}
ISP2: {Fore.GREEN}{org}{Fore.RESET}
Host: {Fore.GREEN}{host}{Fore.RESET}
Country: {Fore.GREEN}{country}{Fore.RESET}
City: {Fore.GREEN}{city}{Fore.RESET}''')
elif x == 'email':
    print(f"example: {Fore.YELLOW}example{Fore.RESET}@example.com")
    x78 = input('emailstart: ')
    print(f"example: example@{Fore.YELLOW}example.com{Fore.RESET}")
    x66 = input('domain: ')
    webbrowser.open(f'https://tools.epieos.com/email.php', new=2, autoraise=True)
    webbrowser.open(f'https://www.cyberbackgroundchecks.com/email/{x78}_.{x66}', new=2, autoraise=True)
    webbrowser.open(f'https://lullar-com-3.appspot.com/en', new=2, autoraise=True)
    print(f'''
──{Fore.CYAN}{x78}@{x66}{Fore.RESET}────────────────────────────────────────
opened{Fore.CYAN}!{Fore.RESET} {Fore.GREEN}https://tools.epieos.com/email.php{Fore.RESET}
opened{Fore.CYAN}!{Fore.RESET} {Fore.GREEN}https://lullar-com-3.appspot.com/en{Fore.RESET}
opened {Fore.GREEN} https://www.cyberbackgroundchecks.com/email/{x78}_.{x66}{Fore.RESET}
	''')
else:
    print(f"{Fore.RED}ERROR{Fore.RESET}")
