import re
x = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
y = re.findall(('[_].*[.]'),x)
a = y[0]
print a[4:(len(a)-1)]
from bs4 import BeautifulSoup
import urllib
html = urllib.urlopen('http://python-data.dr-chuck.net/known_by_Fikret.html ').read()
soup = BeautifulSoup(html)
tags = soup('a')
for tag in tags:
    print tag.get('href',None)
