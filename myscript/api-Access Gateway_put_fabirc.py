# coding=utf-8

from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user='root'
env.gateway='192.168.1.23'  # 定义堡垒机ip，作为文件上传、执行的中转设备
env.hosts=['192.168.1.21','192.168.1.22']
env.passwords={  # 假如所有主机密码都不一样，可以通过env.passwords字典一一指定
    'root@192.168.1.21:22': '*******',
    'root@192.168.1.22:22': '*******',
    'root@192.168.1.23:22': '*******'  # 堡垒机账号信息

}

lpackpath="/home/install/lnmp0.9.tar.gz"  # 本地安装包路径
rpackpath="/tmp/install"  # 远程安装包路径

@task
def put_task():
    run("mkdir -p /tmp/install")
    with settings(warn_only=True):
        result = put(lpackpath, rpackpath)  # 上传安装包
    if result.failed and not confirm("put file failed, Continue[Y/N]?"):
        abort("Aborting file put task!")

@task
def run_task():  # 执行远程命令，安装lnmp环境
    with cd("/tmp/install"):
        run("tar -zxvf lnmp0.9.tar.gz")
        with cd("lnmp0.9/"):  # 使用with继续继承/tmp/install目录位置状态
            run("./centos.sh")

@task
def go():  # 上传、安装组合
    put_task()
    run_task()