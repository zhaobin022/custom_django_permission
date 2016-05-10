#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import time,hashlib,json
import models
from django.shortcuts import render,HttpResponse
import settings

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token

def json_date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.strftime("%Y-%m-%d")


def json_datetime_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.strftime("%Y-%m-%d %H:%M:%S")


def gen_token(username,timestamp,token):
    token_format = "%s\n%s\n%s" %(username,timestamp,token)
    print token_format
    obj = hashlib.md5()
    obj.update(token_format)
    #print '--->token format:[%s]'% token_format
    return obj.hexdigest()[10:17]


def token_required(func):
    def wrapper(*args,**kwargs):
        response = {"errors":[]}
        request = args[0]
        get_args = request.GET
        username = get_args.get("user")
        token_md5_from_client = get_args.get("token")
        timestamp = get_args.get("timestamp")
        if not username or not timestamp or not token_md5_from_client:
            response['errors'].append({"auth_failed":"This api requires token authentication!"})
            return HttpResponse(json.dumps(response))
        try:
            print username
            user_obj = models.UserProfile.objects.get(username=username)
            print user_obj
            user_token = Token.objects.update_or_create(user=user_obj)
            token_md5_from_server = gen_token(username,timestamp,user_token[0].key)
            if token_md5_from_client != token_md5_from_server:
                response['errors'].append({"auth_failed":"Invalid username or token_id"})
            else:
                if abs(time.time() - int(timestamp)) > settings.TOKEN_TIMEOUT:# default timeout 120
                    response['errors'].append({"auth_failed":"The token is expired!"})
                else:
                    pass #print "\033[31;1mPass authentication\033[0m"

                print "\033[41;1m;%s ---client:%s\033[0m" %(time.time(),timestamp), time.time() - int(timestamp)
        except ObjectDoesNotExist,e:
            response['errors'].append({"auth_failed":"Invalid username or token_id"})
        if response['errors']:
            return HttpResponse(json.dumps(response))
        else:
            return  func(*args,**kwargs)
    return wrapper



