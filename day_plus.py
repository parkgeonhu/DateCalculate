import sys

year=int(input('year='))
month=int(input('month='))
day=int(input('day='))

time=0;
leapyear=False;

def isLeapYear(_year):
    if(_year%400==0):
        return True
    elif(_year%4==0):
        if(_year%100==0):
            return False
        else:
            return True
    else:
        return False
    


for i in range(1,year):
    if isLeapYear(i) is True:
        time+=366
    else:
        time+=365

thirtyone_months = [1, 3, 5, 7, 8, 10, 12]
months = range(1, month)

for i in months:
    if i in thirtyone_months:
        time+=31
    elif(i==2):
        if(isLeapYear(year) is True):
            time+=29
        else:
            time+=28
    else:
        time+=30


after_day=int(input('몇 일 후? '))

time+=day
time+=after_day
result=time%7

day_array=['일','월','화','수','목','금','토']

print(year,"년 ",month,"월 ",day,"일에서 ",after_day,"일 후의 요일은 ",day_array[result],"요일입니다.")

year=1
month=1
day=1

#ㄱㄱㄱㄱㄱ
for i in range(1, sys.maxsize):
    if isLeapYear(i) is True:
        time-=366
    else:
        time-=365
    if time<0:
        leapyear=isLeapYear(year)
        if leapyear is True:
            time+=366
        else:
            time+=365
        break
    year+=1
    
temp=0

for i in range(1,13):
    if i in thirtyone_months:
        temp=31
        time-=31
    elif i==2:
        if isLeapYear(year) is True:
            temp=29
            time-=29
        else:
            temp=28
            time-=28
    else:
        temp=30
        time-=30
    if time<0:
        time+=temp
        break
    month+=1

day=time

print(year," ",month," ",day)





