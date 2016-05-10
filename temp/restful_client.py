#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
from urlparse import urljoin
 
BASE_URL = 'http://192.168.26.67:8080'
AUTH = ('admin', 'admin')
 
 
def test_get_user_list():
    rsp = requests.get(urljoin(BASE_URL, '/snippets/'), auth=AUTH, headers={
        'Accept': 'application/json'
    })
    return rsp
 
 
def test_post_user_list():
    json_data = dict(
        title='zhangsan',
        code='oo',
        linenos='true'
    )
    rsp = requests.post(urljoin(BASE_URL, '/snippets/'), auth=AUTH, headers={
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }, data=json.dumps(json_data))
    return rsp
 
def test_get_user():
    rsp = requests.get(urljoin(BASE_URL, '/snippets/17'), auth=AUTH, headers={
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    })
    return rsp
 
def test_put_user():
    json_data = dict(
        title='zhangsan',
        code='oo',
        linenos='true'
    )
    # 注意最后的 /
    rsp = requests.put(urljoin(BASE_URL, '/snippets/1/'), auth=AUTH, headers={
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        }, data=json.dumps(json_data),
    )
    return rsp
 
def test_patch_user():
    json_data = dict(
        title='aaaaaaaaaaaaaaaaaaaa',
        )
    rsp = requests.patch(urljoin(BASE_URL, '/snippets/1/'), auth=AUTH, headers={
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        }, data=json.dumps(json_data),
    )
    return rsp

def add_server(server_name,ip):
    json_data = dict(
        server_name=server_name,
        ip=ip,
    )
    rsp = requests.post(urljoin(BASE_URL, 'api/servers/'),headers={
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }, data=json.dumps(json_data))
    return rsp

def get_server_list():
    rsp = requests.get(urljoin(BASE_URL, 'api/servers/'),headers={
        'Accept': 'application/json',
    })
    return rsp

def delete_server():
    # 注意最后的 /
    rsp = requests.delete(urljoin(BASE_URL, '/api/servers/4/'), headers={
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        }
    )
    return rsp
if __name__ == '__main__':
   # for i in range(2,100):
   #     add_server('server%d' % i,'192.168.1.%d' % i)
        
    s = delete_server()
    print s.text
