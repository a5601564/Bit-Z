#coding:utf-8

from CommonLibraryApproach.ElementsIde import ElementsIde

class SignIn(object):

    #用户名 == 邮箱
    def Email(self):
        email = ""
        try:
            ElementsIde().elementID("lg_myem").send_keys()
        except  Exception:
            return "登录输入用户名失败！"

    #密码
    def Password(self):
        pwd = "qwerqweqr"
        try:
            ElementsIde().elementID("lg_mypsw").send_keys()
        except  Exception:
            return "登录输入密码失败！"

    #登录按钮
    def SignInButton(self):
        try:
            ElementsIde().elementID("lg_btn").click()
        except  Exception:
            return "点击登录按钮失败！"

    #忘记密码
    def ForgotPwd(self):
        try:
            ElementsIde().elementID("lg_forgot").click()
        except  Exception:
            return "点击忘记密码失败！"

    #注册
    def SignUp(self):
        try:
            ElementsIde().elementID("lg_creat").click()
        except  Exception:
            return "点击注册失败！"