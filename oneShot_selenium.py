import tkinter
import requests
import selenium
import json
from bs4 import BeautifulSoup
from requests.api import head

# url = "https://www.dgolfclub.com/doLogin.dp/dmparse.dm"
url ="https://www.dgolfclub.com/loginChk.dp/dmparse.dm"

session = requests.session()

acc = {"cyberId":"na9038", "cyberPass":"dbrrkq12", "memberCode":"80"}
# acc = {"cyberId":"new2879", "cyberPass":"aa287900", "memberCode":"80", "url":""}
header = {"Content-Type":"text/json;charset=UTF-8"}
#res = session.post(url, data = acc, headers=header, verify=False)
res = session.post(url, data = acc, verify=False)
#res = session.get("https://www.dgolfclub.com/main.dp/dmparse.dm")
res.status_code
soup = BeautifulSoup(res.text,"html.parser")
print(soup)
print("oneShot")