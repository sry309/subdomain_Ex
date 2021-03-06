import requests,urllib3,urllib.parse,time,sys
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

__author = 'XiaoTouM1ng'
domain_list = set()


def print_author():
    print("Google subdomain,{name}".format(name=__author))


def Get_domain(domain):
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
        "accept-language": "zh-CN,zh;q=0.9"
    }
    try:
        for page in range(7):
            r = requests.get(url="https://www.google.com/search?q=site:{domain}&start={page}".format(domain=domain,page=page*10),verify=False,headers=header)
            if(r.status_code != 200):
                print('[-] Google error....')
                yield 0
            soup = BeautifulSoup(r.text, 'html.parser')
            for i in soup.find_all('cite', class_='iUh30'):
                if 'http' in i.text:
                    print(urllib.parse.urlparse(i.text).netloc)
                    yield urllib.parse.urlparse(i.text).netloc
                else:
                    print(str(i.text).split('/')[0])
                    yield str(i.text).split('/')[0]
            time.sleep(20)
    except:
        print('[-] Google error....')
        yield 0

def return_domain(domain):
    print("Goole start.....")
    for i in Get_domain(domain):
        if i == 0:
            return 0
        domain_list.add(i)