#coding:utf-8
"""
    功能页面：登录
"""

from    CommonLibraryApproach.ElementsIde import ElementsIde

class   SignIN():

    #邮箱
    def Email(self):
        __Email=""
        try:
            ElementsIde().elementXpath(".//*[@id='lg_myem']").send_keys(__Email)
        except  Exception:
            return "输入邮箱错误！！！"

    #密码
    def PassWd(self):
        __PassWd = ""
        try:
            ElementsIde().elementXpath(".//*[@id='lg_mypsw']").send_keys(__PassWd)
        except  Exception:
            return "输入密码错误！！！"

    # 登录按钮
    def SignInButton(self):
        try:
            ElementsIde().elementID("lg_btn").click()
        except  Exception:
            return "点击登录按钮失败！"

    # 忘记密码
    def ForgotPwd(self):
        try:
            ElementsIde().elementID("lg_forgot").click()
        except  Exception:
            return "点击忘记密码失败！"

    # 注册
    def SignUp(self):
        try:
            ElementsIde().elementID("lg_creat").click()
        except  Exception:
            return "点击注册失败！"

    #错误信息
    def ErrorValue(self):
        try:
            __ErrorValue    =   ElementsIde().elementXpath(".//*[@id='login_fm']/div/div[5]/p").text
            if  __ErrorValue == "Please enter email" or "Account does not exist":
                ElementsIde().elementXpath(".//*[@id='lg_myem']").click()
                SignIN().Email()
            if  __ErrorValue == "Please enter password" or "Incorrect password ! You left 4 chances !":   #错误字符串错误处理
                ElementsIde().elementXpath(".//*[@id='lg_mypsw']").click()
                SignIN().PassWd()

        except  Exception:
            return  "登录信息无误！"

SignInEmail =   SignIN().Email()
SignInPassWd    =   SignIN().PassWd()
SignInButton    =   SignIN().SignInButton()
SignInForgotPwd =   SignIN().ForgotPwd()
SignInSignUp    =   SignIN().SignUp()