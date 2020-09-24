import requests
from bs4 import BeautifulSoup
import bs4
def get(url):
    try:
        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
        r=requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''
def fill(ulist,html):
    soup=BeautifulSoup(html,'html.parser')
    list = soup.find(class_='grid_view').find_all('li')
    for item in list:
        if isinstance(item,bs4.element.Tag):
            name=item.find(class_='title').string
            othername=item.find(class_='other').string
            index = item.find(class_='').string
            info=item.find(class_='bd').find('p')
            ulist.append([index,name,othername,info])
    pass

def printinfo(ulist,num):
    for i in range(num):
        u=ulist[i]
        print(u[0],u[1],u[2],u[3])
def main(page):
    url='https://movie.douban.com/top250?start='+str(page*25)+'&filter='
    uinfo=[]
    html=get(url)
    fill(uinfo,html)
    num=25
    printinfo(uinfo,num)
for i in range(10):
    main(i)
