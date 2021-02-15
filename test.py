import os, sys, json, time, random,  requests

from Email import mail
from urllib import parse
from itertools import product
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

douyuCookie = os.environ.get("douyucookie")
oldlist = os.environ.get("list")
douyuList = str(oldlist).split('-')
oldnum = os.environ.get("num")
douyuNum = str(oldnum).split('-')
oldSum = os.environ.get("sum")
douyuSum = int(oldSum)


# 斗鱼自动发送指定人员礼物

c = ''
# 斗鱼礼物接口
url = 'https://www.douyu.com/member/prop/send'
cookies={}
# 存放cookie
list1 = []


def init(cookie):
    c = cookie
    for line in c.split(';'):
    #其设置为1就会把字符串拆分成2份
        name,value=line.strip().split('=',1)
        cookies[name]=value

    headers['Cookie'] = cookie


headers = {
            'Host': 'www.douyu.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.douyu.com',
            'X-Requested-With':'XMLHttpRequest' ,
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.181Safari / 537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://www.douyu.com/88885',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'
}
print("waibu")


def getYGB():
    #proxy = random.choice(json_resp['proxies'])
    chrome_options = Options()
    #print("--proxy-server=http://{}:{}".format(proxy['ip'], proxy['port']))
    #chrome_options.add_argument("--proxy-server=http://{}:{}".format(proxy['ip'], proxy['port']))
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.get('https://www.douyu.com/9999')
    for i in cookies.keys():
        cookie1 = {
            'domain': '.douyu.com',
            'name': i,
            'value': cookies[i],
            'expires': '',
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False,
        }
        driver.add_cookie(cookie1)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.quit()
    

def mainApi(sum,idList,nubList):
    s = requests.Session()
    if sum == 0:
        for i in range(len(idList)):
            for nub in range(int(nubList[i])):
                data = 'dy=99b3bf61409e9782aee70daf00071501&prop_id=268&num=1&sid=' + cookies[
                    'acf_uid'] + '&did=204389&rid=' + idList[i] + '&is_jz=0'
                Result = s.post(url=url, data=data, headers=headers)
                k = Result.text
                json1 = json.loads(k)
                list1.append(json1['msg'])
                time.sleep(1)

    if sum != 0:
        si = 0
        for i ,id in product(range(999),idList):
            data = 'dy=99b3bf61409e9782aee70daf00071501&prop_id=268&num=1&sid=' + cookies['acf_uid'] + '&did=204389&rid=' + id + '&is_jz=0'
            Result = s.post(url=url, data=data, headers=headers)
            k = Result.text
            json1 = json.loads(k)
            list1.append(json1['msg'])
            si = si + 1
            if si == sum:
                break
            time.sleep(1)


if __name__ == "__main__":
    if cookie:
        print("start")
        main(cookies=douyuCookie,sum=douyuSum,idList=douyuList,nubList=douyuNum)
        print("end")
