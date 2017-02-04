# --coding:UTF-8--  需要crypto、ecdsa包和python开发包python-devel的支持
import paramiko

hostname='47.93.87.11'
username='root'
password='*********'
paramiko.util.log_to_file('syslogin.log')  # 发送paramiko日志到syslogin.log文件

ssh=paramiko.SSHClient()  # 创建一个ssh客户端client对象
ssh.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 自动添加主机名及主机秘钥到本地hostkeys对象，并将其保存，不依赖load_system_host_keys()的配置，即使~/.ssh/known_hosts不存在也不产生影响

ssh.connect(hostname=hostname,username=username,password=password)  # 创建ssh连接
stdin,stdout,stderr=ssh.exec_command('free -m')  # 调用远程执行命令方法stdout.readlines()
print stdout.read()  # 打印命令执行结果，得到python列表形式，可以使用stdout.readlines()
ssh.close()  # 关闭ssh连接.
