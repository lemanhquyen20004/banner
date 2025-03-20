import requests,os,sys, time
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from bs4 import BeautifulSoup
import json
import requests
import time
from time import strftime
import os
import requests
import urllib.parse
from time import strftime
import os
from datetime import datetime
from time import sleep, strftime
import datetime
#Color
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
xanhnhat = "\033[1;36m"
#Đánh Dấu Bản Quyền
HĐ_tool = trang + " " + trang + "[" + do + "+_+" + trang + "] " + trang + "=> "
mquang = trang + " " + trang + "[" + do + "÷_+" + trang + "] " + trang + "=> "
thanh = trang + "-------------------------------------------------------------------------"

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Gọi hàm để xóa màn hình
clear_screen()

# Lmao
thanh_xau=trang+'~'+do+'['+vang+'⟨⟩'+do+'] '+trang+'➩  '+xanhnhat
thanh_dep=trang+'~'+do+'['+xanh_la+'✓'+do+'] '+trang+'➩  '+xanhnhat
def get_ip_from_url(url):
#     response = requests.get(url)
#     ip_address = socket.gethostbyname(response.text.strip())
#     return ip_address
     return "127.0.0.1"
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url
import os
import requests
from time import strftime
now = datetime.datetime.now()
thu = now.strftime('%A')
ngay_hom_nay = now.strftime('%d')
thang_nay = now.strftime('%m')
nam_ = now.strftime('%Y')
now = datetime.datetime.now()
gio_hien_tai = now.strftime('%H:%M:%S')
def save_key_to_file(key, filename='THOMAS-key.txt'):
    with open(filename, 'w') as file:
        file.write(str(key))


def load_key_from_file(filename='THOMAS-key.txt'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read().strip()
    return None

# Thông báo qua web
thongtin = requests.get('http://webkey.x10.bz/ThongBao/thongtin.json').text
thongbao = requests.get("http://webkey.x10.bz/ThongBao/thongbao.json").text
version = requests.get("http://webkey.x10.bz/ThongBao/version.json").text
Copyright = requests.get("http://webkey.x10.bz/ThongBao/copyright.json").text

# Banner
banner = ''' 
  \x1b[38;5;207m╔══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╗
    \033[1;31m  ████████╗██████╗ ███████╗ ██████╗     ██╗  ██╗██╗   ██╗   
    \033[1;34m  ╚══██╔══╝██╔══██╗██╔════╝██╔═══██╗    ╚██╗██╔╝██║   ██  
    \033[1;33m     ██║   ██████╔╝█████╗  ██║   ██║     ╚███╔╝ ██║   ██    
    \033[1;32m     ██║   ██╔══██╗██╔══╝  ██║   ██║     ██╔██╗ ██║   ██║    
    \033[1;35m     ██║   ██║  ██║███████╗╚██████╔╝    ██╔╝ ██╗╚██████╔   
    \033[1;36m     ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚═════╝     ╚═╝  ╚═╝ ╚═════╝ 
\033[1;32m════════════════════════════════════════════════════════════════
{thongtin}
\033[1;32m══════════════════ \033[1;31mTHÔNG BÁO ═══════════════════════════════════
{thongbao}
   \x1b[38;5;207m╚══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╝
''' .format(Copyright=Copyright, version=version, thongtin=thongtin, thongbao=thongbao)

for i in banner:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.00130)
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
thanh_xau= print(f"{red}┌───────────────────────────────────────────────────────────────────────")
thanh_dep= print(f"{red}│\t\t\033[1;33mCopyright : {Copyright} | \033[1;32mVersion : {version} \t\t│")
thanh_cuoi=print(f"{red}├───────────────────────────────────────────────────────────────────────")

Write.Print('╔═════════════════════╗ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║  TOOL Trao Đổi Sub  ║ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════╝ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('[⟨⟩]➩ Nhập Số [1] TDS TIKTOK MAX SPEED [NGON] \n',Colors.white,interval=0.0001)
Write.Print('[⟨⟩]➩ Nhập Số [1.1] TDS TIKTOK AUTO [VIP] \n',Colors.white,interval=0.0001)
Write.Print('[⟨⟩]➩ Nhập Số [2] TDS BẰNG PAGE PRO5 [TẠM] \n',Colors.white,interval=0.0001)
Write.Print('[⟨⟩]➩ Nhập Số [3] TDS FACEBOOK FULL JOD [VIP] \n',Colors.white,interval=0.0001)
Write.Print('[⟨⟩]➩ Nhập Số [4] TDS INSTAGRAM MAX SPEED  [MỚI] \n',Colors.white,interval=0.0001)
Write.Print('╔══════════════════════╗ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║  TOOL TƯƠNG TÁC CHÉO ║ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚══════════════════════╝ \n',Colors.yellow,interval=0.0001,end='\r')
print(f'{hong}[⟨⟩]➩ \033[1;32mNhập Số [5]  TTC PRO5 [ỔN] \n')
print(f'{hong}[⟨⟩]➩ \033[1;32mNhập Số [6] TTC INSTAGRAM MAX SPEED  [MỚI] \n')
Write.Print('╔═════════════════════╗ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║     TOOL GOLIkE     ║ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════╝ \n',Colors.yellow,interval=0.0001,end='\r')
print(f'{hong}[⟨⟩]➩ \033[1;95mNhập Số [7] TOOL GỘP GOLKIE TIKTOK [VIP] \n')
print(f'[⟨⟩]➩ \033[1;95mNhập Số [7.1] TOOL GOLKIE TIKTOK [VIP] \n')

chon = str(input('\033[1;31m[\033[1;3⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;37m: \033[1;33m'))

if chon == '1':
    exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhattool/main/tdstiktok.py').text)
elif chon == '1.1':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhattool/main/traodoisubtiktok.py').text)
elif chon == '2':
    exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhattool/main/tdspro5.py').text)
elif chon == '3':
    exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhattool/main/tdsfb.py').text)
elif chon == '4':
    exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhattool/main/tdsig.py').text)
elif chon == '5':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhattool/main/ttcpro5.py').text)
elif chon == '6':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhattool/main/ttcig.py').text)
elif chon == '7.1':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhattool/main/gotik.py').text)
elif chon == '7':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhattool/main/golikev3.py').text)
else:
    print("Sai Lựa Chọn")
    exit()
