#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
from urlparse import urljoin
import hashlib
import time

class RestFulClient():
    def __init__(self):
        self.url = 'http://192.168.26.67:8080/api/'
        self.username = 'zhaobin'
        self.token_id = '66636e0ceac6720af6dbee4b4e9785b0b6306d61'


    def __get_token(self):
        timestamp = int(time.time())
        md5_format_str = "%s\n%s\n%s" %(self.username,timestamp,self.token_id)
        obj = hashlib.md5()
        obj.update(md5_format_str)
        return obj.hexdigest()[10:17], timestamp

    def get_server_list(self):
        md5_token,timestamp = self.__get_token()
        url_arg_str = "user=%s&timestamp=%s&token=%s" %(self.username,timestamp,md5_token)
        new_url = self.url + 'servers/'
        new_url += "?" + url_arg_str
        rsp = requests.get(new_url,headers={
            'Accept': 'application/json'
        })
        return rsp

    def get_server(self):
        pass

    def update_server(self):
        pass

    def delete_server(self):
        pass

if __name__ == '__main__':
    rest_client = RestFulClient()
    result = rest_client.get_server_list()
    print result.text