# -*- coding: utf-8 -*-
import sys
import re
from functools import reduce


fullname = ''
indata = '13.06.1966'
'''
WN1: 32
WN2: 5
WN3: 6
WN4: 6
Владимир Владимирович Путин
13.06.1966
32 5 6 6
1306196632566
1,1|null|null
2|5|null
3,3|6,6,6,6,6|9
'''

dmyarr = re.split(r'[,.;-]', indata)
#test: print("dmyarr: ", ''.join(dmyarr))

def findto(mychar, mystr):
    mychar= str(mychar)
    res = re.findall(mychar, mystr)
    return ''.join(res)

def strsum(num):
    num = list(str(num)) # str(num)
    #print(num)
    num = reduce((lambda sum, item: int(sum) + int(item)), num)
    #print(num)
    return num
#test: strsum(25)

def truegod(num):
    return (num >=10 and num <= 12)
    #return True if (num >=10 and num <= 12)  else False
#test: print(truegod(5))

firstworknumber = strsum(re.sub(r'[.,;-]', '', indata))
#test: print('WN1: ', firstworknumber)

secondworknumber = 0
if (truegod(firstworknumber)):
    secondworknumber = firstworknumber
else:
    secondworknumber = strsum(str(firstworknumber))

#test: print('WN2: ', secondworknumber)

threeworknumber = 0
if (int(dmyarr[2]) >= int(2000)):
    #после 2000 включительно
    threeworknumber = int(firstworknumber) + 19
else:
    threeworknumber = firstworknumber - int(dmyarr[0])*2

#test: print('WN3: ', threeworknumber)

fourworknumber = 0
if (truegod(threeworknumber)):
    fourworknumber = threeworknumber
else:
    fourworknumber = strsum(str(threeworknumber))

#test: print('WN4: ', fourworknumber)

print(fullname)
print(indata)
all = ''
if (int(dmyarr[2]) >= int(2000)):
    #после 2000 включительно
    #test: print(firstworknumber, secondworknumber, '19', threeworknumber, fourworknumber)
    all = ''.join(dmyarr) + str(firstworknumber) + str(secondworknumber) + '19' + str(threeworknumber) + str(fourworknumber)
else:
    #test: print(firstworknumber, secondworknumber, threeworknumber, fourworknumber)
    all = ''.join(dmyarr) + str(firstworknumber) + str(secondworknumber) + str(threeworknumber) + str(fourworknumber)

#test: 
print(all)
print('{}|{}|{}'.format(findto(1, all),findto(4, all),findto(7, all)) )
print('{}|{}|{}'.format(findto(2, all),findto(5, all),findto(8, all)) )
print('{}|{}|{}'.format(findto(3, all),findto(6, all),findto(9, all)) )
