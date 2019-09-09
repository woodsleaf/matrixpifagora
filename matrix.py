# -*- coding: utf-8 -*-
import sys
import os
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
from tkinter import Menu
import re
from functools import reduce
import argparse
parser = argparse.ArgumentParser(description='Enter birthday')
parser.add_argument(
    '-d',
    '--birthday',
    default='01-01-1978', #'17-11-1991'
    help='provide an birthday -d=ddmmyyyy (default: 17-11-1991 )'
)
parser.add_argument(
    '-n',
    '--fullname',
    default='LastnameNamePatronymic',
    help='provide an fullname -n=ФамилияИмяОтчество (default: LastnameNamePatronymic )'
)
my_namespace = parser.parse_args()
#print(my_namespace)

fullname = my_namespace.fullname
indata = my_namespace.birthday
'''
17-11-1991
30 3 28 10
171119913032810
[111111][][7]
[2][][8]
[33][][99]
'''

def findto(mychar, mystr):
    mychar= '[' + str(mychar) + ']'
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
    return strsum(re.sub(r'[/.,;-]', '', indata))
#test: print(fwn(indata))

#from input to text
def clickedBtn():
    indata = lbl_birthday_value.get()
    print(lbl_birthday_value.get())
    return True

def nd(fwnarr):
    res = fwnarr
    while (len(str(res)) != 1):
        res = strsum(res)
    print('NumDesteny = ', res)
    return res

#Begin==================================================

fwnarr = re.sub(r'[/.,;-]', '', indata) # строка ddmmyyyy
numdesteny = nd(fwnarr)
dmyarr = re.split(r'[/,.;-]', indata)   # массив [dd, mm, yyyy]
#check: print(fwnarr, ' ', dmyarr)
day = str(int(dmyarr[0])) #Убираем из строки начальный ноль, чтобы в dayfirst был не ноль а число.
dayfirst = int(list(day)[0]) #Формируется массив из чисел дня, если их больше одного, берется нулевой элемент
check: print('first Number of day = ', dayfirst)
year = dmyarr[2]
#test: print("dmyarr: ", ''.join(dmyarr))

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
    dopnum = firstworknumber, secondworknumber, '19', threeworknumber, fourworknumber
    all = ''.join(dmyarr) + str(firstworknumber) + str(secondworknumber) + '19' + str(threeworknumber) + str(fourworknumber)
else:
    print(firstworknumber, secondworknumber, threeworknumber, fourworknumber)
    dopnum = firstworknumber, secondworknumber, threeworknumber, fourworknumber
    all = ''.join(dmyarr) + str(firstworknumber) + str(secondworknumber) + str(threeworknumber) + str(fourworknumber)

print(all)
print('[{}][{}][{}]'.format(findto(1, all),findto(4, all),findto(7, all)) )
print('[{}][{}][{}]'.format(findto(2, all),findto(5, all),findto(8, all)) )
print('[{}][{}][{}]'.format(findto(3, all),findto(6, all),findto(9, all)) )

print('Target =', len(findto(147, all)))
print('Famile =', len(findto(258, all)))
print('Stable. =', len(findto(369, all)))

print('Samoocenka =', len(findto(123, all)))
print('Money =', len(findto(456, all)))
print('Talant =', len(findto(789, all)))

print('Duhovnost =', len(findto(159, all)))
print('Temperament =', len(findto(357, all)))

#Рисуем GUI (4 колонки/11строк)
#1#Дата рождения    /Значение                           /Темперамент(357)
#2#Доп. числа       /Значение                           /Значение
#3#Число судьбы     /Значение

#4#Характер(1)      /Здоровье(4)        /Удача(7)       /Цель(147)
#5#значение         /значение           /значение       /значение

#6#Энергия(2)       /Логика-интуиция(5) /Долг(8)        /Семья(258)
#7#значение         /значение           /значение        /значение

#8#Интерес(3)       /Труд(6)            /Память-Ум(9)   /Привычки(369)
#9#значение         /значение           /значение       /значение

#10#Самоценка(123)  /Деньги(456)        /Талант(789)    /Духовность(159)
#11#значение        /значение           /значение       /значение

window = Tk()
#Заголовок окна
window.title("Добро пожаловать в приложение matrix")
#window.geometry('683x768')
#Меню
menu = Menu(window)
new_item = Menu(menu) #, tearoff=0
new_item.add_command(label='Новый')
new_item.add_separator()
new_item.add_command(label='Открыть')
new_item.add_separator()
new_item.add_command(label='Изменить')
menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)

#zero
lbl_birthday = Label(window, text="Дата рождения", font=("Arial Bold", 18))
lbl_birthday.grid(column=0, row=0)
lbl_birthday_value = Entry(window, width=10, font=("Arial", 14))
lbl_birthday_value.insert(INSERT, indata)
lbl_birthday_value.focus()
lbl_birthday_value.grid(column=1, row=0)
btn = Button(window, command=clickedBtn, text="Вычислить", bg="white", fg="black")
btn.grid(column=2, row=0)

lbl_temperament = Label(window, text="Темперамент(357)", font=("Arial", 18))
lbl_temperament.grid(column=3, row=0)

#one
lbl_dopnumbers = Label(window, text="Доп числа", font=("Arial Bold", 18))
lbl_dopnumbers.grid(column=0, row=1)
lbl_dopnumbers_value = Label(window, text="1st, 2st, 3st, 4st", font=("Arial", 14))
lbl_dopnumbers_value['text'] = dopnum
lbl_dopnumbers_value.grid(column=1, row=1)

lbl_temperament_value = Label(window, text="value", font=("Arial", 14))
lbl_temperament_value['text'] = len(findto(357, all))
lbl_temperament_value.grid(column=3, row=1)

