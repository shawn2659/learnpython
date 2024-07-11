# -*- coding: utf-8 -*-
"""
@author: shawn.zhao
@Mail: yh.zhao@yamu.com
@file: generate_dns.py
@time: 2024/7/11 上午10:51
"""

from scapy.all import *

# 构建DNS查询
dns_request = IP(dst="192.168.17.53")/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname="example.com", qtype=0))

# 发送DNS查询并接收响应
response = sr1(dns_request, verbose=0)

# 显示响应
response.show()