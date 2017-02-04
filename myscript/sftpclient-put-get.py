#coding=utf8

import paramiko

username = "root"
password = "*******"
hostname = "192.168.1.200"
port = 22

try:
    t = paramiko.Transport((hostname,port))
    t.connect(username=username,password=password)
    sftp = paramiko.SFTPClient.from_transport(t)

    sftp.put("/home/user/info.db","/data/user/info.db")  # 上传文件
    sftp.get("/data/user/info_1.db","/home/user/info_1.db")  # 下载文件
    sftp.mkdir("/home/userdir",0755)  # 创建目录
    sftp.rmdir("/home/userdir")  # 删除目录
    sftp.rename("/home/test.sh","/home/testfile.sh")  # 文件重命名
    print sftp.stat("/home/testfile.sh")  # 打印文件信息
    print sftp.listdir("/home")  # 打印目录列表
    t.close();
except Exception, e:
    print str(e)