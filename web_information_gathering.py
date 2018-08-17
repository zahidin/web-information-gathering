from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as bs
import dns.resolver
import threading
import requests
import socket
import whois
import os

def judul():
    print('''
\033[91m\033[1m `++++++++++++++++++++++++/`
\033[91m\033[1m`syyyyyyyyyyyyyyyyyyyyyyyyys          #### ########  ##    ##    ##     ##    ###     ######  ##    ## ######## #### ##     ## ####  ######  ########
\033[91m\033[1m```````://///////syyyyyyyy+            ##  ##     ## ###   ##    ##     ##   ## ##   ##    ## ##   ##     ##     ##  ##     ##  ##  ##    ##    ##
\033[91m\033[1m      `-----------/yyyo/y+             ##  ##     ## ####  ##    ##     ##  ##   ##  ##       ##  ##      ##     ##  ##     ##  ##  ##          ##
\033[91m\033[1m                 .syyo.so              ##  ##     ## ## ## ##    ######### ##     ## ##       #####       ##     ##  ##     ##  ##   ######     ##
\033[91m\033[1m                `syys.so`              ##  ##     ## ##  ####    ##     ## ######### ##       ##  ##      ##     ##   ##   ##   ##        ##    ##
\033[91m\033[1m               `syys.oo`               ##  ##     ## ##   ###    ##     ## ##     ## ##    ## ##   ##     ##     ##    ## ##    ##  ##    ##    ##
\033[91m\033[1m               ````````               #### ########  ##    ##    ##     ## ##     ##  ######  ##    ##    ##    ####    ###    ####  ######     ##
\033[91m\033[1m            :::::::::::::-
\033[91m\033[1m           -///////////+yys.
\033[91m\033[1m         +yyyyyyyyyyyyyyyo`yyy+
\033[91m\033[1m        .//////////////ys.syys.        ######  ########  ########  ######  ####    ###    ##          ##     ## ##     ## ########    ########  ####
\033[91m\033[1m           ```` ``    +s-oyys.        ##    ## ##     ## ##       ##    ##  ##    ## ##   ##          ##     ## ##     ##    ##       ##     ##  ##
\033[97m\033[1m          /yyy/:y-   /y-oyyy-         ##       ##     ## ##       ##        ##   ##   ##  ##          ##     ## ##     ##    ##       ##     ##  ##
\033[97m\033[1m         :yyy+-y:   :y-+yyy+-.         ######  ########  ######    ######   ##  ##     ## ##          ######### ##     ##    ##       ########   ##
\033[97m\033[1m        :yyy+-y/   :y:+yyyyyyyy+-           ## ##        ##             ##  ##  ######### ##          ##     ## ##     ##    ##       ##   ##    ##
\033[97m\033[1m       -yyyo.s/   -y:/yyyyyyyyyyys.   ##    ## ##        ##       ##    ##  ##  ##     ## ##          ##     ## ##     ##    ##       ##    ##   ##
\033[97m\033[1m      -yyyo.s+    `` ``````-+yyyyyy-   ######  ##        ########  ######  #### ##     ## ########    ##     ##  #######     ##       ##     ## ####
\033[97m\033[1m     `+oys.s+                :yyyyyo
\033[97m\033[1m       :+`//                 -yyyoyy
\033[97m\033[1m                           `:syyo.y+
\033[97m\033[1m        ossssssssssssssssssyyyy/-so`
\033[97m\033[1m       /ssssssssssssssssssoo/::+s/
\033[97m\033[1m            /++++++++++++++oss+-`
\033[97m\033[1m            ````````````````

 {2}    --={3}[ {0}{5}Author: X-Code 404 , ZahidCode , BitterCode  {3}]{2}=--
{4}| {2}-- --={3}[ {0}{5}Version:1 (Spesial Kermerdekaan HUT-RI 73th) {3}]{2}=-- -- {4}|
| {2}-- --={3}[ {0}{5}Website: https://github.com/zahidin          {3}]{2}=-- -- {4}|
| {2}-- --={3}[ {0}{5}WEB INFORMATION GATHERING ~ IDN HACKTIVIST   {3}]{2}=-- -- {4}|
{0}'''.format(reset, red, red, white, red, bold))
target = ''
def tampilan_pilihan(target):
    print('{0}[ Web Information Gathering Menu ]{1} '.format(red,reset))
    print('{0}[ Target = {2} ]{1} \n'.format(white,reset,target))
    print(' 1)  Banner Grab')
    print(' 2)  Whois')
    print(' 3)  Tracerroute')
    print(' 4)  DNS Record')
    print(' 5)  Reverse DNS Lookup')
    print(' 6)  Zone Transfer Lookup')
    print(' 7)  Port Scan')
    print(' 8)  Subdomain Scan')
    print(' 9)  CMS Identify')
    print(' 10) Reverse IP Lookup')
    print(' 11) Extract Page Links')
    print(' 12) Directory Fuzz')
    print(' 13) File Fuzz')

