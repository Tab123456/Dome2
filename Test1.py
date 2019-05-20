
#TestClass
#定语一个Person人类
class Person:
	#定义属性
	name='张三'
	age=20
	id='50023419991245678X'
	#定义方法
	def fun1(self):
		print('姓名:%s\n年龄:%d\n身份证:%s\n' %(self.name,self.age,self.id))
#定义Student
class Student(Person):
	#定义属性
	number=100
	#定义方法
	def fun1(self):
	#super().  调用父类
		super().fun1()
		print('用户学号:%d' %self.number)
#实例化对象
new=Student()
new.fun1()
