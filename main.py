import time
import os
import math
import sys

#------>Main Pakages<--------
os.system("clear")
os.system("pkg install figlet")
os.system("pkg install nano")
os.system("pkg install micro")
os.system("pkg install unzip")
os.system("pkg install namp")
os.system("pkg install hydra")
os.system("pkg install python3")
os.system("pkg install unzip")
os.system("pkg install curl")
os.system("pkg install perl")
os.system("apt-get install xdg-utils")
os.system("pkg install nodejs")

#------->Slow Print<-------
def slowprint(s):
	for c in s + '' :
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(5. / 100)

#------->Exit<------------
def exit():
	os.exit

#------->Clear<----------
def clear():
	os.system("clear")

#--------->Banner<--------
def banner():
	print('''
████████╗ ██████╗  ██████╗ ██╗         ██╗  ██╗██╗   ██╗██████╗ 
╚══██╔══╝██╔═══██╗██╔═══██╗██║         ██║  ██║██║   ██║██╔══██╗
   ██║   ██║   ██║██║   ██║██║         ███████║██║   ██║██████╔╝
   ██║   ██║   ██║██║   ██║██║         ██╔══██║██║   ██║██╔══██╗
   ██║   ╚██████╔╝╚██████╔╝███████╗    ██║  ██║╚██████╔╝██████╔╝
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ''')

#=================================

#====Hacking Tools=============

def trackip():
	os.system("clear")
	os.system("git clone https://github.com/htr-tech/track-ip")
	os.system("mv track-ip $HOME")
	os.system("python main.py")
def phish():
	os.system("clear")
	os.system("git clone https://github.com/htr-tech/zphisher")
	os.system("mv blackhack_phish $HOME")
	os.system("python main.py")
def ngrok():
	os.system("clear")
	os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip")
	os.system("unzip ngrok-stable-linux-arm.zip")
	os.system("rm -rf ngrok-stable-linux-arm.zip")
	os.system("mv ngrok $HOME")
	os.system("python main.py")
def hydra():
	print("Hydra SecssesFully Installed")
	slowprint('''You Can Run Hydra By Just Typing Hydra''')
	os.system("python main.py")
def vanish():
	os.system("clear")
	os.system("git clone https://github.com/noob-hackers/vanish")
	os.system("mv vanish $HOME")
	os.system("python main.py")
def seeu():
	os.system("clear")
	os.system("git clone https://github.com/noob-hackers/seeu")
	os.system("mv seeu $HOME")
	os.system("python main.py")
def seeker():
	os.system("clear")
	os.system("git clone https://github.com/thewhiteh4t/seeker")
	os.system("mv seeker $HOME")
	os.system("python main.py")
def tigervirus():
	os.system("clear")
	os.system("git clone https://github.com/Devil-Tigers/TigerVirus")
	os.system("mv TigerVirus $HOME")
	os.system("python main.py")
def osint():
	os.system("clear")
	os.system("git clone https://github.com/th3unkn0n/osi.ig.git")
	os.system("mv osi.ig $HOME")
	os.system("python main.py")
def john():
	os.system("clear")
	os.system("git clone git clone https://github.com/openwall/john")
	os.system("mv john $HOME")
	os.system("python main.py")
def websploit():
	os.system("clear")
	os.system("git clone https://github.com/websploit/websploit")
	os.system("mv osi.ig $HOME")
	os.system("python main.py")
def redwak():
	os.system("clear")
	os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK")
	os.system("mv RED_HAWK $HOME")
	os.system("python main.py")
def dodos():
	os.system("clear")
	os.system("git clone https://github.com/ProgrammerGaurav/DDos-Attack.git")
	os.system("mv DDos-Attack $HOME")
	os.system("python main.py")
def sqlmap():
	os.system("clear")
	os.system("git clone https://github.com/sqlmapproject/sqlmap")
	os.system("mv sqlmap $HOME")
	os.system("python main.py")
def phoneinfoga():
	os.system("clear")
	os.system("git clone git clone https://github.com/ExpertAnonymous/PhoneInfoga")
	os.system("mv PhoneInfoga $HOME")
	os.system("python main.py")
def telegramscrapper():
	os.system("clear")
	os.system("git clone https://github.com/th3unkn0n/TeleGram-Scraper.git")
	os.system("mv TeleGram-Scraper $HOME")
	os.system("python main.py")
