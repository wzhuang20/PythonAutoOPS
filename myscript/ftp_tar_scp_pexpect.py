import pexpect
import sys

ip = "192.168.1.21"  # 定义目标主机
user = "root"  # 目标主机用户
passwd = "3cNdk302BNdke"  # 目标主机密码
target_file = "/data/logs/nginx_access.log"  # 目标主机nginx日志文件

child = pexpect.spawn('/usr/bin/ssh', [user+'@'+ip])  # 输入、输出日志写入mylog.txt文件
fout = file('mylog.txt','w')
child.logifle = fout

try:
    child.expect('(?i)password')  # 匹配password字符串，(?i)表示不区分大小写
    child.sendline(passwd)
    child.expect('#')
    child.sendline('tar -zcf /data/nginx_access.tar.gz '+target_file)  #打包nginx日志文件

    child.expect('#')
    print child.before
    child.sendline('exit')
    fout.close()
except EOF:  # 定义EOF异常处理
    print "expect EOF"
except TIMEOUT:  # 定义TIMEOUT异常处理
    print "expect TIMEOUT"


child = pexpect.spawn('/usr/bin/scp', [usr+'@'+ip+':/data/nginx_access.tar.gz','/home'])  # 启动scp远程拷贝命令，实现将打包好的nginx日志复制至本地/home目录
fout = file('mylog.txt','a')
child.logfile = fout
try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect(pexpect.EOF)  # 匹配缓冲区EOF（结尾），保证文件复制正常完成
except EPF:
    print "except EOF"
except TIMEOUT:
    print "except TIMEOUT"