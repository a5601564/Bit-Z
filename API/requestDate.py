#coding:utf-8

import  requests
import json

def GET(url,para=None,headers=None):
    try:
        date = requests.get(url,params=para,headers=headers)
        Date = date.text
        redate = json.loads(Date)
        return redate
    except  BaseException as e:
        return "请求失败！",str(e)

def POST(url,para,headers):
    try:
        date = requests.post(url,date=para,headers=headers)
        Date = date.text
        redate = json.loads(Date)
        return date.status_code(),redate
    except BaseException as e:
        return "请求失败！",str(e)

def POST_JSON(url,para,headers):
    try:
        de=para
        de=json.dumps(de)
        date = requests.post(url,para=de,headers=headers)
        Date = date.text
        redate = json.loads(Date)
        return date.status_code(),redate
    except BaseException as e:
        return "请求失败！",str(e)
