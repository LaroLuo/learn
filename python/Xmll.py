import urllib
import xml.etree.ElementTree as ET
serviceceurl =  'http://python-data.dr-chuck.net/comments_295204.xml'
url = serviceceurl
uh = urllib.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
co=0
for count in tree.findall('.//count'):
	co = co+int(count.text)
print co
