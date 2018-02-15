# coding: UTF8
import urllib  
from bs4 import BeautifulSoup

dic=[]

def getHtml(url):  
    page = urllib.urlopen(url)  
    html = page.read()  
    return html  
  
def getImg(html): 
    soup=BeautifulSoup(html,'lxml')
    imglist=soup.find_all('img',class_="BDE_Image")
    x = 0  
    for img in imglist:  
        link=img.get('src')
        urllib.urlretrieve(link,'%s.jpg' % x)
        print('第%s张图下载完成' % x)  
        x = x + 1          
     
url="http://tieba.baidu.com/p/4553605613"
html = getHtml(url)
getImg(html)
