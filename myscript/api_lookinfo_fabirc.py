# coding=utf-8

from fabric.api import *

env.user='root'
env.hosts=['47.93.87.11','47.93.87.52']
env.password='dongbei.001'

@runs_once  # 查看本地系统信息，当有多台主机时只运行一次
def local_task():  # 本地任务函数
    local("username -a")

def remove_task():
    with cd("/data/logs"):  # "with"的作用是让后面的表达式的语句继承当前状态，实现"cd /data/logs && ls -l"的效果
        run("ls -l")