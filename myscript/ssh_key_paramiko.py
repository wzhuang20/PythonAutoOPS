# --coding:UTF-8--
import paramiko
import so

hostname='192.168.1.21'
username='root'
paramiko.util.log_to_file('syslogin.log')

ssh=paramiko.SSHClient()
ssh.load_system_host_keys()
privatekey = os.path.expanduser('/home/key/id_rsa')  # 定义私钥存放路径
key = paramiko.RSAKey.from_private_key_file(privatekey)  # 创建私钥对象key

ssh.connect(hostname=hostname,username=username,pkey=key)
stdin,stdout,stderr=ssh.exec_command('free -m')
print stdout.read()
ssh.close()