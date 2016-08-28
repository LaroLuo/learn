import urllib
import re
from bs4 import BeautifulSoup
position = 18
count = 7
# url = raw_input('Enter - ')
# position = int(raw_input('Enter - position '))
# count = int(raw_input('Enter - count '))
realname = 'Betsy'
i = 0
lis = list()
ls = []
while i < count+1:
    names=[]
    print 'http://python-data.dr-chuck.net/known_by_%s.html ' %realname
    html = urllib.urlopen('http://python-data.dr-chuck.net/known_by_%s.html ' %realname).read()
    soup = BeautifulSoup(html,"html.parser")
    tags = soup('a')
    for tag in tags :
        t= tag.get('href',None)
        lis= re.findall(('[_].*[.]'),t)
        ls = lis[0]
        realname = (ls[4:(len(ls)-1)])
        names.append(realname)
    realname=names[position-1]
    i = i + 1
print 'done!'