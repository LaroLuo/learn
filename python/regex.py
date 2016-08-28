import re
# file = raw_input('file name:')
# if file > -1 :
file = 'data.txt'
hanl = open(file)
num = list()
su = 0
for line in hanl:
    y = re.findall('[0-9]+',line)
    if len(y) == 0: continue
    for x in y:
        num.append(x)
for x in num:
    numval = float(x)
    su = su + numval
print su