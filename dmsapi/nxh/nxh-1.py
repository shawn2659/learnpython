# -*- coding: utf-8 -*-
# @File    : dmsapi_nxh.py
# @Author  : Gqinyuan
# @Date    : 2024-03-18
import random
import time
import requests
import base64
from Crypto.Cipher import AES
import hashlib
import uuid

"""
集团内循环指令-直接发到dmsapi
"""


def aes_encrypt(data):
    """
    AES加密
    :param data: 加密内容str/bytes
    :return: 加密后的内容str
    """
    # 匿名函数使用整数的16进制ASCII进行补位
    pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16).encode()
    if isinstance(data, bytes):
        data = pad(data)
    else:
        data = pad(str(data).encode())
    # 字符串补位aes加密的原数据长度要求是16的整数倍
    cipher = AES.new('1234567890abcDEF'.encode('utf8'), AES.MODE_CBC, '1234567890abcDEF'.encode('utf8'))
    encryptedbytes = cipher.encrypt(data)
    # 加密后得到的是bytes类型的数据
    encodestrs = base64.b64encode(encryptedbytes)
    # 使用Base64进行编码,返回byte字符串
    return encodestrs.decode()


def aes_decrypt(data):
    """
    AES解密
    :param data: 解密内容
    :return:
    """
    data = data.encode()
    # 对byte字符串按utf-8进行编码
    # print(data)
    encodebytes = base64.b64decode(data)
    # 将加密数据转换位bytes类型数据
    # print(encodebytes)
    cipher = AES.new('1234567890abcDEF'.encode('utf8'), AES.MODE_CBC, '1234567890abcDEF'.encode('utf8'))
    text_decrypted = cipher.decrypt(encodebytes)
    # 将加密数据进行解密

    unpad = lambda s: s[0:-s[-1]]
    text_decrypted = unpad(text_decrypted)
    # 去补位
    return text_decrypted.decode()


def md5_encrypt(data):
    """
    md5加密
    :param data: 加密内容str/bytes
    :return: 加密后的内容str
    """
    m = hashlib.md5()
    if isinstance(data, str):

        b = data.encode()
        m.update(b)
    else:
        m.update(data)

    md = str(base64.b64encode(m.hexdigest().encode()), "utf-8")

    return md


def sha1_encrypt(data):
    """
    sha1加密
    :param data:加密内容str/bytes
    :return: 加密后的内容str
    """
    m = hashlib.sha1()
    if isinstance(data, str):

        b = data.encode()
        m.update(b)
    else:
        m.update(data)
    md = str(base64.b64encode(m.hexdigest().encode()), "utf-8")

    return md


def sha256_encrypt(data):
    """
    sha256加密
    :param data: 加密内容str/bytes
    :return: 加密后的内容str
    """
    if isinstance(data, str):
        md = hashlib.sha256(data.encode())
    else:
        md = hashlib.sha256(data)
    sign = str(base64.b64encode(md.hexdigest().encode()), "utf-8")

    return sign


local_format = "%Y-%m-%d %H:%M:%S"
timeStamp = time.strftime(local_format, time.localtime(time.time()))

payload = '''<?xml version="1.0" ?>
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webservice.ack.dns.act.com/">
                <soapenv:Header/>
                <soapenv:Body>
                    <web:dns_command>
                        <web:dnsId>1111</web:dnsId>
                        <web:randVal>1234567890abcDEF</web:randVal>
                        <web:pwdHash>{}</web:pwdHash>
                        <web:command>{}</web:command>
                        <web:commandHash>{}</web:commandHash>
                        <web:commandType>{}</web:commandType>
                        <web:commandSequence>1671071974545643</web:commandSequence>
                        <web:encryptAlgorithm>1</web:encryptAlgorithm>
                        <web:hashAlgorithm>1</web:hashAlgorithm>
                        <web:compressionFormat>0</web:compressionFormat>
                        <web:commandVersion>v1.0</web:commandVersion>
                    </web:dns_command>
                </soapenv:Body>
            </soapenv:Envelope>'''

head = {'Content-Type': 'text/xml;charset=UTF-8', 'SOAPAction': "urn:dns_command"}

start = 9151314442816847872
end = 9223372036854775807

commandId = random.randrange(start, end)


def data_21(url):
    """
    精准调度域名启停指令；
    :param url:
    :return:
    """
    data = '''<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
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
                        <dnsId>1111</dnsId>        
                        <effectiveScope>1</effectiveScope>
                    </range>    
                    <timeStamp>{}</timeStamp>
                </ednsDomainCommand>'''.format(commandId, timeStamp)
    ranVal = '1234567890abcDEF'
    pwdHash = md5_encrypt('1234567890abcDEF' + '1234567890abcDEF')
    command = aes_encrypt(data.encode())
    commandHash = md5_encrypt(data + ranVal)
    req = requests.post(url=url, data=payload.format(pwdHash, command, commandHash, '21'), headers=head, verify=False)
    return req.content.decode()


def data_22(url):
    """
    精准调度视图管理指令；
    :param url:
    :return:
    """
    data = '''<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
                <viewCommand>    
                    <commandId>{}</commandId>    
                    <type>1</type>    
                    <code>350100</code>
                    <ipv4>35.1.5.0/30</ipv4>
                    <ipv6>35:1:5::/125</ipv6>
                    <urgency>1</urgency>    
                    <time>        
                        <effectTime>2024-07-17 00:00:31</effectTime>        
                        <expiredTime>2024-07-30 23:16:59</expiredTime>    
                    </time>    
                    <range>        
                        <dnsId>1111</dnsId>        
                        <effectiveScope>1</effectiveScope>
                    </range>    
                    <timeStamp>{}</timeStamp>
                </viewCommand>'''.format(commandId, timeStamp)
    ranVal = '1234567890abcDEF'
    pwdHash = md5_encrypt('1234567890abcDEF' + '1234567890abcDEF')
    command = aes_encrypt(data.encode())
    commandHash = md5_encrypt(data + ranVal)
    req = requests.post(url=url, data=payload.format(pwdHash, command, commandHash, '22'), headers=head, verify=False)
    return req.content.decode()


def data_23(url):
    """
    权重调度域名启停指令
    :param url:
    :return:
    """
    data = '''<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
                <WeightDomainCommand>    
                    <commandId>{}</commandId>    
                    <type>2</type>    
                    <domainType>1</domainType>    
                    <domain>wapi1.yamutest.com</domain> 
                    <urgency>1</urgency>    
                    <time>        
                        <effectTime>2024-06-26 00:01:31</effectTime>        
                        <expiredTime>2024-06-29 23:59:59</expiredTime>    
                    </time>    
                    <range>        
                        <dnsId>1111</dnsId>        
                        <effectiveScope>1</effectiveScope>   
                    </range>    
                    <timeStamp>{}</timeStamp>
                </WeightDomainCommand>'''.format(commandId, timeStamp)
    ranVal = '1234567890abcDEF'
    pwdHash = md5_encrypt('1234567890abcDEF' + '1234567890abcDEF')
    command = aes_encrypt(data.encode())
    commandHash = md5_encrypt(data + ranVal)
    req = requests.post(url=url, data=payload.format(pwdHash, command, commandHash, '23'), headers=head, verify=False)
    return req.content.decode()


config_url = 'https://192.168.17.43:8081/cmccYyzb/command'

print(data_22(config_url))
