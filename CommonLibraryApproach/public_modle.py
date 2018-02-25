#coding:utf-8
import random
class publicModle():
    #生成随机数
    def RandomData(self):
        #生成0-50之间的随机数
        _randomNum   =   random.randint(0,10)
        return _randomNum

    #读取文件
    def ReadFile(self,path):

        __file  =   open(path,"r")
        __lines =   __file.readlines()#读取全部内容
        for line    in __lines:
            return line

    #写文件
    def WriteFine(self,path,text):
        __file  =   open(path,"r+")#可读可写
        __file.write(text)#写入文本

    #随机生成手机号
    def RandomPhone(self):
        prelist =   ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        _randomPre  =   random.choice(prelist)
        _Number     ="".join(random.choice("0123456789") for i in range(8))
        _phoneNum   =   _randomPre  +   _Number
        return _phoneNum
    #随机生成邮箱
    # 可以指定邮箱类型和邮箱长度
    def RandomEmail(self,emailType=None,rang=None):

        __emailtype = ["@qq.com", "@163.com", "@126.com", "@189.com"]
        #如果没有指定邮箱类型，默认在 __emailtype中随机一个
        if  emailType   ==  None:
            __randomEmail = random.choice(__emailtype)
        else:
            __randomEmail = emailType
        #如果没有指定邮箱长度，默认在4-10之间随机
        if  rang        ==  None:
            __rang = random.randint(4, 10)
        else:
            __rang  =   int(rang)
        __Number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
        __randomNumber = "".join(random.choice(__Number) for i in range(__rang))
        _email           =  __randomNumber  +    __randomEmail
        return _email

    #随机生成密码
    def RandomPasswd(self,rang=None):
        __numlist   =   ['0','1','2','3','4','5','6','7','8','9','q','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',            'q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','W','R','S','T',           'U','V','W','X','Y','Z']
        if  rang    ==  None:
            _Passwd = "".join(random.choice(__numlist) for i in range(8))
        else:
            _Passwd     =   "".join(random.choice(__numlist) for i in range(int(rang)))
        return _Passwd