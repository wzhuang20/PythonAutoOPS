#--coding:UTF-8--

import os,datetime,time

def month_get():
    d = datetime.datetime.now()  # 创建当天时间函数
    dayscount = datetime.timedelta(days=d.day)  # 计算出本月的第几天
    dayto = d - dayscount  # 当天时间-本月第几天=上个月最后一天
    date_from = datetime.datetime(dayto.year, dayto.month, 1, 0, 0, 0)  # 上个月第一天
    date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)  # 上个月最后一天
    return  (time.mktime(time.strptime(str(date_from), '%Y-%m-%d %H:%M:%S')),time.mktime(time.strptime(str(date_to), '%Y-%m-%d %H:%M:%S')))  #返回成linux的时间戳

date_range = month_get()  # 赋值

def get_dirlist(date_range):
    dir = '/opt/www/logs'  # 需要列出文件的目录路径
    files = os.listdir(dir)  # 累出目录下的所有文件
    for i in files:
        if os.stat(dir + os.sep + i).st_mtime >= date_range[0] and os.stat(dir + os.sep + i).st_mtime <= date_range[1]:  # os.stat查看文件属性，os.sep添加“/”（在windows下就是“\\”），st_atime (访问时间), st_mtime (修改时间), st_ctime（创建时间），具体可百度“python中如何获得文件的修改时间”
            print dir + os.sep + i,os.remove(dir + os.sep + i)  # 输出匹配出来的文件，再删除，这样可以知道删除了哪些文件

print date_range[0],date_range[1]  # 输出return里的第一个和第二个元祖
get_dirlist(date_range)  # 调用函数（执行函数）