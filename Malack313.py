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
                                                                  
  ╔═══╗ ╔═══╗  ╔═══════╗ ╔═╗       ╔═══════╗  ╔══════╗ ╔═╗ ╔═══╗   
  ║▒▒═╗▒╔═╗▒║  ║▒╔═══╗▒║ ║▒║       ║▒╔═══╗▒║  ║▒═════╝ ║▒║ ║▒╔═╝   
  ║▒║ ║▒║ ║▒║  ║▒║   ║▒║ ║▒║       ║▒    ║▒║  ║▒║      ║▒╚═══╝    
  ║▒║ ║▒║ ║▒║  ║▒╚═══╝▒║ ║▒║       ║▒╚═══╝▒║  ║▒║      ║▒╔═══╗     
  ║▒║ ╚═╩ ║▒║  ║▒╔═══╗▒║ ║▒║═════╗ ║▒╔═══╗▒║  ║▒═════╗ ║▒║ ║▒╚═╗   
  ╚═╝     ╚═╝  ╚═╝   ╚═╝ ╚═══════╝ ╚═╝   ╚═╝  ╚══════╝ ╚═╝ ╚═══╝   
                                                                  
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

count = 0
headers = []
referer = [
    "https://google.it/",
    "https://google.com/",
    "https://alibaba.com/",    
    "https://x.com/",
    "https://facebook.com/",
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
