### 简介:

插件式的子域名收集工具。

版本:0.1

### 文档:

所有插件应该以_plugin.py结尾,如:google_plugin.py

所有插件应该具有：
```python
domain_list 变量,是一个set类型的变量
__author 变量,是一个字符串型变量,它说明了此插件的作者
print_author() 函数,这个函数打印作者信息
return_domain(str domain) 函数,这个函数用来修改domain_list变量
```

### 示例:

#### 设置变量
```python
__author = 'XiaoTouM1ng'
domain_list = set()
```

#### 输出作者信息:
```python
def print_author():
    print("Google subdomain,{name}".format(name=__author))
```

#### 对子域名进行收集:
```python
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
```

#### 操作变量进行返回:
```python
def return_domain(domain):
    print("Goole start.....")
    for i in Get_domain(domain):
        if i == 0:
            return 0
        domain_list.add(i)
```

#### 联系我:
```text
blog:www.f4ckweb.top
```