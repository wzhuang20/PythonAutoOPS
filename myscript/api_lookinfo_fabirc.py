# coding=utf-8

from fabric.api import *

env.user='root'
env.hosts=['192.168.1.5','192.168.1.6']
env.password='********'

@runs_once  # 查看本地系统信息，当有多台主机时只运行一次
def local_task():  # 本地任务函数
    local("username -a")

def remove_task():
    with cd("/data/logs"):  # "with"的作用是让后面的表达式的语句继承当前状态，实现"cd /data/logs && ls -l"的效果
        run("ls -l")

# 通过fab命令分别调用local_task和remove_task
#fab -f simple.py local_task
#fab -f simple.py remove_task