def fotosploit():
	os.system("clear")
	os.system("git clone https://github.com/khansaad1275/FotoSploit")
	os.system("mv FotoSploit $HOME")
	os.system("python main.py")
def wifi():
	os.system("clear")
	os.system('''git clone https://github.com/TermuxHackz/wifi-hacker && git clone https://github.com/waseem-sajjad/WifiGod && wget https://raw.github.com/derv82/wifite/master/wifite.py && git clone https://github.com/savio-code/fern-wifi-cracker.git && git clone https://github.com/faizann24/wifi-bruteforcer-fsecurify''')
	os.system("mv wifi-hacker $HOME")
	os.system("mv wifite.py $HOME")
	os.system("mv WifiGod $HOME")
	os.system("mv wifi-bruteforcer-fsecurify $HOME")
	os.system("mv fern-wifi-cracker $HOME")
	os.system("python main.py")
def routor():
	os.system("clear")
	os.system("git clone https://github.com/threat9/routersploit")
	os.system("mv routersploit $HOME")
	os.system("python main.py")
def nmap():
	os.system("clear")
	print("Nmap Installed SecssesFully")
	print("You Can Run Nmap By Just Typing nmap")
	os.system("python main.py")
def osrframework():
	os.system("clear")
	os.system("git clone https://github.com/i3visio/osrframework")
	os.system("mv osrframework $HOME")
	os.system("python main.py")
def brutex():
	os.system("clear")
	os.system("git clone https://github.com/1N3/BruteX")
	os.system("mv BruteX $HOME")
	os.system("python main.py")
def cupp():
	os.system("clear")
	os.system("git clone https://github.com/Mebus/cupp")
	os.system("mv cupp $HOME")
	os.system("python main.py")
def instaspam():
	os.system("clear")
	os.system("git clone https://github.com/wnein/instaspam")
	os.system("mv instaspam $HOME")
	os.system("python main.py")
def bomber():
	os.system("clear")
	os.system("git clone https://github.com/anubhavanonymous/XLR8_BOMBER")
	os.system("mv XLR8_BOMBER $HOME")
	os.system("python main.py")
def tsfconsole():
	os.system("clear")
	os.system("git clone https://github.com/BHUTUU/TSconsole-framework")
	os.system("mv TSconsole-framework $HOME")
	os.system("python main.py")
def qrljacking():
	os.system("clear")
	os.system("git clone https://github.com/OWASP/QRLJacking")
	os.system("mv QRLJacking $HOME")
	os.system("python main.py")
def xerosploit():
	os.system("clear")
	os.system("git clone https://github.com/LionSec/xerosploit")
	os.system("mv xerosploit $HOME")
	os.system("python main.py")
def hakkuframework():
	os.system("clear")
	os.system("git clone https://github.com/4shadoww/hakkuframework")
	os.system("mv hakkuframework $HOME")
	os.system("python main.py")
def arat():
	os.system("clear")
	os.system("git clone https://github.com/Zack-sys/A-Rat-Exploit")
	os.system("mv A-Rat-Exploit $HOME")
	os.system("python main.py")
def keylogger():
	os.system("clear")
	os.system("git clone https://github.com/D4Vinci/PyLoggy.git")
	os.system("mv PyLoggy $HOME")
	os.system("python main.py")
def seet():
	os.system("clear")
	os.system("curl -LO https://raw.githubusercontent.com/Hax4us/setoolkit/master/setoolkit.sh ")
	os.system("mv setoolkit.sh $HOME")
	os.system("cd")
	os.system("clear")
	print("This Will Take A Long Time So Pls Wait")
	os.system("bash setoolkit.sh")
	os.system("cd Tool-Hub")
	os.system("python main.py")
def exploitdb():
	os.system("clear")
	os.system("git clone https://github.com/offensive-security/exploitdb")
	os.system("mv exploitdb $HOME")
	os.system("python main.py")
def shellnoob():
	os.system("clear")
	os.system("git clone https://github.com/reyammer/shellnoob")
	os.system("mv shellnoob $HOME")
	os.system("python main.py")
def haxrat():
	os.system("clear")
	os.system("git clone https://github.com/Hax4us/hatRat")
	os.system("mv hatRat $HOME")
	os.system("python main.py")
def axex():
	os.system("clear")
	os.system("git clone https://github.com/farinap5/A-xex")
	os.system("mv A-xex $HOME")
	os.system("python main.py")
def brutal():
	os.system("clear")
	os.system("git clone https://github.com/screetsec/Brutal")
	os.system("mv Brutal $HOME")
	os.system("python main.py")
