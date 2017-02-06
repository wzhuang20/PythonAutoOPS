# coding:utf-8

import paramiko
import sys,os,time

blip="192.168.1.23"  # 定义堡垒机信息
bluser="root"
blpasswd="*****"

hostname="192.168.1.21"  # 定义业务服务器信息
username="root"
password="*****"

tmpdir="/tmp"
remotedir="/data"
localpath="/home/nginx_access.tar.gz"  # 本地源文件路径
tmppath=tmpdir+"/nginx_access.tar.gz"  # 堡垒机临时路径
remotepath=remotedir+"/nginx_access_hd.tar.gz"  # 业务主机目标路径
port=22
passinfo='\'s password: '
paramiko.util.log_to_file('syslogin.log')

t = paramiko.Transport((blip,port))
t.connect(username=bluser,password=blpasswd)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(localpath, tmppath)  # 上传本地源文件到堡垒机临时路径
sftp.close()

ssh=paramiko.SSHClient()  # 登录堡垒机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip,username=bluser,password=blpasswd)

channel=ssh.invoke_shell()  # 创建会话，开启命令调用
channel.settimeout(10)  # 会话命令执行超时时间，单位为秒

buff = ''
resp = ''
# scp中专目录文件到目标主机
channel.send('scp'+tmppath+' '+username+'@'+hostname':'+remotepath+'\n')
while not buff.endswith(passinfo):  # ssh登录的提示信息判断，输出串尾含有"\'s password:"时退出while循环
    try:
        resp = channel.recv(9999)
    except Exception,e:
        print 'Error info:%s connection time.' % (str(e))
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp
    if not buff.find('yes/no')==-1:  # 输出串尾含有"yes/no"时发送"yes"并回车
        channel.send('yes\n')
        buff=''

channel.send(password+'\n')

buff=''
while not buff.endswith('# '):
    resp = channel.recv(9999)
    if not resp.find(passinfo)==-1:  # 输出串尾含有"\'s password: "时说明密码不正确，要求重新输入
        print 'Error info: Authentication failed.'
        channel.close()
        ssh.close()
        sys.exit()

    buff += resp
print buff
channel.close()
ssh.close()