bold = '\033[1m'
underline = '\033[4m'
black = '\033[90m'; red = '\033[91m'; green = '\033[92m'; yellow = '\033[93m'; blue = '\033[94m'; magenta = '\033[95m'; cyan = '\033[96m'; white = '\033[97m'
reset = '\033[0m'

ids = [
    'NONE','A','NS','MD','MF','CNAME','SOA','MB','MG','MR','NULL','WKS','PTR','HINFO','MINFO','MX','TXT','RP','AFSDB','X25','ISDN','RT','NSAP','NSAP-PTR','SIG','KEY','PX','GPOS','AAAA','LOC','NXT','SRV','NAPTR','KX','CERT','A6','DNAME','OPT','APL','DS','SSHFP','IPSECKEY','RRSIG','NSEC','DNSKEY','DHCID','NSEC3','NSEC3PARAM','TLSA','HIP','CDS','CDNSKEY','CSYNC','SPF','UNSPEC','EUI48','EUI64','TKEY','TSIG','IXFR','AXFR','MAILB','MAILA','ANY','URI','CAA','TA','DLV'
]


def banner_grab(url):
    banner = requests.get(url)
    banners = banner.headers
    banners_result = str(banners).replace("{","").replace("}","").replace("': '",": ").replace("', '", ",\n")
    return banners_result

def whoiss(url):
    whois_q = whois.whois(url)
    return whois_q

def tracerroute(target):
    tracerroute_req = requests.get('https://api.hackertarget.com/mtr/?q={}'.format(target))
    tracerroute_respon = tracerroute_req.text
    result = """{0}""".format(str(tracerroute_respon))
    return result

def dns_record_scanner(hostname, ids, dns_record_list):
    try:
        respon = dns.resolver.query(hostname,ids)
        for data in respon:
            ids = str(ids); data = str(data)
            dns_record_list.append(str(ids + ' : ' + data))
    except Exception:
        pass

def dns_record(hostname):
    dns_record_list = []
    for a in ids:
        t = threading.Thread(target=dns_record_scanner,args=(hostname,a,dns_record_list))
        t.start()
    t.join()
    result = dns_record_list
    return result

def reverse_dns_lookup(rdl_ip):
    rdl_ip = rdl_ip + '/24'
    req = requests.get('https://api.hackertarget.com/reversedns/?q={}'.format(rdl_ip))
    respon = req.text
    result = """{0}""".format(str(respon))
    return result

def reverse_ip_lookup(hostname):
    req = requests.get('https://api.hackertarget.com/reverseiplookup/?q={}'.format(hostname))
    respon = req.text
    result = """{0}""".format(str(respon))
    return result

def zone_transfer_lookup(hostname):
    req = requests.get('https://api.hackertarget.com/zonetransfer/?q={}'.format(hostname))
    respon = req.text
    result = """{0}""".format(str(respon))
    return result

def TCP_connect(ip,port,delay,output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip,port))
        output[port] = 'Open'
    except:
        output[port] = ''

def port_scan(hostname,port_end):
    port_scan_list = []
    threads = []
    output = {}
    delay = 10
    for i in range(port_end + 1):
        t = threading.Thread(target=TCP_connect,args=(hostname,i,delay,output))
        threads.append(t)
    for i in range(port_end + 1):
        threads[i].start()
    for i in range(port_end + 1):
        threads[i].join()
    for i in range(port_end +1):
        if output[i] == 'Open':
            port_scan_list.append('# Port Open - '+str(i))
    return port_scan_list

