#coding=utf-8


class Animal():


    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

class Dog(Animal):


    def bark(self):
        print("汪汪汪")



class XiaoTianQuan(Dog):


    def fly(self):
        print("我会飞")
wangcai = Dog()
dongwu  = Animal()
wangcai.run()
wangcai.eat()
wangcai.drink()
wangcai.sleep()
#dongwu没有这个方法
#dongwu.bark()

wangcai.bark()

print("-" * 50)
xiaotianquan = XiaoTianQuan()
xiaotianquan.bark()
xiaotianquan.sleep()
xiaotianquan.run()
xiaotianquan.eat()
xiaotianquan.drink()
xiaotianquan.fly()
