s#coding:utf-8
class assertions(object):
    def Contrast_expected_actual(self,expected,actual):
        "验证预期结果和实际结果是否一致"
        try:
            #预期结果==实际结果
            assert expected == actual
        except Exception:
            # """#不一致   #输出预期结果   #实际结果"""
            assert False,\
            "预期结果：%s;实际结果：%s" % (expected,actual)
        else:
            #一致  输出预期结果
            print expected