# coding=utf-8

from fabric.colors import *
from fabric.api import *

env.user='root'
env.roledefs = {  # 定义业务角色分组
    'webservers': ['192.168.1.21','192.168.1.22'],
    'dbservers': ['192.168.1.23']
}
env.passwords = {
    'root@192.168.1.21:22': '******'
    'root@192.168.1.22:22': '******'
    'root@192.168.1.23:22': '******'
}

@roles('webservers')  # webtask任务函数引用'webservers'角色修饰符
def webtask():  # 部署nginx php php-fpm 等环境
    print yellow("Install nginx php php-fpm...")
    with settings(warn_only=True):
        run("yum -y install nginx")
        run("yum -y intall php-fpm php-mysql php-mbstring php-xml php-mcrypyt php-gd")
        run("chkconfig --levels 235 php-fpm on")
        run("chkconfig --levels 235 nginx on")

@roles('dbservers')  # dbtask任务函数引用'dbservers'角色修饰符
def dbtask():  # 部署mysql环境
    print yellow("Install Mysql...")
    with settings(warn_only=True):
        run("yum -y install mysql mysql-server")
        run("chkconfig --levels 235 mysqld on")

@roles('webservers','dbservers')  # publictask任务函数同时引用两个角色修饰符
def publictask():  # 部署公共类环境，如epel、ntp等
    print yellow("Install epel ntp...")
    with settings(warn_only=True):
        run("rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm")
        run("yum -y install ntp")

def deploy():
    execute(publictask)
    execute(webtask)
    execute(dbtask)