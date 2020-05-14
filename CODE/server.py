#!/usr/bin/python3
# filename 文件名：server.py
# -*-coding:utf-8 -*-
# import socket、sys modules 导入 socket、sys 模块
import socket
import sys

# create socket object 创建 socket 对象
s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# get local hostname 获取本地主机名
host = socket.gethostname()

port = 9999

# bind port 绑定端口号
s.bind((host, port))

# set max connects 设置最大连接数，超过后排队
s.listen(5)

while True:
    # create client connect 建立客户端连接
    c, a = s.accept()

    print("client ip address 连接地址: %s" % str(a))

    msg = 'welcome to use 欢迎使用Python！' + "\r\n"
    c.send(msg.encode('utf-8'))
    c.close()
