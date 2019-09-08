# -*- coding: utf-8 -*-
import sys
import argparse
parser = argparse.ArgumentParser(description='Enter birthday')
parser.add_argument(
    '-D',
    '--birthday',
    default='17-11-1991',
    help='provide an birthday -D=ddmmyyyy (default: 17-11-1991 )'
)
parser.add_argument(
    '-N',
    '--fullname',
    default='ФамилияИмяОтчество',
    help='provide an fullname -N=ФамилияИмяОтчество (default: ФамилияИмяОтчество )'
)
my_namespace = parser.parse_args()
print(my_namespace)
import re
from functools import reduce


fullname = my_namespace.fullname #'Владимир Владимирович Путин'
indata = my_namespace.birthday #'13.06.1966'
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
day = dmyarr[0]
dayfirst = int(list(day)[0])
#print('df ', dayfirst)
year = dmyarr[2]
#test: print("dmyarr: ", ''.join(dmyarr))

def findto(mychar, mystr):
    mychar= str(mychar)
    res = re.findall(mychar, mystr)
    return ''.join(res)
#test: print(findto(1,'34241414'))

def strsum(num):
    #print(num)
    num = list(str(num)) # str(num)
    #print(num)
    num = reduce((lambda sum, item: int(sum) + int(item)), num)
    #print(num)
    return num
#test: strsum(25)

def truegod(num):
    num = int(num)
    return (num >=10 and num <= 12)
    #return True if (num >=10 and num <= 12)  else False
#test: print(truegod(5))

def fwn(indata):
    return strsum(re.sub(r'[.,;-]', '', indata))
#test: print(fwn(indata))

#Begin==================================================

firstworknumber = fwn(indata)
#test: print('WN1: ', firstworknumber)

secondworknumber = 0
if (truegod(firstworknumber)):
    secondworknumber = firstworknumber
else:
    secondworknumber = strsum(str(firstworknumber))

#test: print('WN2: ', secondworknumber)

threeworknumber = 0
if (int(year) >= 2000):
    #после 2000 включительно
    threeworknumber = str(int(firstworknumber) + 19)
else:
    threeworknumber = str(int(firstworknumber) - int(dayfirst)*2)

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
if (int(year) >= 2000):
    #после 2000 включительно
    print(firstworknumber, secondworknumber, '19', threeworknumber, fourworknumber)
    all = ''.join(dmyarr) + str(firstworknumber) + str(secondworknumber) + '19' + str(threeworknumber) + str(fourworknumber)
else:
    print(firstworknumber, secondworknumber, threeworknumber, fourworknumber)
    all = ''.join(dmyarr) + str(firstworknumber) + str(secondworknumber) + str(threeworknumber) + str(fourworknumber)

print(all)
print('[{}][{}][{}]'.format(findto(1, all),findto(4, all),findto(7, all)) )
print('[{}][{}][{}]'.format(findto(2, all),findto(5, all),findto(8, all)) )
print('[{}][{}][{}]'.format(findto(3, all),findto(6, all),findto(9, all)) )
