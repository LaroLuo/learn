import json
import urllib
serviceurl = 'http://python-data.dr-chuck.net/geojson?'
while True:
	address = raw_input("input address:   ")
	if len(address)<1:
		break
	url = serviceurl+ urllib.urlencode({"sensor": 'false','address': address })
	print "Retrieved from ",url
	fhand = urllib.urlopen(url)
	data = fhand.read()
	try : js = json.loads(data)
	except : js = None
	if 'status' not in js or js['status'] != 'OK':
		print '====Failure==='
		print data
		continue
	print json.dumps(js, indent =4)
	print js['results'][0]['place_id']