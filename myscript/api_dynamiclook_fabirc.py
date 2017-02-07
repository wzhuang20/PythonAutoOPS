# coding=utf-8

from fabric.api import *

env.user='root'
env.hosts=['47.93.87.11', '47.93.87.22']
env.password='******'


@runs_once  # 主机遍历过程中，只有第一台触发此函数
def input_raw():
    return prompt("please input directory name:", default="/home")


def worktask(dirname):
    run("ls -l "+dirname)


@task  # 限定只有go函数对fab命令可见
def go():
    getdirname = input_raw()
    worktask(getdirname)