def beef():
	os.system("clear")
	os.system("git clone https://github.com/beefproject/beef")
	os.system("mv beef $HOME")
	os.system("python main.py")
def ciphey():
	os.system("clear")
	os.system("git clone https://github.com/Ciphey/Ciphey")
	os.system("mv Ciphey $HOME")
	os.system("python main.py")
def metasploit():
	os.system("clear")
	os.system("wget Auxilus.github.io/metasploit.sh")
	os.system("mv metasploit.sh $HOME")
	os.system("cd")
	os.system("bash metasploit.sh")
	os.system("clear")
	print("This Will Take A long Time,So Pls Wait")
	os.system("python main.py")


#=========Hacking Tools End============

#===========Menu==========
clear()
banner()
print("")
print("========================")
print("Developed By King-Nazim")
print("========================")
print("Select Your Options:-")
print("1]Hacking Tools")
print("2]Update")
print("3]Our Apps")
print("4]Our Instagram")
print("5]Our Github")
print("6]Exit")
choose=int(input("Enter Your Option Here: "))
if choose==1 :
	os.system("clear")
	os.system("figlet Tools")
	print("")
	print("=======================")
	print("Developed By King-Nazim")
	print("=======================")
	print("")
	print("The Tools Are Give Below")
	print("")
	print('''1]zphisher
2]Track-Ip
3]Ngrok
4]Nmap
5]Hydra
6]Vanish
7]SeeU
8]Seeker
9]Tiger_Virus
10]Osint
11]Websploit
12]RED_HAWK
13]Metasploit
14]SET
15]A-Rat-Exploit
16]Beef
17]QRLJacking
18]Routersploit
19]JohnTheRipper
20]DDos
21]SqlMap
22]PhoneInfoGa
23]Telegram-Scrappe
24]Fotosploit
25]Wifi-Hacking
26]Key-Logger
27]Ciphey
28]Brutal
29]A-xex
30]Shellnoob
31]Exploitdb
32]Hakkuframework
33]Xerosploit
34]Osrframework
35]Cupp
36]XLR8_BOMBER
37]TSconsole
38]HaxRat
39]BruteX
40]InstaSpam

		''')
	main2=int(input("Enter Your Option Here: "))
	if main2==2 :
		trackip()
	if main2==1 :
		phish()
	if main2==3 :
		ngork()
	if main2==4 :
		namp()
	if main2==5 :
		hydra()
	if main2==6 :
		vanish()
	if main2==7 :
		seeu()
	if main2==8 :
		seeker()
	if main2==9 :
		tigervirus()
	if main2==10 :
		osint()
	if main2==11 :
		websploit()
	if main2==12 :
		redwak()
	if main2==13 :
		metasploit()
	if main2==14 :
		seet()
	if main2==15 :
		arat()
	if main2==16 :
		beef()
	if main2==17 :
		qrljacking()
	if main2==18 :
		routor()
	if main2==19 :
		john()
	if main2==20 :
		dodos()
	if main2==21 :
		sqlmap()
	if main2==22 :
		phoneinfoga()
	if main2==23 :
		telegramscrapper()
	if main2==24 :
		fotosploit()
	if main2==25 :
		wifi()
	if main2==26 :
		keylogger()
	if main2==27 :
		ciphey()
	if main2==28 :
		brutal()
	if main2==29 :
		axex()
	if main2==30 :
		shellnoob()
	if main2==31 :
		exploitdb()
	if main2==32 :
		hakkuframework()
	if main2==33 :
		xerosploit()
	if main2==34 :
		osrframework()
	if main2==35 :
		cupp()
	if main2==36 :
		bomber()
	if main2==37 :
		tsfconsole()
	if main2==38 :
		haxrat()
	if main2==39 :
		brutex()
	if main2==40 :
		instaspam()


if choose==7:
	exit()

if choose==2:
	os.system("figlet Update")
	print("")
	os.system("cd")
	os.system("rm -rf Tool-Hub")
	os.system("git clone https://github.com/King-Nazim/Tool-Hub.git")
	os.system("cd Tool-Hub")
	os.system("python main.py")

if choose==3:
	os.system("xdg-open https://appsuishop.blogspot.com/")

if choose==4:
	os.system("xdg-open https://www.instagram.com/nazimcp7/")

if choose==5:
	os.system("xdg-open https://github.com/King-Nazim/")




























