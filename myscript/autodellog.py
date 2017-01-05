#--coding:UTF-8--

import os,datetime,subprocess,time

def month_get():
    d = datetime.datetime.now()
    dayscount = datetime.timedelta(days=d.day)
    dayto = d - dayscount
    date_from = datetime.datetime(dayto.year, dayto.month, 1, 0, 0, 0)
    date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
    return  (time.mktime(time.strptime(str(date_from), '%Y-%m-%d %H:%M:%S')),time.mktime(time.strptime(str(date_to), '%Y-%m-%d %
H:%M:%S')))

def get_dirlist(date_range):
    dir = '/opt/www/logs'
    files = os.listdir(dir)
    for i in files:
        if os.stat(dir + os.sep + i).st_mtime > date_range[0] and os.stat(dir + os.sep + i).st_mtime < date_range[1]:
            print dir + os.sep + i,os.remove(dir + os.sep + i)

date_range = month_get()
print date_range[0],date_range[1]
get_dirlist(date_range)