def subdomain_scanner(web,st_200,st_301,st_302,st_403,st_404):
    web = 'http://'+web
    try:
        req = requests.get(web)
        req_code = req.status_code
        if req_code == 200:
            st_200.append(web)
            print("{}{} ->[200]{}".format(green,web,reset))
        elif req_code == 301:
            st_301.append(web)
            print("{}{} ->[301]{}".format(blue,web,reset))
        elif req_code == 302:
            st_302.append(web)
            print("{}{} ->[302]{}".format(cyan,web,reset))
        elif req_code == 403:
            st_403.append(web)
            print("{}{} ->[403]{}".format(red,web,reset))
        else:
            st_404.append(web)
            print("{}{} ->[404]{}".format(yellow,web,reset))
    except ConnectionError:
        pass

def subdomain_scan(hostname,subdomain_list):
    st_200 = []
    st_301 = []
    st_302 = []
    st_403 = []
    st_404 = []
    ss_urls = []
    subdomain_list = open(subdomain_list,'r').read().splitlines()
    for i in subdomain_list:
        ss_urls.append(i + '.' + hostname)
    for i in ss_urls:
        t  = threading.Thread(target=subdomain_scanner,args=(i,st_200,st_301,st_302,st_403,st_404))
        t.start()
    t.join()

def cms_detect(web):
    cms = []
    cms_web = []
    req = requests.get('https://whatcms.org/?s={}'.format(web))
    soup = bs(req.content,'html.parser')
    div_soup = soup.find('div',attrs={'class','large text-center'})
    for i in div_soup.find_all('span',attrs={'class','nowrap'}):
        cms_web.append(i.text)
    cms.append(div_soup.find('a').text)
    if not cms:
        cms_detect = '[!] no CMS Detected'
    else:
        cms_web = cms_web[0]
        cms_detect = cms[0].replace('/c/', '')
        cms_detect = 'Cms : '+cms_detect + ' - ' + cms_web
    return cms_detect

def subnet_lookup(hostname):
    req = requests.get('https://api.hackertarget.com/reverseiplookup/?q={}'.format(hostname))
    respon = req.text
    result = """{0}""".format(str(respon))
    return result

def links_extract(url):
    req = requests.get('https://api.hackertarget.com/pagelinks/?q={}'.format(url))
    respon = req.text
    result = """{0}""".format(str(respon))
    return result

def directory_scanner(url_list,directory_fuzz1,directory_fuzz2,directory_fuzz3):
    try:
        req = requests.get(url_list)
        if req.status_code == 200:
            directory_fuzz1.append(url_list)
            print("{}{} ->[200]{}".format(white,url_list,reset))
        elif req.status_code == 301 or req.status_code == 302:
            directory_fuzz2.append(url_list)
            print("{}{} ->[301/302]{}".format(white,url_list,reset))
        elif req.status_code == 403:
            directory_fuzz3.append(url_list)
            print("{}{} ->[403]{}".format(red,url_list,reset))
        else:
            print("{}{} ->[404]{}".format(red,url_list,reset))

    except:
        pass

def file_scanner(url_list,file_fuzz1,file_fuzz2,file_fuzz3):
    try:
        req = requests.get(url_list)
        if req.status_code == 200:
            file_fuzz1.append(url_list)
            print("{}{} ->[200]{}".format(white,url_list,reset))
        elif req.status_code == 301 or req.status_code == 302:
            file_fuzz2.append(url_list)
            print("{}{} ->[301/302]{}".format(white,url_list,reset))
        elif req.status_code == 403:
            file_fuzz3.append(url_list)
            print("{}{} ->[403]{}".format(red,url_list,reset))
        else:
            print("{}{} ->[404]{}".format(red,url_list,reset))
    except:
        pass

def directory_fuzz(url,directory_list):
    directory_fuzz1 = []
    directory_fuzz2 = []
    directory_fuzz3 = []
    directory_list = open(directory_list,'r').read().splitlines()
    url_list = []
    ii = 0
    for i in directory_list:
        if '/' in directory_list[ii]:
            url_list.append(url + i)
        else:
            url_list.append(url + '/' + i)
        ii = ii + 1
    for i in url_list:
        t = threading.Thread(target=directory_scanner,args=(i,directory_fuzz1,directory_fuzz2,directory_fuzz3))
        t.start()
    t.join()

