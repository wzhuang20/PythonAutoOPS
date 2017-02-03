# --coding:UTF-8--  需要crypto、ecdsa包和python开发包python-devel的支持
import paramiko

hostname='47.93.87.52'
username='root'
password='*********'
paramiko.util.log_to_file('syslogin.log')  # 发送paramiko日志到syslogin.log文件

ssh=paramiko.SSHClient()  # 创建一个ssh客户端client对象
ssh.load_system_host_keys()  # 获取客户端host_keys，默认 ~/.ssh/known_hosts，非默认路径需要制定

ssh.connect(hostname=hostname,username=username,password=password)  # 创建ssh连接
stdin,stdout,stderr=ssh.exec_command('free -m')  # 调用远程执行命令方法stdout.readlines()
print stdout.read()  # 打印命令执行结果，得到python列表形式，可以使用stdout.readlines()
ssh.close()  # 关闭ssh连接
