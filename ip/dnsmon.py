#--coding:UTF-8--

import dns.resolver,os,httplib

iplist = []  # 定义域名IP列表
appdomain = "baidu.com"  # 定义监控域名

def get_iplist(domain=""):  # 域名解析函数，解析成功的IP将被追加到iplist
    try:
        A = dns.resolver.query(domain,'A')
    except Exception,e:
        print "dns resolver error:"+str(e)  # str()是将内容转换成字符串，如i=1,str(i),i='1'
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)  # 追加到iplist
    return True

def checkip(ip):
    checkurl=ip+":80"
    getcontent=""
    httplib.socket.setdefaulttimeout(5)  # 定义http链接超时时间5秒
    conn=httplib.HTTPConnection(checkurl)  # 创建http连接对象

    try:  # 尝试这行语句
        conn.request("GET","/",headers = {"Host": appdomain})  # 发起URL请求，添加host主机头
        r=conn.getresponse()
        getcontent=r.read(20)  # 获取URL页面前15个字符，以便做可用性校验
    finally:  # 不管try如何都执行下面语句
        if getcontent.strip().upper().find('HTML'):  # strip()空格和换行都删除，upper()所有字母换成大写，find()查找是否包含的字符串。监控URL页的内容一般是事先定义好的，比如HTTP200等
            print ip+" [OK]"
        else:
            print ip+" [Error]"  # 此处可放告警程序，邮件、短信、微信
if __name__=="__main__":
    if get_iplist(appdomain) and len(iplist)>0:  # 条件：域名解析正确且至少返回一个IP
        for ip in iplist:
            checkip(ip)
    else:
        print "dns resolver error."