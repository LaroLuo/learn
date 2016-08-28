import urllib
import json

urll = "http://python-data.dr-chuck.net/comments_295208.json"

fhand = urllib.urlopen(urll)
data = fhand.read()
readj = json.loads(data)
coun = 0
for comment in readj["comments"]:
	coun =int(comment["count"]) + coun
print coun