def file_fuzz(url,file_list):
    file_fuzz1 = []
    file_fuzz2 = []
    file_fuzz3 = []
    file_list = open(file_list,'r').read().splitlines()
    url_list = []
    for i in file_list:
        url_list.append(url + '/' + i)
    for i in url_list:
        t = threading.Thread(target=file_scanner,args=(i,file_fuzz1,file_fuzz2,file_fuzz3))
        t.start()
    t.join()


def main():
    judul()
    tampilan_pilihan(target)
    pilihan = input('\n{}ZahidCode>{}{}'.format(red,white,reset))
    print('\n')
    if pilihan == 1:
        print("{}[ ### Banner Grab ###]{}\n".format(red,reset))
        hasil = banner_grab(http_target)
        hasil = str(hasil).replace("'","")
        print("{}{}".format(white,hasil))

    elif pilihan == 2:
        print("{}[ ### Whois ###]{}\n".format(red,reset))
        hasil = whoiss(http_target)
        hasil = str(hasil).replace("{","").replace("}","").replace('"',"").replace("[","").replace("]","")
        print("{}{}".format(white,hasil))

    elif pilihan == 3:
        print("{}[ ### Tracerroute ### ]{}\n".format(red,reset))
        get_ip = socket.gethostbyname(target)
        hasil = tracerroute(get_ip)
        print("{}{}".format(white,hasil))

    elif pilihan == 4:
        print("{}[ ### DNS Record ### ]{}\n".format(red,reset))
        hasil = dns_record(target)
        hasil = str(hasil).replace("["," ").replace("'","").replace(",","\n").replace("]","")
        print("{}{}".format(white,hasil))

    elif pilihan == 5:
        print("{}[ ### Reverse DNS Lookup ### ]{}\n".format(red,reset))
        get_ip = socket.gethostbyname(target)
        hasil = reverse_dns_lookup(get_ip)
        print("{}{}".format(white,hasil))


    elif pilihan == 6:
        print("{}[ ### Zone Transfer Lookup ### ]{}\n".format(red,reset))
        hasil = zone_transfer_lookup(target)
        print("{}{}".format(white,hasil))

    elif pilihan == 7:
        print("{}[ ### Port ### ]{}\n".format(red,reset))
        port_end = input("{}Port End :{}".format(yellow,blue))
        hasil = port_scan(target,port_end)
        hasil = str(hasil).replace("[","").replace("]","").replace("'","").replace(",","\n")
        print("{}{}".format(white,hasil))

    elif pilihan == 8:
        print("{}[ ### Subdomain Scan ### ]{}\n".format(red,reset))
        subdomain_list = raw_input("{}File Subdomain List :{}".format(yellow,blue))
        subdomain_scan(target,subdomain_list)
        exit()

    elif pilihan == 9:
        print("{}[ ### CMS Identify ### ]{}\n".format(red,reset))
        hasil = cms_detect(target)
        print("{}{}".format(white,hasil))


    elif pilihan == 10:
        print("{}[ ### Reverse IP Lookup ### ]{}\n".format(red,reset))
        hasil = subnet_lookup(target)
        print("{}{}".format(white,hasil))


    elif pilihan == 11:
        print("{}[ ### Extract Page Links ### ]{}\n".format(red,reset))
        hasil = links_extract(target)
        print("{}{}".format(white,hasil))
        os.system('clear')


    elif pilihan == 12:
        print("{}[ ### Directory Fuzz ### ]{}\n".format(red,reset))
        directory_list = raw_input("{}File Directory List :{}".format(yellow,blue))
        directory_fuzz(http_target,directory_list)
        exit()


    elif pilihan == 13:
        print("{}[ ### File Fuzz ### ]{}\n".format(red,reset))
        file_list = raw_input("{}File-File List :{}".format(yellow,blue))
        file_fuzz(http_target,file_list)
        exit()

    else:
        print("{}Nothing!".format(red))
        os.system('clear')
        exit()

if __name__ == '__main__':
    judul()
    target = raw_input('{}Set Target :{}'.format(red,white))
    http_target = target
    if "http://" not in http_target:
        http_target = "http://"+target
    os.system('clear')
    ulang = ''
    while ulang != 'n':
        main()
        ulang = raw_input("\n{}Back?(y/n) :{}".format(red,white))
        os.system('clear')
