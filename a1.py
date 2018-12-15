#类的定义
class Student():
    name = '戚成明'
    age = 21

    def __init__(self): #构造函数
        print('')
    def print_file(self):
        print('name: ' + self.name)
        print('age: ' + str(self.age))


student = Student()
student.print_file()
