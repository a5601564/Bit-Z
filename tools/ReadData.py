#coding:utf-8
"""
读取XML文档数据
"""
from xml.dom    import minidom
class   ReadData(object):
    def getxml(self, _filename, firstnode, secondnode):
        filename = minidom.parse("../data/" + _filename)
        a = filename.documentElement  # 解析xml文档
        # ?a = minidom.parse(filename)
        oneNode = a.getElementsByTagName(firstnode)[0]
        twonode = oneNode.getElementsByTagName(secondnode)[0].childNodes[0].nodeValue
        return twonode
class readxml():
    def getxml(self,_filename,firstnode,secondnode):
        filename=minidom.parse("../data001/"+_filename)
        a=minidom.parse(filename)
        oneNode=a.getElementsByTagName(firstnode)[0]
        twonode=oneNode.getElementsByTagName(secondnode)[0].childNodes[0].nodeValue
        return twonode