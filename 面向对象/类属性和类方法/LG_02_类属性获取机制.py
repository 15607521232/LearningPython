#coding=utf-8


class Tools():

    #使用赋值语句定义类属性，记录所有工具对象的方法
    count = 0

    def __init__(self,name):
        self.name = name

    #让类的属性值加1

        Tools.count += 1


#创建工具对象
tool1 = Tools("斧头")
tool2 = Tools("铲子")
tool3 = Tools("枪")

#输出工具对象的总数

#print(Tools.count)

#使用对象获取类属性，python 获取类属性的向上查找机制
print(tool3.count)