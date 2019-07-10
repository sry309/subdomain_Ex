import requests,json,base64,urllib3,time,sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

__author = 'XiaoTouM1ng'
domain_list = set()

def print_author():
    print("virustotal subdomain,{name}".format(name=__author))


def Get_domain(domain,page):
    page = base64.b64encode(('I{0}\n.'.format(page)).encode('utf-8'))
    header = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    }
    try:
        r = requests.get("https://www.virustotal.com/ui/domains/{domain}/subdomains?relationships=resolutions&cursor={page}&limit=10".format(domain=domain,page=str(page,'utf-8')),verify=False,headers=header)
        if r.status_code != 200:
            print("[-] virustotal error....")
            yield 0
        res = json.loads(r.text)
        if res['data'] != None:
            for i in res['data']:
                print(i['id'])
                yield i['id']
        else:
            yield 0
    except:
        yield 0

def return_domain(domain):
    print("virustotal start.....")
    page = 0
    while True:
        for i in Get_domain(domain,page):
            if i == 0:
                return 0
            domain_list.add(i)
        page += 1
        time.sleep(10)