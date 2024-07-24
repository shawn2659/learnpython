# -*- coding: utf-8 -*-
"""
@author: shawn.zhao
@Mail: yh.zhao@yamu.com
@file: gen_payload.py
@time: 2024/7/18 下午6:21
"""

import random
import time
import base64
from Crypto.Cipher import AES
import hashlib

def aes_encrypt(data):
    pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16).encode()
    if isinstance(data, bytes):
        data = pad(data)
    else:
        data = pad(str(data).encode())
    cipher = AES.new('1234567890abcDEF'.encode('utf8'), AES.MODE_CBC, '1234567890abcDEF'.encode('utf8'))
    encryptedbytes = cipher.encrypt(data)
    encodestrs = base64.b64encode(encryptedbytes)
    return encodestrs.decode()

def md5_encrypt(data):
    m = hashlib.md5()
    if isinstance(data, str):
        b = data.encode()
        m.update(b)
    else:
        m.update(data)
    md = str(base64.b64encode(m.hexdigest().encode()), "utf-8")
    return md

local_format = "%Y-%m-%d %H:%M:%S"
timeStamp = time.strftime(local_format, time.localtime(time.time()))

start = 9151314442816847872
end = 9223372036854775807

commandId = random.randrange(start, end)

data = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<ednsDomainCommand>    
    <commandId>{}</commandId>    
    <type>1</type>
    <domainType>1</domainType>
    <domain>api1.yamutest.com</domain>
    <urgency>1</urgency>    
    <time>        
        <effectTime>2024-06-27 00:00:00</effectTime>        
        <expiredTime>2024-09-27 23:00:00</expiredTime>    
    </time>    
    <range>        
        <dnsId>2222</dnsId>        
        <effectiveScope>1</effectiveScope>
    </range>    
    <timeStamp>{}</timeStamp>
</ednsDomainCommand>'''.format(commandId, timeStamp)

ranVal = '1234567890abcDEF'
pwdHash = md5_encrypt('1234567890abcDEF' + '1234567890abcDEF')
command = aes_encrypt(data.encode())
commandHash = md5_encrypt(data + ranVal)

payload = '''<?xml version="1.0" ?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webservice.ack.dns.act.com/">
    <soapenv:Header/>
    <soapenv:Body>
        <web:dns_command>
            <web:dnsId>2222</web:dnsId>
            <web:randVal>1234567890abcDEF</web:randVal>
            <web:pwdHash>{}</web:pwdHash>
            <web:command>{}</web:command>
            <web:commandHash>{}</web:commandHash>
            <web:commandType>21</web:commandType>
            <web:commandSequence>1671071974545643</web:commandSequence>
            <web:encryptAlgorithm>1</web:encryptAlgorithm>
            <web:hashAlgorithm>1</web:hashAlgorithm>
            <web:compressionFormat>0</web:compressionFormat>
            <web:commandVersion>v1.0</web:commandVersion>
        </web:dns_command>
    </soapenv:Body>
</soapenv:Envelope>'''.format(pwdHash, command, commandHash)

print(payload)
