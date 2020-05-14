#!/usr/bin/python3
# file name 文件名：client.py
# -*-coding:utf-8 -*-
# import socket、sys modules 导入 socket、sys 模块
import socket
import sys

# create socket object 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local hostname 获取本地主机名
host = socket.gethostname()

# set port 设置端口号
port = 9999

# connect server, set host and port 连接服务，指定主机和端口
s.connect((host, port))

# received data length < 1024 byte 收小于 1024 字节的数据
msg = s.recv(1024)

s.close()

print(msg.decode('utf-8'))
