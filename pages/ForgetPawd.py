#coding:utf-8
from CommonLibraryApproach.ElementsIde import ElementsIde

class   ForgotPassword(object):

    #邮箱
    def Email(self):
        email = ""
        try:
            ElementsIde().elementID("forgot_myem").send_keys(email)
        except  Exception:
            return "输入邮箱失败！"

    #图形验证码
    def ImageCode(self):
        code = ""
        try:
            ElementsIde().elementID("forgot_code").send_keys(code)
        except  Exception:
            return "输入图形验证码失败！"

    #确定按钮
    def Submit(self):
        try:
            ElementsIde().elementID("forgot_btn").click()
        except  Exception:
            return "点击确定按钮失败！"