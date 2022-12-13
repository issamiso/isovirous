import os
import socket
import sys
import time
import random 
os.system('clear')
W='\33[0m'
R='\33[1;31m'
G='\33[1;32m'
O='\33[1;33m'
B='\33[1;34m'
P='\33[1;35m'
C='\33[1;36m'
GR='\33[1;37m'
y='\033[0;32m'
gr='\033[1;30m'
#try:
#	os.system('cd /sdcard/VirousISO')
#except:
#	os.mkdir('/sdcard/VirousISO')
def xx():
	print(f'{R} >{W} [{R}+{W}]{G} Loding {R} ',end='',flush=True)
	for i in range(15):
		for s in r'-\|/-\|/':
			print('\b',s,end='',sep='',flush=True)
			time.sleep(0.04)
def virous():
	print(R+f'''
 ___ ___ _______ ______ _______ _______ _______ 
|   |   |_     _|   __ \       |   |   |     __|
|   |   |_|   |_|      <   -   |   |   |__     |
 \_____/|_______|___|__|_______|_______|_______|
                                                
{R} >{y} Coding bay issam iso 
{R} >{y} github: {gr}github.com/issamiso
{R} >{y} Telegram:{gr} i_4iS_exe 
 {R}>{y} Facebook:{gr} Iso Hacking 
{P}————————————————————{R}[{G}TERMUX{R}]{P}——————————————————————'''+W)
	print(f'''{R} > {G}({O}1{G}){W} Virous Facebook
{R} > {G}({O}2{G}){W} Virous Instagram
{R} > {G}({O}3{G}){W} Virous Messenger
{R} > {G}({O}4{G}){W} Virous telegram
{R} > {G}({O}5{G}){W} Virous watsupp
{R} > {G}({O}6{G}){W} Virous Normal 
{R} > {G}({O}7{G}){W} Virous {R}X''')
	try:
		cmd=input(f'{R} >{W} [{R}+{W}]{G} Enter Namber:{O} ')
	except:
		print(R+'Good bay ...')
	try:
		if cmd == '1' or cmd == '01':
			xx()
			print('')
			os.system('cd .-&&cp Facebook.apk /sdcard')
			print(f'{R} >{W} [{R}+{W}]{R} Virous{G} /sdcard')
			use()
		if cmd == '2' or cmd == '02':
			xx()
			print('')
			os.system('cd .-&&cp Instagram.apk /sdcard')
			print(f'{R} >{W} [{R}+{W}]{R} Virous{G} /sdcard')
			use()
		if cmd == '3' or cmd == '03':
			xx()
			print('')
			os.system('cd .-&&cp Messenger.apk /sdcard')
			print(f'{R} >{W} [{R}+{W}]{R} Virous{G} /sdcard')
			use()
		if cmd == '4' or cmd == '04':
			xx()
			print('')
			os.system('cd .-&&cp Telegram.apk /sdcard')
			print(f'{R} >{W} [{R}+{W}]{R} Virous{G} /sdcard')
			use()
		if cmd == '5' or cmd == '05':
			xx()
			print('')
			os.system('cd .-&&cp Watsupp.apk /sdcard')
			print(f'{R} >{W} [{R}+{W}]{R} Virous{G} /sdcard')
			use()
		if cmd == '6' or cmd == '06':
			xx()
			print('')
			os.system('cd .-&&cp Virous.apk /sdcard')
			print(f'{R} >{W} [{R}+{W}]{R} Virous{G} /sdcard')
			use()
		if cmd == '7' or cmd == '07':
			xx()
			print('')
			os.system('cd .-&&cp xxn.apk /sdcard')
			print(f'{R} >{W} [{R}+{W}]{R} Virous{G} /sdcard')
			use()
	except:
		print(R+'Good bay ')
def use():
	try:
		com=input(f'{R} >{W} [{R}+{W}]{G} Do you want to complete? y/n :{O} ')
		if com == 'y':
			os.system('clear')
			while virous():
				print('Hello')
	except:
		print(R+'Good bay ')
	
virous()