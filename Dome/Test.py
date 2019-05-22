#定义一个学生类
class student():
#定义属性
    def __init__(self,name,age,scores):
        self.name=name
        self.age=age
        self.scores=scores
#定义姓名方法
    def get_name(self):
        print('姓名:',self.name)
#定义年龄方法
    def get_age(self):
        print('年龄:',self.age)
#定义成绩方法
    def get_scores(self):
        print('最高分数:',max(self.scores))
#实例化对象
zm= student('zhangming',20,[69,88,100])
#调用对象
zm.get_name()
zm.get_age()
zm.get_scores()
