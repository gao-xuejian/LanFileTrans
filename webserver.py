#!/usr/bin/python
# -*- coding:utf-8
import sys
import socket
import os
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


def run(ip,port):
    Handler = SimpleHTTPRequestHandler
    Server = BaseHTTPServer.HTTPServer
    Protocol = "HTTP/1.0"
    server_address = (ip, port)
    Handler.protocol_version = Protocol
    try:
        httpd = Server(server_address, Handler)
        dbchk = raw_input( u'''对方将可以获取本文件夹内所有文件，确认请输入"y"，否则请输入"n"（默认为“y”）: '''.encode('gb18030'))
        if (dbchk == 'y') or (dbchk == ""):
            # try:
            print u'''服务启动成功，请通知对方通过浏览器访问如下地址下载文件'''
            print '''
                        %s:%s
                        ''' % (ip,port)
            httpd.serve_forever()
            # except:
                # print u'''停止服务'''
                # sys.exit()    
        elif dbchk == 'n':
            print u'''停止当前服务，如有必要请重启程序'''
            # os.system('pause')
        else:
            print u'''输入不合法，请退出重试'''
            # os.system('pause')
    except:
        print u'''停止当前服务，如有必要请重启程序''' 

    # try:
        # httpd.serve_forever()
    # except:
        # sys.exit()


def get_ip():
    try:
        myname=socket.getfqdn(socket.gethostname())
        myaddr=socket.gethostbyname(myname)
    except:
        print u"获取本机IP地址失败".encode('gb18030')
    return myaddr


if __name__=="__main__":

    print "#"*80
    print u'''
    使用说明：
    1、开启服务后，对方将可以获取本文件夹内所有文件，请确认是否含有保密内容；
    2、如果当前为工作模式，则对方也必须处于工作模式；
    3、如果当前为非工作模式，对方为工作模式，请通过托盘打开浏览器进行访问；
    4、请确认端口未被占用；
    5、使用结束请及时关闭本程序。
           '''
    print "#"*80
    port = raw_input(u'请输入端口号（默认为8000）: '.encode('gb18030'))
    ip = ""
    if port == "":
        port = 8000
    port = int(port)
    if ip == "":
        ip = get_ip()          #自动获取本机ip地址
        # print ip
    run(ip,port)         #运行主函数