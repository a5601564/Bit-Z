#coding:utf-8

from setting.OpenBrowser import openBrowser
from CommonLibraryApproach.public_modle import publicModle
from CommonLibraryApproach.ElementsIde import ElementsIde
from tools.ReadData import ReadData
from selenium.webdriver.support.select import Select
import time

class Sigup(object):

    # Email
    def Eamil(self):
        __email = publicModle().RandomEmail()
        try:
            ElementsIde().elementID("email").send_keys(__email)
        except  Exception:
            return "输入邮箱失败！"

    # Password
    def Password(self):
        paw = "qwerqwer"
        try:
            ElementsIde().elementID("pwd").send_keys(paw)
        except  Exception:
            return "输入密码失败！"

    # Repeat Password
    def Repeat_Password(self):
        rpaw = "qwerqwer"
        try:
            ElementsIde().elementID("repwd").send_keys(rpaw)
        except  ElementsIde:
            return "输入确认密码失败！"

    # 邀请人
    def Invite(self):
        uid = ""
        try:
            ElementsIde().elementID("pid").send_keys(uid)
        except  Exception:
            return "添加邀请人失败！"

    #图片验证码
    def Ver_Code(self):
        vercode = ""
        try:
            ElementsIde().elementID("captcha").send_keys(vercode)
        except  Exception:
            return "输入图形验证码失败！"

    #用户协议
    def Terms(self):
        try:
            ElementsIde().elementID("reg_agck").click()
        except  Exception:
            return "勾选用户协议失败！"

    def Sumbit(self):
        try:
            ElementsIde().elementID("reg_btn").click()
        except  Exception:
            return "点击注册按钮失败！"

