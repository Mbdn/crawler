#!/usr/bin python2.7
#-*- coding:utf-8 -*-
#chartjs.图表库amcharts

import time, os, urllib2,re,string
import sched  #是一种调度（延时处理机制）

#初始化sched模块 scheduler类
schedule=sched.scheduler(time.time,time.sleep) #参数（时间戳，延时)

#定时调取函数
def execute_command():
    request = urllib2.Request("http://bbs.xuegod.cn")
    response = urllib2.urlopen(request)
    reader = response.read()
    response.close()
    #匹配规则
    usernump = re.compile(r'人数<br><em>.*?</em>')
    usernummatch = usernump.findall(reader)

    if usernummatch:
        currentnum = usernummatch[0]
        currentnum = currentnum[string.index(currentnum,'>')+5:string.rindex(currentnum,'<')]
        lit = "当前时间："+ time.strftime("%y年%m月%d日%H时%M分",time.localtime(time.time())) + "论坛在线人数:"+ currentnum +"\n"
        print lit
    f = open('word.txt','a+')
    f.write(lit)

def timing(inc):
    schedule.enter(inc,0,timing,(inc,))
    execute_command()

def main(inc=5):       #10秒执行一次
    schedule.enter(0,0,timing,(inc,))
    schedule.run()      #执行

#该模块可以被别的模块调用执行，自己也可以执行
if __name__=="__main__":
    main()
