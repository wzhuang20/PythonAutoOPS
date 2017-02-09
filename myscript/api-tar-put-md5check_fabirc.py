# coding=utf-8

from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user='root'
env.hosts=['192.168.1.21','192.168.1.22']
env.password='******'

@task
@runs_once
def tar_task():  # 本地打包任务函数，只限执行一次
    with lcd("/data/logs")
        local("tar -zcf access.tar.gz access.log")

@task
def put_task():  # 上传文件函数
    run("mkdir -p /data/logs")
    with cd("/data/logs"):
        with settings(warn_only=True):  # put出现异常时继续执行，非终止
            result = put("/data/logs/access.tar.gz","/data/logs/access.tar.gz")
        if result.failed and not confirm("put file failed,Continue[Y/N]?"):
            abort("Aborting file put task!")  # 出现异常时，确认用户是否继续，(Y继续)

@task
def check_task():  # 校验文件任务函数
    with settings(warn_only=True):
        lmd5=local("md5sum /data/logs/access.tar.gz",capture=True).split(' ')[0]  # 本地local命令需要配置capture=True才能捕获返回值
        rmd5=run("md5sum /data/logs/access.tar.gz").split(' ')[0]
    if lmd5==rmd5:  # 对比本地及远程文件md5信息
        print "OK"
    else:
        print "ERROR"

@task
def go():
    tar_task()
    put_task()
    check_task()

# 不适用go函数的话，适用如下命令，可分开运行
#  fab -f simple.py tar_task
#  fab -f simple.py put_task
#  fab -f simple.py check_task

# 如果适用go函数的话，如下命令即可
# fab -f simple.py go