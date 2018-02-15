# coding: UTF8
import re
from bs4 import BeautifulSoup
import urllib
import os
 
path = os.getcwd()                        # 获取此脚本所在目录
new_path = os.path.join(path,u'图片')
if not os.path.isdir(new_path):
    os.mkdir(new_path)
  
url='http://tieba.baidu.com/p/4553605613'
html=urllib.urlopen(url)
soup = BeautifulSoup(html,"lxml")
image = soup.find_all('div',class_='BDE_Image')

for img in image:
    urllib.urlretrieve(img)
