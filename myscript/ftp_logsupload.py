import os,datetime,time
import ftplib
from ConfigParser import SafeConfigParser
import sys
import os

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

date_from = datetime.datetime(yesterday.year, yesterday.month, yesterday.day, 0, 0, 0)  #
date_to = datetime.datetime(yesterday.year, yesterday.month, yesterday.day, 23, 59, 59)  #
date_from =  time.mktime(time.strptime(str(date_from), '%Y-%m-%d %H:%M:%S'))
date_to =  time.mktime(time.strptime(str(date_to), '%Y-%m-%d %H:%M:%S'))

def get_loglist():
    dir = '/opt/www/logs'
    logfiles = os.listdir(dir)

    for i in logfiles:

        if os.stat(dir+os.sep+i).st_mtime > date_from and  os.stat(dir+os.sep+i).st_mtime < date_to :
            print dir+os.sep+i
            upload(i, 'test', folderstate=1)
            #upload(dir,dir+os.sep+i,'test')

def upload(filename, filedirectory=None, folderstate=0):
    parser = SafeConfigParser()
    parser.read('config.ini')

    host = parser.get('FTP Server', 'host')
    user = parser.get('FTP Server', 'user')
    password = parser.get('FTP Server', 'pass')

    session = ftplib.FTP(host, user, password)
    filename_extension_together = os.path.splitext(filename)
    storefilename = filename_extension_together[0] + filename_extension_together[1]
    file = open(filename, 'rb')  # file to send
    print "Opening Folder ", filedirectory
    print "Sending ..."

    if folderstate == 1:  # setting folder name
        session.cwd(filedirectory)

    elif folderstate == 2:  # new folder create command
        session.mkd(filedirectory)
        session.cwd(filedirectory)

    session.storbinary('STOR ' + storefilename, file)  # send the file
    print "Uploaded File ..."
    file.close()  # close file and FTP
    print "Operation Done Session Closed ..."
    session.quit()

def getList(filedirectory=None):
    parser = SafeConfigParser()
    parser.read('config.ini')

    host = parser.get('FTP Server', 'host')
    user = parser.get('FTP Server', 'user')
    password = parser.get('FTP Server', 'pass')

    session = ftplib.FTP(host, user, password)
    filelist = []  # to store all files
    if filedirectory is not None:  # current directory list
        session.cwd(filedirectory)
    print "List of Content"
    print session.retrlines('LIST')
    session.quit()

get_loglist()