#coding:utf-8
from tools.ReadData import ReadData


# 邮箱元素值
def Ele_Email():
    ele_email = ReadData.getxml("ForgetPassword.xml","ElementValue","email")
    return ele_email

#图形验证码元素值
def Ele_Imagecode():
    ele_imagecode = ReadData.getxml("ForgetPassword.xml","ElementValue","imagecode")
    return ele_imagecode

