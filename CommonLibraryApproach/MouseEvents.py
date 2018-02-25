#coding:utf-8
from selenium.webdriver.common.action_chains import ActionChains
from    setting.OpenBrowser import openBrowser
class MouseEvents(object):
    def __init__(self):
        self.driver = openBrowser().driver

    #模拟鼠标点击
    def MouseClick(self,Element=None):
        __Click = ActionChains(self.driver).click(Element)
        return __Click

    #模拟鼠标单击并保持,点击一个元素并保持，参数为一个元素
    def Mouse_Click_and_hold(self,Element=None):
        __Click_Hold = ActionChains(self.driver).click_and_hold(Element)
        return __Click_Hold

    #模拟鼠标右击,右击一个元素，参数为一个元素
    def Mouse_Context_Click(self,Element=None):
        __Context_Click = ActionChains(self.driver).context_click(Element)
        return __Context_Click

    #模拟鼠标双击,双击一个元素，参数为一个元素
    def Mouse_Double_Click(self,Element=None):
        __Double_Click = ActionChains(self.driver).double_click(Element)
        return __Double_Click

    #模拟鼠标将一个元素拖至另外一个元素,将source元素拖放至target元素处，参数为两个元素
    def Mouse_Drag_and_Drop(self,source, targe):
        __Drag_and_Drop = ActionChains(self.driver).drag_and_drop(source,targe)
        return __Drag_and_Drop

    #模拟鼠标将一个元素拖放至另外一个位置
    def Mouse_drag_and_drop_by_offset(self,source, xoffset, yoffset):    #将source元素拖放到xoffset, yoffse位置，xy为整形
        __Drag_and_drop_by_offset = ActionChains(self.driver).drag_and_drop_by_offset(source, xoffset, yoffset)
        return __Drag_and_drop_by_offset

    #模拟键盘按下某个按键,按下某个按键如ctrl,shift,alt，参数为一个按键和一个元素（可为空
    def Keyboard_Key_Down(self,value, element=None):
        __Key_Down = ActionChains(self.driver).key_down(value, element=None)
        return __Key_Down

    #模拟键盘松开一个按键，配合Keyboard_Key_Down一起使用,方法为松开某个按键如ctrl,shift,alt，参数为一个按键和一个元素（可为空）
    def Keyboard_Key_Up(self,value, element=None):
        __Key_Up = ActionChains(self.driver).key_up(value, element=None)
        return __Key_Up

    #模拟鼠标移动一段横纵距离,移动鼠标至指定的坐标，参数为两个数值（需为整形
    def Move_By_Offset(self,xoffset, yoffse):
        __By_Offset = ActionChains(self.driver).move_by_offset(xoffset, yoffse)
        return __By_Offset

    #移动鼠标至一个指定的元素，参数为一个元素
    def Move_to_element(self,element):
        __dri = self.driver.find_element_by_id(element)
        __To_Element = ActionChains(self.driver).move_to_element(__dri).click()
        return __To_Element

    #移动鼠标至一个指定的元素，参数为一个元素，和两个整形数字
    def move_to_element_with_offset(self, to_element, xoffset, yoffset):
        __Move_to_element_with_offset = ActionChains(self.driver).move_to_element_with_offset(to_element, xoffset, yoffset)
        return __Move_to_element_with_offset

    #松开鼠标,和拖放等一起使用
    def Move_releas(self,on_element=None):
        __Move_releas = ActionChains(self.driver).release(on_element=on_element)
        return __Move_releas