#two
lbl_desteny = Label(window, text="Число судьбы", font=("Arial Bold", 18))
lbl_desteny.grid(column=0, row=2)
lbl_desteny_value = Label(window, text="value", font=("Arial", 14))
lbl_desteny_value['text'] = numdesteny
lbl_desteny_value.grid(column=1, row=2)


#three
lbl_character = Label(window, text="Характер(1)", font=("Arial Bold", 18))
lbl_character.grid(column=0, row=3)
lbl_zdorovie = Label(window, text="Здоровье(4)", font=("Arial Bold", 18))
lbl_zdorovie.grid(column=1, row=3)
lbl_udacha = Label(window, text="Удача(7)", font=("Arial Bold", 18))
lbl_udacha.grid(column=2, row=3)
lbl_target = Label(window, text="Цель(147)", font=("Arial Bold", 18))
lbl_target.grid(column=3, row=3)

lbl_character_value = Label(window, text="value", font=("Arial", 14))
lbl_character_value['text'] = findto(1, all)
lbl_character_value.grid(column=0, row=4)
lbl_zdorovie_value = Label(window, text="value", font=("Arial", 14))
lbl_zdorovie_value['text'] = findto(4, all)
lbl_zdorovie_value.grid(column=1, row=4)
lbl_udacha_value = Label(window, text="value", font=("Arial", 14))
lbl_udacha_value['text'] = findto(7, all)
lbl_udacha_value.grid(column=2, row=4)
lbl_target_value = Label(window, text="value", font=("Arial", 14))
lbl_target_value['text'] = len(findto(147, all))
lbl_target_value.grid(column=3, row=4)

#five
lbl_energy = Label(window, text="Энергия(2)", font=("Arial Bold", 18))
lbl_energy.grid(column=0, row=5)
lbl_logika = Label(window, text="Логика(5)", font=("Arial Bold", 18))
lbl_logika.grid(column=1, row=5)
lbl_dolg = Label(window, text="Долг(8)", font=("Arial Bold", 18))
lbl_dolg.grid(column=2, row=5)
lbl_family = Label(window, text="Семья(258)", font=("Arial Bold", 18))
lbl_family.grid(column=3, row=5)

lbl_energy_value = Label(window, text="value", font=("Arial", 14))
lbl_energy_value['text'] = findto(2, all)
lbl_energy_value.grid(column=0, row=6)
lbl_logika_value = Label(window, text="value", font=("Arial", 14))
lbl_logika_value['text'] = findto(5, all)
lbl_logika_value.grid(column=1, row=6)
lbl_dolg_value = Label(window, text="value", font=("Arial", 14))
lbl_dolg_value['text'] = findto(8, all)
lbl_dolg_value.grid(column=2, row=6)
lbl_family_value = Label(window, text="value", font=("Arial", 14))
lbl_family_value['text'] = len(findto(258, all))
lbl_family_value.grid(column=3, row=6)

#seven
lbl_interes = Label(window, text="Интерес(3)", font=("Arial Bold", 18))
lbl_interes.grid(column=0, row=7)
lbl_trud = Label(window, text="Труд(6)", font=("Arial Bold", 18))
lbl_trud.grid(column=1, row=7)
lbl_memory = Label(window, text="Память(9)", font=("Arial Bold", 18))
lbl_memory.grid(column=2, row=7)
lbl_privichki = Label(window, text="Привычки(369)", font=("Arial Bold", 18))
lbl_privichki.grid(column=3, row=7)

lbl_interes_value = Label(window, text="value", font=("Arial", 14))
lbl_interes_value['text'] = findto(3, all)
lbl_interes_value.grid(column=0, row=8)
lbl_trud_value = Label(window, text="value", font=("Arial", 14))
lbl_trud_value['text'] = findto(6, all)
lbl_trud_value.grid(column=1, row=8)
lbl_memory_value = Label(window, text="value", font=("Arial", 14))
lbl_memory_value['text'] = findto(9, all)
lbl_memory_value.grid(column=2, row=8)
lbl_privichki_value = Label(window, text="value", font=("Arial", 14))
lbl_privichki_value['text'] = len(findto(369, all))
lbl_privichki_value.grid(column=3, row=8)

#nine
lbl_samoocenka = Label(window, text="Самооценка(123)", font=("Arial Bold", 18))
lbl_samoocenka.grid(column=0, row=9)
lbl_money = Label(window, text="Деньги(456)", font=("Arial Bold", 18))
lbl_money.grid(column=1, row=9)
lbl_talant = Label(window, text="Талант(789)", font=("Arial Bold", 18))
lbl_talant.grid(column=2, row=9)
lbl_duhovnost = Label(window, text="Духовность(159)", font=("Arial Bold", 18))
lbl_duhovnost.grid(column=3, row=9)

lbl_samoocenka_value = Label(window, text="value", font=("Arial", 14))
lbl_samoocenka_value['text'] = len(findto(123, all))
lbl_samoocenka_value.grid(column=0, row=10)
lbl_money_value = Label(window, text="value", font=("Arial", 14))
lbl_money_value['text'] = len(findto(456, all))
lbl_money_value.grid(column=1, row=10)
lbl_talant_value = Label(window, text="value", font=("Arial", 14))
lbl_talant_value['text'] = len(findto(789, all))
lbl_talant_value.grid(column=2, row=10)
lbl_duhovnost_value = Label(window, text="value", font=("Arial", 14))
lbl_duhovnost_value['text'] = len(findto(159, all))
lbl_duhovnost_value.grid(column=3, row=10)

# must be end
window.mainloop()
