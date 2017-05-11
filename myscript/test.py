# coding=utf-8

from fabric.colors import *
from fabric.api import *

env.user='root'
env.roledefs = {  # 定义业务角色分组
    'webservers': ['172.16.204.240'],
    'dbservers': ['172.16.204.240']
}
env.password = '123456'

@roles('webservers')  # webtask任务函数引用'webservers'角色修饰符
def webtask():  # 部署nginx php php-fpm 等环境
    print yellow("Install nginx php php-fpm...")
    with settings(warn_only=True):
        run("yum -y install nginx")
        run("yum -y install php-fpm php-mysql php-mbstring php-xml php-mcrypyt php-gd")
        run("systemctl start php-fpm")
        run("systemctl start nginx")
        run("systemctl enable php-fpm")
        run("systemctl enable nginx")

@roles('dbservers')  # dbtask任务函数引用'dbservers'角色修饰符
def dbtask():  # 部署mysql环境
    print yellow("Install Mariadb...")
    with settings(warn_only=True):
        run("yum -y install mariadb mariadb-server")
        run("systemctl start mariadb")
        run("systemctl enable mariadb")


#@roles('webservers','dbservers')  # publictask任务函数同时引用两个角色修饰符。
#def publictask():  # 部署公共类环境，如epel、ntp等
#    print yellow("Install epel ntp...")
#    with settings(warn_only=True):
#        run("rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm")
#        run("yum -y install ntp")

def deploy():
#    execute(publictask)
    execute(webtask)
    execute(dbtask)

print deploy()